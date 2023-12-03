# Group18._FinalProject_SleepDisorder_prediction

Sleep Health and Lifestyle Prediction Model
This repository contains the code and trained models for predicting sleep health based on lifestyle factors.

Overview
This project aims to develop a model capable of predicting an individual's sleep health based 
on various lifestyle factors such as physical activity level, age, stress level, heart rate, 
sleep duration, gender, BMI group, blood pressure, and occupation.

The project utilizes a variety of techniques including data exploration, feature selection, 
and model training with different algorithms like MLP, Random Forest, and XGBoost.

Data:
Sleep_health_and_lifestyle_dataset.csv: The dataset contains information about various factors such as age, gender, 
BMI, physical activity level,stress level, heart rate, sleep duration, blood pressure, and sleep disorder


Data Analysis and Preprocessing
We began by exploring the dataset through data visualization and statistical analysis. 
We then preprocessed the data by handling missing values, encoding categorical features, and scaling numerical features.

Feature Selection and Engineering
We employed various feature selection techniques to identify the most relevant features for predicting sleep quality. 
We also engineered new features based on existing ones to improve model performance.

Models:
Multi-layer Perceptron (MLP): A type of neural network used for classification.
Random Forest: An ensemble learning method that combines multiple decision trees to improve accuracy.
XGBoost: A gradient boosting framework that is highly efficient and accurate for classification task

Model Building and Evaluation
We built and evaluated several machine learning models, including Random Forest, XGBoost, and a multi-layer perceptron (MLP). 
We used hyperparameter tuning to optimize the performance of each model.

Results
The project achieved the following results:

MLP Model:
Test Accuracy: 89.33%
Random Forest Model:
Test Accuracy: 88%
XGBoost Model:
Test Accuracy: 91%


Deployment of Local Server
1.Install Streamlit:
pip install streamlit
2.Create a Streamlit app file, for example app.py.
3.In the app file, import the trained models and any other necessary libraries.
4.Define a function that takes user input for the relevant features and returns the predicted sleep health using the chosen model.
5.Create a Streamlit interface to accept user input and display the predicted sleep health.
6.Run the Streamlit app:
streamlit run app.py

Video Demonstration
https://youtu.be/5NBoAlQ5sjE

