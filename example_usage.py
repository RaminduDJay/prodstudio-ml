
import pandas as pd
import joblib

# Load the model
model = joblib.load('project_review_classifier_model.pkl')

# Prepare project data (ensure it has all required features)
project_data = pd.DataFrame({
    # Include all project features here
    'project_type_id': ['Documentary'],
    'title': ['Sample Project Title'],
    'description': ['This is a sample project description.'],
    # ... other features
})

# Make prediction
prediction = model.predict(project_data)[0]
probabilities = model.predict_proba(project_data)[0]

print(f"Predicted review status: {prediction}")
print(f"Prediction probabilities: {dict(zip(model.classes_, probabilities))}")
