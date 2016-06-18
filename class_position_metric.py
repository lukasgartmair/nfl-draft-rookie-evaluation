# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:27:46 2016

@author: Lukas Gartmair
"""

import numpy as np
import matplotlib.pyplot as pl
import functools
import pandas as pd 

def conjunction(*conditions):
    return functools.reduce(np.logical_and, conditions)

class Attribute():
        def __init__(self, attribute_name , weight_factor):
            self.attribute_name = attribute_name
            self.weight_factor = weight_factor

class Position_Metric():
    
    def __init__(self, position, features_list):
        self.position = position
        self.features = features_list
        self.additional_criteria_list = []
        self.crit_metric = 0

    def calculate_metric(self, stats):
        # weight factors for the total metric
        # here has to be my own philosophy for which criteria to search
        # means of the evaluations of the scouts
        metric = 0
        for f in self.features:
            low = 'Low_' + f.attribute_name
            high = 'High_'+f.attribute_name
            mean = 0
            mean = stats[[low, high]].mean(axis=1) 
            metric += (mean*f.weight_factor)

        metric /= 1000    
        
        return metric
    
    def get_crit_pos_met(self):
        return self.crit_metric

### general functions


def get_headers(df):
    headers = list(df.columns.values)
    return headers
    

def reorder_data_drame(important,df):
# http://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
    reordered = important + [c for c in df.columns if c not in important]
    df = df[reordered]
    return df

def get_best_metrics(stats):

    positions = ['T','G', 'DT', 'DE', 'OLB', 'QB','WR', 'FB','RB', 'S']
    
    ## make subset of stats total
    position = ''
    final_draftboard = pd.DataFrame()
    final_draftboard['Position_Comparison'] = 0
    
    for position in positions:
        
        pos_prospects = pd.DataFrame()
        pos_prospects = stats[stats['Position_Group'] == (position)]
        
        quantile_metric = pos_prospects[position + '_Metric'].quantile(q=0.8)

        avg = pos_prospects[position + '_Metric'].median()
        final_prospects = pos_prospects[pos_prospects[position + '_Metric'] >= quantile_metric ]

        # a better formula for this would be nice
        final_prospects['Position_Comparison'] =  ((pos_prospects[position + '_Metric'] - avg) / avg)
        
        frames = [final_draftboard, final_prospects]
        final_draftboard = pd.concat(frames)
        
    headers = get_headers(stats)
    final_draftboard = reorder_data_drame(headers, final_draftboard)
        
    final_draftboard = final_draftboard.sort_values(by=['Position_Comparison'],ascending=False)          
        
    return final_draftboard