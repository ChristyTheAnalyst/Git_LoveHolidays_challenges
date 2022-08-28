# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 08:08:12 2022

@author: Christy
"""

# To calculate the distance I will use Geopy python package
from geopy.distance import geodesic

# Creating the dataframe
import pandas as pd

d = {'hotelID':[1,2,3],
        'longitude':[-0.118092,-73.935242,-0.013589],
        'latitude':[51.509865,40.730610,30.123456]}
df = pd.DataFrame(d)
print(df.head())

# Building custom funtion to display nearest hotels for each hotelID in the dataframe
def findNearestHotel(dFrame):
    """ 
    This function returns a dictionary with key as hotel IDs,
    and values as a list of hotelIds nearest to it in ascending order.
    *** Assuming the dataFrame has no null values and hotelIDs are unique"""
    
    d2={}
    for i in range(len(list(dFrame['hotelID']))):
        tempDict = {}
        # print(dFrame['hotelID'][i])
        
        origin = (dFrame['latitude'][i],dFrame['longitude'][i])
        
        for j in range(len(list(dFrame['hotelID']))):
            if(dFrame['hotelID'][i] != dFrame['hotelID'][j]):
                # creating a tuple to calculate the distance
                t = (dFrame['latitude'][j],dFrame['longitude'][j])
                
                # calculating the distance
                tempDict[dFrame['hotelID'][j]] = round(geodesic(origin,t).miles,2)
        
        d2[dFrame['hotelID'][i]] = sorted(tempDict, key=tempDict.get)
        print("hotelID:",dFrame['hotelID'][i], end=" ")
        print(tempDict)
    
    return d2
        
findNearestHotel(df)
