# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:20:03 2020

@author: Gary Perrier
"""

import csv
import pandas as pd

playerstats = pd.read_csv('playerstats.csv')
teamstats = pd.read_csv('teamstats.csv')

playerstats = playerstats.set_index('PLAYER_NAME')
teamstats = teamstats.set_index('TEAM')

#base stats
def base_stats_player(player):
    kill = playerstats.loc[player, ['KILL']]
    #The total number of kills earned by a player or team
    dth = playerstats.loc[player, ['DEATH']]
    #The total number of deaths earned by a player or team
    assist = playerstats.loc[player, ['ASSIST']]
    #The total number of assists earned by a player or team
    cs = playerstats.loc[player, ['CS']]
    #The number of minions killed plus the "score" earned for jungle monsters (i.e. one camp = 4 CS)
    gold = playerstats.loc[player, ['GOLD']]
    #Total gold earned by a player or team
    xp = playerstats.loc[player, ['XP']]
    #Experience earned by a player or team
    dmg = playerstats.loc[player, ['DAMAGE']]
    #damage dealt by player or team
    print('Base stats of:', player, '\n' 'Kills:', kill, '\n' 'Deaths:', dth, '\n' 'Assists:', assist, '\n' 'Creep Score:', cs, '\n' 'Gold:', gold, '\n' 'Experience:', xp, '\n' 'Damage:', dmg)
    # I know this styling is terrible but I can't seem to make a multi line print statement work
    return
def base_stats_team(team):
    drakes = teamstats.loc['team',['DRAKE']]
    print(team, 'had', drakes, 'drakes')
    #The number of Drakes + Dragons taken by a team
    towers = teamstats.loc['team',['TOWER']]
    print(team, 'had', towers, 'towerss')
    #The number of towers taken by a team
    heralds = teamstats.loc['team',['HERALD']]
    print(team, 'had', heralds, 'heralds')
    #The number of rift heralds taken by a team
    return
#calculated stats
def calc_stats(player):
    k = playerstats.loc[player, ['KILL']]
    d = playerstats.loc[player, ['DEATH']]
    a = playerstats.loc[player, ['ASSIST']]
    g = playerstats.loc[player, ['GOLD']]
    cs = playerstats.loc[player, ['CS']]
    xp = playerstats.loc[player, ['XP']]
    dmg = playerstats.loc[player, ['DAMAGE']]
    t = 39.2
    kda = (k + a)/d
    #The ratio of a player or team's kills and assists to deaths
    print(player, 'KDA (calculated):', kda)
    k_d_a = k + '/' + d + '/' + a
    print(player, 'K/D/A (scoreline):', k_d_a)
    #The scoreline of a player or team
    k_a = k+a
    print(player,'Kills+Assists:', k_a)
    #The sum of a player or team's kills and assists
    dmg_gold = dmg / g
    print(player, 'Damage dealth per gold:', dmg_gold)
    #Damage dealt to champions per gold earned by a player
    ck_m = k / t
    print(player, 'Kills per minute:', ck_m)
    #The total number of kills in a team's games per minute of game time
    cs_m = cs/t
    print(player, 'CS per minute:', cs_m)
    #The creep score earned by a player or team per minute of game time
    gold_m = g/t
    print(player, 'Gold per minute:', gold_m)
    #The amount of gold earned by a player or team per minute of game time
    xp_m = xp/t
    print(player,'Experience per minute:', xp_m)
    #The amount of experience earned by a player or team per minute of game time
    dmg_m = dmg/t
    print(player,'Damage dealt per minute:', dmg_m)
    #The amount of damage dealt to champions by a player or team per minute of game time
    return

#shares
def calc_shares(team, player):
    #Be sure to use the team a player is on, otherwise the stat is pointless
    k = playerstats.loc[player, ['KILL']]
    g = playerstats.loc[player, ['GOLD']]
    cs = playerstats.loc[player, ['CS']]
    dmg = playerstats.loc[player, ['DAMAGE']]
    tk = teamstats.loc['team', ['KILL']]
    tg = teamstats.loc['team', ['GOLD']]
    tcs = teamstats.loc['team', ['CS']]
    tdmg = teamstats.loc['team', ['DAMAGE']]
    kill_s = (k / kt) * 100
    print(player, 'Kill share:', kill_s, '%')
    #The portion of a player's team's total kills that they have earned (i.e. their kills / team total kills)
    dmg_s = (dmg / tdmg) * 100
    print(player,'Damage share:', dmg_s, '%')
    #The portion of a damage to champions a player deals out of their team's total damage dealt
    gold_s = (g / tg) * 100
    print(player, 'Gold share:', gold_s,'%')
    #The portion of a gold a player earns out of their team's total gold
    cs_s = (cs / tcs) * 100
    print(player, 'CS share:',cs_s,'%')
    #The portion of CS a player earns out of the total CS their team earns from 15-30 minutes 
    return 

#differences
def differences(player1,player2):
    #obviously the players roles are dependent on how the differences will look
    #will be very skewed if you calculate the csd of support vs a mid laner
    #a negative value indicates they were behind, a positive number indicated they were ahead
    g1 = playerstats.loc['player1', ['GOLD']]
    cs1 = playerstats.loc['player1', ['CS']]
    xp1 = playerstats.loc['player1', ['XP']]
    dmg1 = playerstats.loc['player1', ['DAMAGE']]    
    g2 = playerstats.loc['player2', ['GOLD']]
    cs2 = playerstats.loc['player2', ['CS']]
    xp2 = playerstats.loc['player2', ['XP']]
    dmg2 = playerstats.loc['player2', ['DAMAGE']]
    t = 39.2
    csd = cs1 - cs2
    print(player1, 'had a', csd, 'cs difference against', player2)
    #The difference between a player's CS and their opponent's CS (e.g. top lane vs top lane)
    gd = g1 - g2
    print(player1, 'had a', gd, 'gold difference against', player2)
    #The difference between a player's gold earned and their opponent's gold earned
    xpd = xp1 - xp2
    print(player1, 'had a', xpd, 'xp difference against', player2)
    #The difference between a player's experience earned and their opponent's experience earned
    dpmd = (dmg1 / t) - (dmg2/ t)
    print(player1, 'had a', dpmd, 'dpm difference against', player2)
    #The difference between a player's damage per minute and their opponent's DMG/M
    return