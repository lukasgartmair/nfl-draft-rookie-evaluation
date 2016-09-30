# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:26:11 2016

@author: Lukas Gartmair
"""

import numpy as np
import matplotlib.pyplot as pl

# normalize all metrics 
def normalize_metrics(stats):
    metric_cols = [col for col in stats.columns if '_Metric' in col]
    
    for mc in metric_cols:
        stats[mc] = stats[mc] / stats[mc].sum()
        
    return stats

def correct_time(dash_or_agility):
    corrected = []
    for d in dash_or_agility:
        if d != 0:
            d = str(d)
            x = d[0] + '.' + d[1] + d[2] 
            corrected.append(float(x))
        else:
            corrected.append(0)
    return corrected


# correct grade
def correct_grade(grade):
    grade_corrected = []
    for g in grade:
        if g != 0:
            g = str(g)
            if int(g) >= 10:
                x = g[0] + '.' + g[1]
            else: 
                x = '0.' + g
            grade_corrected.append(float(x))
        elif int(g) == 100:
            grade_corrected.append(10)
        else:
            grade_corrected.append(0)
    return grade_corrected

# correct broad jump
def correct_broad_jump(broad_jump):
    broad_jump_in_feet = []
    for bj in broad_jump:
        if bj != 0:
            bj = str(bj)
            feet = bj[:-1]
            inches = bj[-1:]
            broad_jump_in_feet.append(int(feet)+(0.0833*int(inches)))
        else:
            broad_jump_in_feet.append(0)
    return broad_jump_in_feet
    
def correct_height(height):
    height_corr = height *2.54 # inches to cm
    return height_corr
    
def correct_weight(weight):
    weight_corrected = weight * 0.453 # from pound to kg
    return  weight_corrected
    
  
def correct_measures(df):  
    
    # correct height
#    height_corrected = correct_height(df['Height'])
#    df['Height'] = height_corrected
    # correct weight
#    weight_corrected = correct_weight(df['Weight'])
#    df['Weight'] = weight_corrected
    # correct dash
    dash_corrected = correct_time(df['Dash'])
    df['Dash'] = dash_corrected
    
    agility_corrected = correct_time(df['Agility'])
    df['Agility'] = agility_corrected
    
    grade_corrected = correct_grade(df['Grade'])
    df['Grade'] = grade_corrected
    
    broad_jump_in_feet = correct_broad_jump(df['Jump'])
    df['Jump'] = broad_jump_in_feet
    explosion_number = df['Strength'] + broad_jump_in_feet
    df['Explosion_Number'] = explosion_number
    
    return df
