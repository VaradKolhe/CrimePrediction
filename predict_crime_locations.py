import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

# Load the data
print("Loading data...")
df = pd.read_csv('raw_crime_data.csv')
df = df.dropna(subset=['latitude', 'longitude', 'Crime Description', 'Date of Occurrence']) #dropping rows with null values

# Convert date string to datetime
df['Date of Occurrence'] = pd.to_datetime(df['Date of Occurrence'])

# Extract temporal features
df['hour'] = df['Date of Occurrence'].dt.hour
df['day_of_week'] = df['Date of Occurrence'].dt.dayofweek
df['month'] = df['Date of Occurrence'].dt.month

# Create risk level based on crime data
# We'll use Crime Code and Crime Description to determine risk level
print("Creating risk levels...")

# Create a risk mapping based on crime severity
crime_risk_mapping = {
    'HOMICIDE': 'High',
    'MURDER': 'High',
    'RAPE': 'High',
    'KIDNAPPING': 'High',
    'SEXUAL ASSAULT': 'High',
    
    'ROBBERY': 'Medium',
    'ASSAULT': 'Medium',
    'EXTORTION': 'Medium',
    'FIREARM OFFENSE': 'Medium',
    'DOMESTIC VIOLENCE': 'Medium',
    'ILLEGAL POSSESSION': 'Medium',
    'DRUG OFFENSE': 'Medium',

    'BURGLARY': 'Low',
    'THEFT': 'Low',
    'FRAUD': 'Low',
    'VANDALISM': 'Low',
    'SHOPLIFTING': 'Low',
    'ARSON': 'Low',
    'TRAFFIC VIOLATION': 'Low',
    'COUNTERFEITING': 'Low',
    'PUBLIC INTOXICATION': 'Low',
    'CYBERCRIME': 'Low',
    'IDENTITY THEFT': 'Low',
    'VEHICLE - STOLEN': 'Low'
}

# Function to determine risk level based on crime description
def get_risk_level(description):
    description = str(description).upper()
    for crime_type, risk in crime_risk_mapping.items():
        if crime_type in description:
            return risk
    return 'Low'  # Default risk level

# Add risk level column
df['risk_level'] = df['Crime Description'].apply(get_risk_level)

# Calculate crime density per area
area_crime_counts = df.groupby('area_location').size()
df['area_crime_density'] = df['area_location'].map(area_crime_counts)

# Calculate crime density per city
city_crime_counts = df.groupby('city').size()
df['city_crime_density'] = df['city'].map(city_crime_counts)

# Calculate crime type frequency
crime_type_counts = df['Crime Description'].value_counts()
df['crime_type_frequency'] = df['Crime Description'].map(crime_type_counts)

# Create time-based features
df['is_night'] = (df['hour'] >= 20) | (df['hour'] <= 5)
df['is_weekend'] = df['day_of_week'].isin([5, 6])
df['is_peak_hour'] = df['hour'].isin([8, 9, 17, 18, 19])

# Calculate split index for 80-20 split
split_idx = int(len(df) * 0.8)

# Split data chronologically
train_df = df.iloc[:split_idx]
test_df = df.iloc[split_idx:]

print(f"Training data size: {len(train_df)}")
print(f"Testing data size: {len(test_df)}")

# Prepare features
feature_columns = [
    'latitude', 'longitude',
    'hour', 'day_of_week', 'month',
    'area_crime_density',
    'city_crime_density',
    'crime_type_frequency',
    'is_night',
    'is_weekend',
    'is_peak_hour'
]

X_train = train_df[feature_columns]
y_train = train_df['risk_level']

X_test = test_df[feature_columns]
y_test = test_df['risk_level']

# Initialize and fit LabelEncoder with all possible classes
le = LabelEncoder()
all_classes = ['High', 'Medium', 'Low']  # All possible risk levels
le.fit(all_classes)

# Transform the labels
y_train_encoded = le.transform(y_train)
y_test_encoded = le.transform(y_test)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Prepare more balanced data with adjusted SMOTE parameters
print("Applying SMOTE for balanced training data...")
smote = SMOTE(random_state=42, k_neighbors=5, sampling_strategy='not majority')
X_train_bal, y_train_bal = smote.fit_resample(X_train_scaled, y_train_encoded)

# Train Random Forest Classifier with adjusted parameters
print("Training Random Forest Classifier...")
rf_classifier = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,      
    min_samples_split=3,  
    min_samples_leaf=1,   
    max_features='sqrt',
    class_weight='balanced',
    random_state=42,
    bootstrap=True,
    oob_score=True
)
rf_classifier.fit(X_train_bal, y_train_bal)

# Make predictions on test data
print("Making predictions...")
predictions = rf_classifier.predict(X_test_scaled)

# Create a new DataFrame with predictions for test data
predicted_df = pd.DataFrame({
    'city': test_df['city'],
    'area': test_df['area_location'],
    'latitude': test_df['latitude'],
    'longitude': test_df['longitude'],
    'risk_level': le.inverse_transform(predictions),
    'crime_description': test_df['Crime Description']  
})

# Save predictions to CSV
print("Saving predictions to predicted_crime_data.csv...")
predicted_df.to_csv('predicted_crime_data.csv', index=False)

# Print model performance
print("\nModel Performance:")
print(f"Accuracy: {accuracy_score(y_test_encoded, predictions):.2f}")
print("\nClassification Report:")
print(classification_report(y_test_encoded, predictions))

# Print feature importance
feature_importance = pd.DataFrame({
    'feature': feature_columns,
    'importance': rf_classifier.feature_importances_
})
print("\nFeature Importance:")
print(feature_importance.sort_values('importance', ascending=False))

print("\nPredictions have been saved to predicted_crime_data.csv") 