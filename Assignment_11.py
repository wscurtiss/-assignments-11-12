import numpy as np
import matplotlib
matplotlib.use('Agg') # This is only required to use matplotlib on Cloud9
import matplotlib.pyplot as plt
import pymongo
from pymongo import MongoClient
x = np.linspace(0,10,11) # This creates an evenly spaced array from 0 to 10 
y = x**2 # This our y array, equals to x squared
print(x)
print(y)
figure, axis = plt.subplots(1, 1) # This create a figure with 1 axis
axis.plot(x, y)
figure.savefig("x_squared.svg")
db = MongoClient("mongodb://mongo0.scitecha.com,mongo1.scitecha.com,mongo2.mrocha.org/mrocha?replicaSet=rs0").mrocha 
user_data = list(db.users.find({}, {"profile.TracyProgress": 1})) # This is the query requesting the TracyProgress data 
                                                                  # from the users collection
tprogress = [user["profile"]["TracyProgress"] for user in user_data] # This converts the result from the query to an 
                                                                     # array containing only the TracyProgress fi
figure, axis = plt.subplots(1, 1) # This create a figure with 1 axis
axis.hist(tprogress, bins=10) # This draws a histogream with 10 bins
figure.savefig('TracyProgress_histogram.svg')