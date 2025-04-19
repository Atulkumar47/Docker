import pandas as pd
import numpy as np
import joblib
import os
import json
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, ClassificationPreset
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Define paths
PROJECT_DIR = "projects/project_1"
REPORTS_DIR = os.path.join(PROJECT_DIR, "reports")
MODEL_PATH = os.path.join(PROJECT_DIR, "model.pkl")

# Create necessary directories
os.makedirs(REPORTS_DIR, exist_ok=True)

# Load dataset (Simulated Credit Card Fraud Detection Data)
df = pd.DataFrame(np.random.randn(1000, 10), columns=[f"feature_{i}" for i in range(10)])
df['label'] = np.random.randint(0, 2, size=(1000,))

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['label']), df['label'], test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, MODEL_PATH)  # Save the model

# Make predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Generate Evidently AI report
report = Report(metrics=[DataDriftPreset(), ClassificationPreset()])
report.run(reference_data=X_train, current_data=X_test, column_mapping=None)

# Save report as HTML and JSON
html_report_path = os.path.join(REPORTS_DIR, "fraud_detection_report.html")
json_report_path = os.path.join(REPORTS_DIR, "fraud_detection_report.json")

report.save_html(html_report_path)

report_metadata = {
    "model": "RandomForestClassifier",
    "accuracy": accuracy,
    "description": "Fraud detection model monitoring report"
}

with open(json_report_path, "w") as f:
    json.dump(report_metadata, f, indent=4)

print(f"✅ Model training completed. Report saved at: {json_report_path}")
