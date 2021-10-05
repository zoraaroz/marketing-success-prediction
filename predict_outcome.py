# load libraries
import pickle
import numpy as np
import pandas as pd
from datetime import date

# print welcome messages
print('Hello. I am here to help you find the right offer for your customer.\n')

# load portfolio features and create input data frame
portfolio_features = pd.read_csv('data/portfolio_features.csv')
X_input = portfolio_features.drop(['offer_id', 'duration', 'offer_type'], axis = 1)

##### input block for the demographic data #####
# gender
while True:
    g = int(input('Please enter the gender of your customer [0 = female, 1 = male, 2 = other]: '))
    if g in [0, 1, 2]: # make sure the gender is valid
        X_input['gender'] = g
        break
    else:
        print('The gender you entered is invalid --> 0 = female, 1 = male, 2 = other')

# age
while True:
    a = int(input('Please enter the age of your customer: '))
    if a in range(15,101): # make sure the age is in a resonable range
        X_input['age'] = a
        break
    else:
        print('Are you sure your customer is {} years old?!'.format(a))

# income
while True:
    i = int(input('Please enter the annual income of your customer: '))
    if i >= 0: # make sure the income is positive
        X_input['income'] = i
        break
    else:
        print('The income has to be a postive number.')

# membership duration
while True:
    d = input('When did your customer become a member? Please enter the date in the format YYYYMMDD: ')
    try:
        d_date = pd.to_datetime(d, format = '%Y%m%d')
        duration = int((pd.to_datetime(date.today()) - d_date)/np.timedelta64(1, 'D'))
        if (d_date <= pd.to_datetime(date.today())) & (duration/365 < (a-15)):
            X_input['membership_duration'] = duration
            break
        else:
            print('Your customer became a member before they were born or when they were still a child.')
    except Exception:
        print('Your date appears to be invalid.')

# load model, prredict and print the outcome
model = pickle.load(open('model/outcome_prediction.pkl', 'rb'))
predicted_outcome = pd.DataFrame(model.predict(X_input), columns = ['outcome'])
# convert numeric offer outcome
predicted_outcome.replace(0, 'success', inplace = True)
predicted_outcome.replace(1, 'waste', inplace = True)
predicted_outcome.replace(2, 'failure', inplace = True)
predicted_outcome.replace(3, 'potential', inplace = True)
# load portfolio data frame
portfolio = pd.read_csv('data/portfolio.csv')
# remove informational offers
portfolio = portfolio[(portfolio.offer_id != '3f207df678b143eea3cee63160fa8bed') & # offer id of informational offer
                     (portfolio.offer_id != '5a8bc65990b245e5a138643cd4eb9837')] # offer id of informational offer
# concat with predicted outcome
portfolio_predicted = pd.concat([portfolio.reset_index(drop = True), predicted_outcome], axis = 1)
# print result
print('\n\n These are the predicted outcomes for the offers in the portfolio:\n')
print(portfolio_predicted)
