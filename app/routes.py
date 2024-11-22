from flask import Blueprint, render_template, request
from app.expert_systems import create_expert_system  # Import the function to create the expert system

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/signup', methods=['POST'])
def process_signup():
    # Get data from the form
    email = request.form['email']
    age = int(request.form['age'])
    country = request.form['country']
    income = int(request.form['income'])
    
    # Prepare the user data for evaluation
    user_data = {
        "email": email,
        "age": age,
        "country": country,
        "income": income,
    }
    
    # Create an expert system instance
    expert_system = create_expert_system()

    # Evaluate the user data using the expert system
    result = expert_system.evaluate(user_data)
    
    # Render the dashboard with classification and tier
    return render_template('dashboard.html', email=email, classification=result["classification"], tier=result["tier"])
