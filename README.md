# Crime Prediction Using Random Forest Classifier & HDBSCAN Clustering

This project (ZoneAlert) demonstrates the use of a **Random Forest Classifier** to predict potential crime locations using raw crime data and **HDBSCAN** to cluster and visualize high-risk areas.

---

## Project Pages

- **Home Page**: Overview of the app, model performance, and navigation.
- **Prediction Page**: Select a location and receive predicted crime data.
- **Map Page**: Visual display of clustered crime-prone locations on a map.
- **Contact Page**: Feedback and FAQs for users.

---

## How It Works

### 1. Raw Data Processing
- Input: `raw_crime_data.csv`
- Data is cleaned and preprocessed.
- **SMOTE** is used to balance class distribution.

### 2. Prediction (`predict_crime_locations.py`)
- Model: **Random Forest Classifier** (80:20 train-test split).
- Outputs: `predicted_crime_data.csv`
- Accuracy and metrics calculated (see below).

### 3. Clustering (`cluster_crime_locations.py`)
- Uses **HDBSCAN** for clustering predicted crime locations.
- Clusters are analyzed to determine:
  - Average location
  - Risk level
  - Common crime type
  - Cluster size
- Output saved as `clustered_crime_data.csv`.

---

## Model Performance

- **Overall Accuracy**: `0.84`
- Macro Average F1-Score: `0.83`
- Weighted Average F1-Score: `0.85`

---

## Getting Started

### 1. Create a Virtual Environment
```bash
python -m venv venv
```

### 2. Activate It
- **Windows**: 
```bash
venv\\Scripts\\activate
```
- **Linux/Mac**: 
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Project
```bash
python predict_crime_locations.py
python cluster_crime_locations.py
python app.py
```

---

## Contact

Have suggestions or feedback? Use the **Contact Page** in the app or open an issue.

---

## Tech Stack

- Python 3.x
- Scikit-learn
- HDBSCAN
- Pandas, NumPy
- Flask
- imbalanced-learn (SMOTE)

---

## Note

Only the `raw_crime_data.csv` file is required to run the project. The other csv files are generated after execution.