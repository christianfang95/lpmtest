#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:02:47 2022

@author: christianfang
"""


def assess_predictions(x, y):
    #assess_predictions takes a fitted OLS/LPM model as input (x) as well as the number of decimals to be displayed (y)
    x=x.predict()
    print("======================================================================")
    print("Linear Probability Model Diagnostics")
    print("======================================================================")
    print("Summary of predicted values" )
    print( )
    print("Lowest predicted value: " +  str(round(x.min(),y)))
    print("Highest predicted value: " + str(round(x.max(),y)))
    print( )
    pred2080=x[(x<=0.80) & (x>=0.20)]
    lenpred2080=float(len(pred2080))
    length=float(len(x))
    proplenpre2080=(lenpred2080/length)*100
    print(str(round(proplenpre2080, y)) + "% of predicted values fall in the range 0.2 to 0.8") 
    if x.min() <0 or x.max()>1:
        print("======================================================================")
        print()
        print("Some issues were found with the range of predicted values:")
    else:
        print("No issues were found with the range of predicted values.")
    if x.min() <0:
        print( )
        pred_smaller = x[x<0]
        len_smaller=float(len(pred_smaller))
        print("There are " + str(len(pred_smaller)) + " predicted values smaller than 0.")
        prop_smaller=(len_smaller/length)*100
        print("This is "+ str(round(prop_smaller, y)) + "% of all observations")
    if x.max() >1:
        print( )
        pred_greater = x[x>1]
        len_greater=float(len(pred_greater))
        print("There are " + str(len(pred_greater)) + " predicted values greater than 1.")
        prop_greater=(len_greater/length)*100
        print("This is "+ str(round(prop_greater, y)) + "% of all observations")
    print( )
    print("Predicted values outside of the [0,1] interval can be problematic.")
    print("Consider using a logistic regression model.")

assess_predictions(res, 2)
