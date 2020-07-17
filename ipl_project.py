# Imports

import csv
from matplotlib import pyplot as plt
import os
from ipl_teams import teams as team_list


def total_runs_scored():

    with open('data_source/deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        runs_scored = {}
        next(csv_reader)
        for row in csv_reader:
            team = row[2]
            runs_scored[team] = runs_scored.get(team, 0) + 1

    x, y = zip(*runs_scored.items())
    plt.figure(figsize=(15, 10))
    plt.bar(x, y)
    plt.title("Total runs by Teams")
    plt.ylabel("Total Runs")
    plt.xlabel("Teams")
    plt.xticks(rotation=' vertical ')
    plt.savefig(
        os.path.join('images/Total runs by Teams.png'),
        dpi=300, format='png', bbox_inches='tight'
        )
    plt.show()


def top_batsman_rcb():

    with open('data_source/deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        rcb_batsman = {}
        next(csv_reader)
        for row in csv_reader:
            team = row[2]
            batsman = row[6]
            batsman_run = int(row[15])
            if team == 'Royal Challengers Bangalore':
                rcb_batsman[batsman] = rcb_batsman.get(batsman, batsman_run)
                + batsman_run

    x, y = zip(*rcb_batsman.items())
    plt.figure(figsize=(15, 10))
    plt.plot(x, y)
    plt.title("otal runs by RCB batsman")
    plt.ylabel("Total Runs")
    plt.xlabel("Batsman")
    plt.xticks(rotation='vertical')
    plt.savefig(os.path.join(
        'images/Total runs by RCB batsman.png'),
         dpi=300, format='png', bbox_inches='tight'
        )
    plt.show()


def foreign_umpire():

    with open('data_source/umpires.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        umpire_country_count = {}
        for row in csv_reader:
            country = row[1]
            if country == 'India':
                continue
            umpire_country_count[country] = umpire_country_count.get(
                country, 0) + 1

    x, y = zip(*umpire_country_count.items())
    plt.figure(figsize=(15, 10))
    plt.bar(x, y)
    plt.title("Foreign umpire analysis")
    plt.ylabel("Count of Umpire")
    plt.xlabel("Nationality")
    plt.xticks(rotation=' vertical')
    plt.savefig(
        os.path.join('images/Foreign umpire analysis.png'),
        dpi=300, format='png', bbox_inches='tight'
        )
    plt.show()


def matches_team_season():
    with open('data_source/matches.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        matches = []
        for i in csv_reader:
            matches.append(i)

    with open('data_source/deliveries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        deliveries = []
        for i in csv_reader:
            deliveries.append(i)

    def merge(lst1, lst2):
        return [a + [b[1]] for (a, b) in zip(lst1, lst2)]

    mergedlst = merge(deliveries, matches)

    i = 0
    s = {}

    for r in mergedlst:
        if i == 0:
            i += 1
        else:
            if r[21] not in s:
                if r[21] not in s:
                    s[r[21]] = {}

    for i in team_list:
        for key in sorted(s):
            s[key][i] = 0

    for x in matches:
        if x[1] in s and x[4] in s[x[1]] and x[5] in s[x[1]]:
            s[x[1]][x[4]] += 1
            s[x[1]][x[5]] += 1

    teams = {}
    years = []

    for key, team_dict in s.items():
        years.append(key)
        for team, pop in sorted(team_dict.items()):
            if team not in teams:
                teams[team] = []
            teams[team].append(pop)

    years = sorted(years)
    teams_count = sorted(teams.keys())
    year_sum = [0]*len(years)
    bar_graphs = []

    for team in teams_count:
        graph = plt.bar(years, teams[team], bottom=year_sum)
        bar_graphs.append(graph[0])
        year_sum = [year_sum[i] + teams[team][i] for i in range(len(years))]

    plt.legend(bar_graphs, teams_count)
    plt.savefig(
        os.path.join('images/Matches Played by Teams by Seasons.png'),
        dpi=300, format='png', bbox_inches='tight'
    )
    plt.show()


def main():
    total_runs_scored()
    top_batsman_rcb()
    foreign_umpire()
    matches_team_season()


if __name__ == '__main__':
    main()
