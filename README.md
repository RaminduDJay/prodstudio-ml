# Project Review Status Classification

A machine learning system that predicts the review status of projects (Approved, Rejected, Needs Review) based on project attributes such as title, description, synopsis, production details, crew roles, and casting roles.

## Overview

This project implements a classification model that determines whether a project submission should be automatically approved, rejected, or flagged for manual review. The system analyzes various aspects of a project submission, including:

- Text content (title, description, synopsis)
- Production details (dates, locations)
- Crew and casting information (roles, compensation, demographics)
- Project metadata (type, creator package tier, etc.)

The machine learning pipeline includes comprehensive data preparation, model development, evaluation, and deployment components.


## Installation

1. Clone the repository:
```
git clone https://github.com/username/project-review-classifier.git
cd project-review-classifier
```

2. Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Install additional NLTK resources:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
```

## Data Processing

The data preparation pipeline includes:

### Text Preprocessing
- Lowercasing
- Punctuation removal
- Stopword removal
- Lemmatization/stemming
- Sentiment analysis
- Readability metrics

### JSON Field Processing
- Extraction of production location features
- Analysis of crew roles and compensation
- Cast diversity metrics
- Role importance identification

### Date Feature Engineering
- Project duration calculation
- Lead time analysis
- Season identification

### Missing Value Handling
- Median imputation for numerical features
- Most frequent value imputation for categorical features


## Model Training

The model training process includes:

### Baseline Models
- Dummy Classifier (majority class)
- Logistic Regression
- Decision Tree

### Advanced Models
- Random Forest
- Gradient Boosting
- XGBoost
- Support Vector Machine

### Evaluation Metrics
- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix
- ROC Curves
- Cross-Validation

### Feature Importance
- Tree-based feature importance
- Permutation importance


## Deployment

The model deployment components include:

### Prediction Functions
- Single-instance prediction
- Batch prediction
- Input validation and error handling

### Web Service
- Flask API implementation
- JSON request/response format
- Error handling
- Logging

To run the deployment notebook:
```
jupyter notebook notebooks/3_model_deployment.ipynb
```

To start the API service:
```
python app/flask_api.py
```


```

### Batch Prediction

For batch prediction, use the provided batch prediction function in the deployment notebook, or implement a batch endpoint in the API.

## Monitoring

The monitoring system tracks:

- Prediction logs
- Performance metrics
- Data drift
- Model confidence

To view monitoring metrics:
```
python scripts/monitor_model.py
```

## Future Improvements

- Implement deep learning models for text processing
- Add more sophisticated NLP features like topic modeling
- Develop an ensemble approach combining multiple models
- Create a real-time dashboard for monitoring
- Implement automated retraining when performance degrades
- Add explainability features using SHAP or LIME

