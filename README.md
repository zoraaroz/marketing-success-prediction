## Marketing Success Prediction

### Date created
October 2021

### Description
The basis for this project is a dataset from Starbucks that contains information about customers, about different types of offers made to these customers and about the purchase behaviour of the customers after they received these offers.

From a marketing perspective it is interesting to know if is worth sending offers to certain customers. In order to solve this problem the project takes two steps:

1. A classification model was trained to predict the outcome of an offer depending on features regarding user demographics as well as offer characteristics.
2. This model was used to predict the outcome of each offer in the offer portfolio for any new or existing user.

The resulting python script can be seen as a marketing tool to decide what kind of offers to send to users.

### Usage
#### Prediction model
The implementation in the Jupyter Notebook uses the provided data, cleans and pre-processes the data and trains five different models for predicting the outcome of offers sent to customers. The outcome of each model is evaluated against a test set and the best model is saved into a pickle file.

##### Libraries used
###### General
- import pandas as pd
- import numpy as np
- import json
- import math
- import time
- from datetime import date
- import pickle

###### Plotting
- import matplotlib.pyplot as plt
- import seaborn as sb

###### sklearn
- from sklearn.tree import DecisionTreeClassifier
- from sklearn.naive_bayes import GaussianNB
- from sklearn.neighbors import KNeighborsClassifier
- from sklearn.svm import LinearSVC
- from sklearn.linear_model import LogisticRegression
- from sklearn.ensemble import RandomForestClassifier
- from sklearn.model_selection import train_test_split, GridSearchCV
- from sklearn.metrics import accuracy_score, f1_score

##### Files used
- data/portfolio.json
- data/profile.json
- data/transcript.json

#### Prediction script
To run the prediction script, type

`<python predict_outcome.py>`

into your terminal. You will be prompted to enter demographic data on your customer. Once this is completed, the predicted outcome for all offers in the offer portfolio is presented.

![Screenshot](screenshot.png)

##### Libraries used
- import pickle
- import numpy as np
- import pandas as pd
- from datetime import date

##### Files used
- data/portfolio_features.csv
- data/portfolio.csv
- outcome_prediction.pkl

### Files
- outcome_classification.ipynb – Jupyter notebook used for data cleaning, pre-processing, prediction and model selection
- predict_outcome.py – Script to be used for predicting the outcome of sending the offers to any new user
- data
    - portfolio.json – raw portfolio data
    - profile.json – raw user data
    - transcript.json – raw event data
    - portfolio.csv – cleaned portfolio data
    - portfolio_features.csv – offer features used for prediction
- model
    - outcome_prediction.pkl – saved model
- README.md
- LICENSE

### Credits
The data used was provided by Starbucks.

The idea and task was provided by the [Udacity Data Scientist
Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025) course.

### License
The contents of this repository are covered under the MIT License.
