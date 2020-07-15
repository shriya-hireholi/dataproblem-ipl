#Imports

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os

deliveries = pd.read_csv('data_source/deliveries.csv')
matches = pd.read_csv('data_source/matches.csv')


# Merging Two Datasets

data3 = pd.merge(deliveries,matches)
data3.to_csv('data_source/total.csv')

# Total runs scored by team

def total_runs_scored():
    x = data3.groupby(['batting_team'], as_index=False)['total_runs'].count()
    x.to_csv('tables/battingteam_totalruns_table.csv')
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(x.batting_team,x.total_runs, width = 0.5)
    plt.xticks(rotation = 'vertical')
    plt.xlabel('Teams')
    plt.ylabel('Total Runs')
    plt.title('Total runs by Teams')
    for i in range(len(x.total_runs)):
        plt.annotate(str(x.total_runs[i]), xy=(x.batting_team[i], x.total_runs[i]))
    plt.savefig(os.path.join('images/Total runs by Teams.png'), dpi=300, format='png', bbox_inches='tight')
    plt.show()


# Top batsman for Royal Challengers Bangalore

def top_batsman_RCB():
    y = data3.groupby(['batsman','batting_team'], as_index=False)['total_runs'].count()
    
    dict1 = {}
    for i in y.index:
        if((y['batting_team'][i]) == 'Royal Challengers Bangalore'):
            dict1.update({y['batsman'][i]: y['total_runs'][i]})

    z = pd.DataFrame(dict1.items(),columns=['batsman','total_runs'])
    z.to_csv('tables/batsman_totalruns_table.csv')

    fig = plt.figure()
    ax = fig.add_axes([2,2,3,3])
    ax.plot(z.batsman,z.total_runs)
    plt.xticks(rotation = 'vertical')
    plt.xlabel('Batsman')
    plt.ylabel('Total Runs')
    plt.title('Total runs by RCB batsman')

    for i in range(len(z.total_runs)):
        plt.annotate(str(z.total_runs[i]), xy=(z.batsman[i], z.total_runs[i]))
    plt.savefig(os.path.join('images/Total runs by RCB batsman.png'), dpi=300, format='png', bbox_inches='tight')
    plt.show()



#Foreign umpire analysis

def foreign_umpire():
    umpires = pd.read_csv('data_source/umpires.csv')
    u = umpires.groupby(['Umpire','Nationality'], as_index=False)['No. of Matches'].count()
    
    u1 = {}
    for i in u.Nationality:
        if i != 'India' and i in u1:
            u1[i] +=1
        
        if i != 'India' and i not in u1:
            u1[i] = 1

    ump_dataframe = pd.DataFrame(u1.items(),columns=['Nationality','count_ump'])
    ump_dataframe.to_csv('tables/umpire_nationality_count.csv')

    plt.bar(ump_dataframe.Nationality, ump_dataframe.count_ump)

    plt.xticks(rotation = 'vertical')
    plt.xlabel('Nationality')
    plt.ylabel('Count of Umpire')
    plt.title('Foreign umpire analysis')

    for i in range(len(ump_dataframe.count_ump)):
        plt.annotate(str(ump_dataframe.count_ump[i]), xy=(ump_dataframe.Nationality[i], ump_dataframe.count_ump[i]))
    
    plt.savefig(os.path.join('images/Foreign umpire analysis.png'), dpi=300, format='png', bbox_inches='tight')
    plt.show()


#Stacked chart of matches played by team by season

def matches_team_season():
    selected_columns = data3[["date","batting_team","season"]]
    new_df = selected_columns.copy()

    df1 = new_df.drop_duplicates()
    d = df1.pivot_table(index = 'season', margins=all, columns= 'batting_team' ,values = 'date' ,aggfunc='count', fill_value=0)
    
    d.reset_index(inplace=True)
    d.drop('All', axis=1, inplace = True)
    d.drop(10, inplace = True)
    d.to_csv('tables/season_team.csv')

    d.plot.bar(x = 'season', figsize=(20,10), width = 0.8)
    plt.xlabel('Seasons')
    plt.ylabel('Matches Played')
    plt.title('Number of Matches Played by Teams by Seasons')

    plt.savefig(os.path.join('images/Matches Played by Teams by Seasons.png'), dpi=300, format='png', bbox_inches='tight')
    plt.show()


#Calling all the functions

total_runs_scored()

top_batsman_RCB()

foreign_umpire()

matches_team_season()