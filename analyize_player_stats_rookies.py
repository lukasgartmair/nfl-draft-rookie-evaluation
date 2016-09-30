# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:26:03 2016

@author: Lukas Gartmair
"""

import numpy as np
import matplotlib.pyplot as pl
import pandas as pd
import correction_functions
import class_position_metric
from class_position_metric import Attribute

## combine

base_path = 'C:\\Users\Lukas Gartmair\AppData\Roaming\Solecismic Software\Front Office Football Seven\leaguedata\league03\\'

fn = base_path + 'rookies.csv'
#fn = 'rookies.csv'
data_combine = pd.read_csv(fn)
df = pd.DataFrame(data_combine)

df = correction_functions.correct_measures(df)

## scout report  - draft personal (shit name for this content)
fn2 = base_path + 'draft_personal.csv'
#fn2 = 'draft_personal.csv'
data_scouts = pd.read_csv(fn2)
df2 = pd.DataFrame(data_scouts)

# merge the lists
#http://chris.friedline.net/2015-12-15-rutgers/lessons/python2/04-merging-data.html
stats_total = pd.merge(left=df,right=df2, left_on='Player_ID', right_on='Player_ID')



# offensive tackles
# pat kirwan page 99:
#  the right guard and right tackle have to be powerful runblockers first and foremost.
# in pass situations he can get help from te or rb

position = 'T'
feature_list = []
feature_list = [Attribute('Run_Blocking',10),Attribute('Pass_Blocking',5), 
                Attribute('Blocking_Strength',5), Attribute('Endurance',5)]          
                     
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
ot_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                             (stats_total['Explosion_Number'] > 40) &
#                               (stats_total['Developed'] >= 10) &  
#                               (stats_total[position + '_Metric'] > 1) ]
                               
ot_prospects = ot_prospects.sort_values(by=[position + '_Metric'],ascending=False)                

position = 'G'
feature_list = []
feature_list = [Attribute('Run_Blocking',10),Attribute('Pass_Blocking',5), 
                Attribute('Blocking_Strength',5), Attribute('Endurance',5)]          
                     
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
og_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                             (stats_total['Explosion_Number'] > 40) &
#                               (stats_total['Developed'] >= 10) &  
#                               (stats_total[position + '_Metric'] > 1) ]
                               
og_prospects = og_prospects.sort_values(by=[position + '_Metric'],ascending=False)                      
                               
# defensive tackles
# pat kirwan page 125:
# 34 nose tackle height between 6'2 and 6'4 and about 350 pounds
position = 'DT'
feature_list = []
feature_list = [Attribute('Run_Defense',10),Attribute('Pass_Rush_Technique',3), 
                Attribute('Pass_Rush_Strength',3), Attribute('Play_Diagnosis',10),  
                Attribute('Punishing_Hitter',0), Attribute('Endurance',5)]       
                        
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
dt_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                             (stats_total['Explosion_Number'] > 40) &
#                               (stats_total['Developed'] >= 10) &  
#                               (stats_total['Height'] > 75) &
#                               (stats_total['Weight'] > 260) &
#                               (stats_total[position + '_Metric'] > 1.2) ]
dt_prospects = dt_prospects.sort_values(by=[position + '_Metric'],ascending=False)                                 
# defensive ends
# pat kirwan page 125:
# the quintessential defensive end in 34 is: 6'8 height 300 pounds and blessed with long arms
# in 34 the defensive ends are no pass rushers  as you find in 43!
# he has to keep the linebackers free from the blockers, not penetrate the backfield
position = 'DE'
feature_list = []
feature_list = [Attribute('Run_Defense',10),Attribute('Pass_Rush_Technique',3), 
                Attribute('Pass_Rush_Strength',3), Attribute('Play_Diagnosis',10),
                Attribute('Punishing_Hitter',0), Attribute('Endurance',5)]                               
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
de_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                             (stats_total['Explosion_Number'] > 31) &
#                               (stats_total['Developed'] >= 10) &  
#                               (stats_total['Height'] > 75) &
#                               (stats_total['Weight'] > 250) &
#                               (stats_total[position + '_Metric'] > 1.5) ]
de_prospects = de_prospects.sort_values(by=[position + '_Metric'],ascending=False)                                 
                               
# outside linebackers
position = 'OLB'
feature_list = []
feature_list = [Attribute('Run_Defense',5),Attribute('Pass_Rush_Technique',8), 
                Attribute('Man-to-Man_Defense',3),Attribute('Zone_Defense',8), 
                Attribute('Bump-and-Run_Defense',5), Attribute('Pass_Rush_Strength',8),
                Attribute('Play_Diagnosis',8), Attribute('Punishing_Hitter',0), 
                Attribute('Endurance',5)]          
                     
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
olb_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                             (stats_total['Explosion_Number'] > 30) &
#                               (stats_total['Developed'] >= 20) &  
#                               (stats_total['Dash'] < 4.9) &
#                               (stats_total['Strength']) > 2 &
#                               (stats_total['Position_Specific'] > 30) &
#                               (stats_total[position + '_Metric'] > 2) ]        

# outside linebackers
position = 'ILB'
feature_list = []
feature_list = [Attribute('Run_Defense',8),Attribute('Pass_Rush_Technique',4), 
                Attribute('Man-to-Man_Defense',5),Attribute('Zone_Defense',10), 
                Attribute('Bump-and-Run_Defense',5), Attribute('Pass_Rush_Strength',3),
                Attribute('Play_Diagnosis',10), Attribute('Punishing_Hitter',0), 
                Attribute('Endurance',5)]          
                     
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
ilb_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                             (stats_total['Explosion_Number'] > 30) &
#                               (stats_total['Developed'] >= 20) &  
#                               (stats_total['Dash'] < 4.9) &
#                               (stats_total['Strength']) > 2 &
#                               (stats_total['Position_Specific'] > 30) &
#                               (stats_total[position + '_Metric'] > 2) ]     

                               
ilb_prospects = ilb_prospects.sort_values(by=[position + '_Metric'],ascending=False)                                

# quarterbacks
position = 'QB'
feature_list = []
feature_list = [Attribute('Screen_Passes',8),Attribute('Short_Passes',9), 
                Attribute('Medium_Passes',7),Attribute('Long_Passes',5), 
                Attribute('Deep_Passes',0), Attribute('Third_Down',8),
                Attribute('Run_Frequency',0), Attribute('Accuracy',8), 
                Attribute('Timing',5), Attribute('Sense_Rush',7),
                Attribute('Read_Defense',5), Attribute('Two-Minute_Offense',0)]
                               
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
qb_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                               (stats_total['Developed'] >= 20) &  
#                               (stats_total[position + '_Metric'] > 3.0) ]
                               
qb_prospects = qb_prospects.sort_values(by=[position + '_Metric'],ascending=False)                                 

# wide receivers
position = 'WR'
feature_list = []
feature_list = [Attribute('Avoid_Drops',10),Attribute('Get_Downfield',8), 
                Attribute('Route_Running',9),Attribute('Third-Down_Receiving',5), 
                Attribute('Big_Play_Receiving',1), Attribute('Courage',5),
                Attribute('Adjust_to_Ball',7), Attribute('Punt_Returns',0), 
                Attribute('Kick_Returns',0)]
                               
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
wr_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                                (stats_total['Height'] > 70) & 
#                                (stats_total['Dash'] < 4.5) & 
#                                (stats_total['Position_Specific'] > 40    ) & 
#                               (stats_total['Developed'] >= 20) &  
#                               (stats_total[position + '_Metric'] > 1) ]
wr_prospects = wr_prospects.sort_values(by=[position + '_Metric'],ascending=False)                                
                            
# fullbacks
position = 'FB'
feature_list = []
feature_list = [Attribute('Run_Blocking',5), Attribute('Pass_Blocking',5), 
                Attribute('Blocking_Strength',5),
                Attribute('Power_Inside',10),Attribute('Third-Down_Runs',8), 
                Attribute('Hole_Recognition',9),Attribute('Elusiveness',7), 
                Attribute('Speed_Outside',1), Attribute('Blitz_Pickup',5),
                Attribute('Avoid_Drops',3), Attribute('Get_Downfield',1), 
                Attribute('Route_Running',2), Attribute('Third-Down_Receiving',1),
                Attribute('Endurance',5)]
                               
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
fb_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                                (stats_total['Agility'] < 7.5) & 
#                                (stats_total['Dash'] < 4.55) & 
#                               (stats_total['Developed'] >= 20) &  
#                               (stats_total[position + '_Metric'] > 0.5) ]
fb_prospects = fb_prospects.sort_values(by=[position + '_Metric'],ascending=False)  

# running backs
position = 'RB'
feature_list = []
feature_list = [Attribute('Run_Blocking',5), Attribute('Pass_Blocking',5), 
                Attribute('Blocking_Strength',5),
                Attribute('Power_Inside',10),Attribute('Third-Down_Runs',8), 
                Attribute('Hole_Recognition',9),Attribute('Elusiveness',7), 
                Attribute('Speed_Outside',1), Attribute('Blitz_Pickup',5),
                Attribute('Avoid_Drops',3), Attribute('Get_Downfield',1), 
                Attribute('Route_Running',2), Attribute('Third-Down_Receiving',1),
                Attribute('Endurance',5)]
                               
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
rb_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                                (stats_total['Agility'] < 7.5) & 
#                                (stats_total['Dash'] < 4.55) & 
#                               (stats_total['Developed'] >= 20) &  
#                               (stats_total[position + '_Metric'] > 1) ]
rb_prospects = rb_prospects.sort_values(by=[position + '_Metric'],ascending=False)  

# cornerbacks
position = 'CB'
feature_list = []
feature_list = [Attribute('Run_Defense',1), 
                Attribute('Man-to-Man_Defense',3),Attribute('Zone_Defense',9), 
                Attribute('Bump-and-Run_Defense',6),
                Attribute('Play_Diagnosis',8), Attribute('Punishing_Hitter',0), 
                Attribute('Endurance',5)]       
                               
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
cb_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                                (stats_total['Agility'] < 7.5) & 
#                                (stats_total['Dash'] < 4.55) & 
#                               (stats_total['Developed'] >= 20) &  
#                               (stats_total[position + '_Metric'] > 1) ]
cb_prospects = cb_prospects.sort_values(by=[position + '_Metric'],ascending=False)  

# safeties
position = 'S'
feature_list = []
feature_list = [Attribute('Run_Defense',5), 
                Attribute('Man-to-Man_Defense',7),Attribute('Zone_Defense',10), 
                Attribute('Bump-and-Run_Defense',0),
                Attribute('Play_Diagnosis',10), Attribute('Punishing_Hitter',0), 
                Attribute('Endurance',5)]       
                               
pos = class_position_metric.Position_Metric(position,feature_list)
stats_total[position + '_Metric'] = pos.calculate_metric(stats_total)
s_prospects  = stats_total[(stats_total['Position_Group'] == (position)) ]
#                                (stats_total['Agility'] < 7.5) & 
#                                (stats_total['Dash'] < 4.55) & 
#                               (stats_total['Developed'] >= 20) &  
#                               (stats_total[position + '_Metric'] > 1) ]
s_prospects = s_prospects.sort_values(by=[position + '_Metric'],ascending=False)  


###

stats_total = correction_functions.normalize_metrics(stats_total)

final_draftboard = class_position_metric.get_best_metrics(stats_total)




