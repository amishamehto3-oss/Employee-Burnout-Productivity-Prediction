# Employee Burnout & Productivity Prediction System

## Project Overview

The Employee Burnout & Productivity Prediction System is a machine learning-based application developed to predict employee burnout risk and productivity levels using employee and workplace-related information.

The project provides an interactive Streamlit interface where users can enter employee details and obtain burnout and productivity predictions. It also includes a Power BI dashboard and project documentation for analytical and academic purposes.

## Objectives

- Predict employee burnout probability using a trained machine learning model.
- Classify employees into burnout risk categories.
- Predict employee productivity levels.
- Provide an interactive and user-friendly prediction interface.
- Include department and country information in the prediction inputs.
- Provide analytical support for HR decision-making.
- Support early identification of potential burnout and productivity concerns.

## Problem Statement

Employee burnout and declining productivity can negatively affect employee well-being and organizational performance. Traditional approaches may rely heavily on periodic assessments or manual observations, which may make it difficult to identify potential concerns at an early stage.

This project develops a machine learning-based decision-support system that uses employee and workplace-related features to estimate burnout risk and predict productivity levels.

## Proposed Solution

The system contains two main prediction modules.

### Burnout Prediction

The burnout module uses employee information to generate a burnout prediction and probability. The application interprets the probability into:

- Low Burnout Risk
- High Burnout Risk

### Productivity Prediction

The productivity module predicts the employee's productivity level and presents the result as:

- Low Productivity
- Medium Productivity
- High Productivity

## Input Features

### Burnout Prediction

- Gender
- Company Type
- WFH Setup Available
- Department
- Country
- Hours Worked Per Week
- Overtime Hours
- Stress Level
- Satisfaction Score
- Performance Score
- Absenteeism Days
- Burn Rate

### Productivity Prediction

- Gender
- Company Type
- WFH Setup Available
- Department
- Country
- Hours Worked Per Week
- Tasks Completed
- Stress Level
- Satisfaction Score
- Performance Score

## Departments

- IT
- Finance
- HR
- Marketing
- Operations

## Countries

- India
- USA
- Germany
- Indonesia
- Brazil

## Machine Learning Models

The application uses two pre-trained model files:

- `final_burnout_model.pkl`
- `final_productivity_model.pkl`

The models are loaded by the Streamlit application using Python's `pickle` module.

## Application Workflow

```text
Employee Information
        |
        v
Streamlit Interface
        |
   +----+----+
   |         |
   v         v
Burnout   Productivity
 Model       Model
   |         |
   v         v
Burnout   Productivity
Probability Level
   |         |
   v         v
Risk      Low/Medium/High
Level
   \         /
    \       /
     v     v
    HR Decision Support
```

## How the System Can Help HR

### Burnout Prediction

A higher burnout probability can encourage HR to investigate factors such as working hours, overtime, stress, satisfaction, absenteeism, burn rate, and department-level patterns.

Possible interventions include:

- Reviewing employee workload.
- Discussing work-related concerns with the employee.
- Providing appropriate employee support.
- Considering flexible working arrangements where appropriate.
- Reviewing overtime and work allocation.
- Providing mentoring or development support.

The model is intended to identify indicators for further investigation, rather than automatically making decisions about employees.

### Productivity Prediction

Productivity predictions can help HR identify situations that may require additional investigation or support.

Possible actions include:

- Training and skill development.
- Mentoring.
- Reviewing work allocation.
- Performance support.
- Process improvement.
- Additional discussion with employees or managers.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle
- Jupyter Notebook
- Power BI

## Project Structure

```text
Employee-Burnout-Productivity-Prediction/
|
├── Employee_app.py
├── final_burnout_model.pkl
├── final_productivity_model.pkl
├── Employee_Productivity_Burnout_Expanded_10000.csv
├── EmployeesBurnoutAnalysis.pbix
├── Employee_Burnout_Productivity_Presentation.pptx
├── Employee_Insights_Report.docx
├── screenshots/
|   ├── burnout_prediction.png
|   ├── productivity_prediction.png
|   └── dashboard.png
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project directory

```bash
cd Employee-Burnout-Productivity-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run

Run the Streamlit application using:

```bash
streamlit run Employee_app.py
```

The application will normally open at:

```text
http://localhost:8501
```

Make sure the following files are in the same project directory as `Employee_app.py`:

```text
final_burnout_model.pkl
final_productivity_model.pkl
```

## Requirements

The main Streamlit application requires:

```text
streamlit
pandas
numpy
scikit-learn
```

## Power BI Dashboard

The project also includes:

```text
EmployeesBurnoutAnalysis.pbix
```

This file contains the Power BI component of the project and can be opened using Microsoft Power BI Desktop.

## Project Documentation

The repository includes:

- `Employee_Insights_Report.docx` — Final project report.
- `Employee_Burnout_Productivity_Presentation.pptx` — Project presentation.
- `EmployeesBurnoutAnalysis.pbix` — Power BI dashboard.
- `Employee_Productivity_Burnout_Expanded_10000.csv` — Project dataset.

## Screenshots

Add application screenshots to the `screenshots` folder and reference them here.

### Burnout Prediction

![Burnout Prediction](screenshots/burnout_prediction.png)

### Productivity Prediction

![Productivity Prediction](screenshots/productivity_prediction.png)

### Dashboard

![Employee Dashboard](screenshots/dashboard.png)

## Limitations

- The prediction results depend on the quality and characteristics of the data used to develop the models.
- The system should be treated as a decision-support tool.
- Predictions should not be used as the sole basis for employment, disciplinary, or other high-impact HR decisions.
- Additional organizational and employee-related variables may improve future versions of the system.
- Real-world deployment would require appropriate validation using suitable organizational data.

## Future Scope

Future improvements may include:

- Integration with organizational HR systems.
- Validation using appropriately anonymized real-world data.
- Continuous monitoring of employee trends.
- Automated alerts for increasing burnout risk.
- Explainable AI techniques.
- Cloud deployment.
- Real-time HR analytics.
- Additional employee well-being and performance indicators.
- More detailed department-level monitoring.

## Ethical Considerations

Employee-related predictions should be used responsibly. The system should support HR assessment rather than replace professional judgment.

Appropriate privacy, confidentiality, fairness, and transparency practices should be followed before using such a system with real employee information.

## Academic Purpose

This project was developed as an academic machine learning project to demonstrate the application of predictive analytics to employee burnout and productivity analysis.

It combines machine learning, Python programming, Streamlit application development, and HR/business analytics.

## Author

**Amisha Mehto**

MSc Economics & Analytics  
Christ University, Delhi NCR

## Disclaimer

This project is developed for academic and research purposes. The predictions generated by the system are intended to provide analytical and decision-support insights and should not replace professional HR assessment or judgment.
