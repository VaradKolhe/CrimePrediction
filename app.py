from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import random
import pandas as pd

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crime.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_USER')

mail = Mail(app)
db = SQLAlchemy(app)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def get_recommendations(risk_level):
    recommendations = {
        'High': [
            'Avoid walking alone, especially during night hours',
            'Keep emergency contacts readily available',
            'Stay in well-lit and populated areas',
            'Consider using secure transportation services',
            'Be extra vigilant of your surroundings',
            'Keep valuables hidden and secure'
        ],
        'Medium': [
            'Stay aware of your surroundings',
            'Keep valuables secure and out of sight',
            'Travel in groups when possible',
            'Avoid isolated areas',
            'Keep emergency numbers handy'
        ],
        'Low': [
            'Practice general safety awareness',
            'Keep emergency contacts handy',
            'Stay in well-lit areas when possible',
            'Be aware of your surroundings'
        ]
    }
    return random.sample(recommendations[risk_level], k=min(4, len(recommendations[risk_level])))

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        city = data.get('city')
        area = data.get('area')
        
        if not city or not area:
            return jsonify({'error': 'City and area are required'}), 400
        
        # Load clustered data
        clustered_df = pd.read_csv('clustered_crime_data.csv')
        
        # Find matching cluster for the city and area
        matching_cluster = clustered_df[
            (clustered_df['city'] == city) & 
            (clustered_df['area'] == area)
        ]
        
        if matching_cluster.empty:
            return jsonify({'error': 'No data found for the specified location'}), 404
        
        # Get the first matching cluster (there should be only one)
        cluster = matching_cluster.iloc[0]
        
        # Get recommendations based on risk level
        recommendations = get_recommendations(cluster['risk_level'])
        
        return jsonify({
            'risk_level': cluster['risk_level'],
            'probability': 0.8 if cluster['risk_level'] == 'High' else 0.5 if cluster['risk_level'] == 'Medium' else 0.2,
            'likely_crime': cluster['crime_description'],
            'crime_description': cluster['crime_description'],
            'recommendations': recommendations
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/contact', methods=['POST'])
def send_contact_email():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        # Create email message
        msg = Message(
            subject=f"Contact Form: {subject}",
            recipients=['varad4422@gmail.com'],
            body=f"""
            New contact form submission:
            
            Name: {name}
            Email: {email}
            Subject: {subject}
            
            Message:
            {message}
            """
        )
        
        # Send email
        mail.send(msg)
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/get_clustered_data')
def get_clustered_data():
    try:
        # Read the clustered data
        df = pd.read_csv('clustered_crime_data.csv')
        
        # Convert DataFrame to list of dictionaries
        data = df.to_dict('records')
        
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
