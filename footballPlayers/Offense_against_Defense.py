import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc

def stats_against_rbs():
    url = 'https://www.pro-football-reference.com/years/2021/fantasy-points-against-RB.htm'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                                                 'Chrome/103.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(r.text, 'html.parser')
    game_table = soup.find('table', id='fantasy_def')

    player_dict = {'name': [], 'link': [], 'gamesPlayed':[], 'rush_att':[], 'rush_yds':[], 'rush_td':[],
                   'targets':[], 'rec':[], 'rec_yds':[], 'rec_td':[], 'fantasy_points':[],'draftkings_points':[],
                   'fanduel_points':[], 'fantasy_points_per_game':[], 'draftkings_points_per_game':[],
                   'fanduel_points_per_game':[]}

    for team in game_table.find_all('tbody'):
        rows = team.findAll('tr')
        for row in rows:
            player_dict['name'].append(row.find('a').text)
            pl_link = row.find('a', href=True)
            player_dict['link'].append(pl_link['href'])
            player_dict['gamesPlayed'].append(row.find('td', {'data-stat': 'g'}).text)
            player_dict['rush_att'].append(row.find('td', {'data-stat': 'rush_att'}).text)
            player_dict['rush_yds'].append(row.find('td', {'data-stat': 'rush_yds'}).text)
            player_dict['rush_td'].append(row.find('td', {'data-stat': 'rush_td'}).text)
            player_dict['targets'].append(row.find('td', {'data-stat': 'targets'}).text)
            player_dict['rec'].append(row.find('td', {'data-stat': 'rec'}).text)
            player_dict['rec_yds'].append(row.find('td', {'data-stat': 'rec_yds'}).text)
            player_dict['rec_td'].append(row.find('td', {'data-stat': 'rec_td'}).text)
            player_dict['fantasy_points'].append(row.find('td', {'data-stat': 'fantasy_points'}).text)
            player_dict['draftkings_points'].append(row.find('td', {'data-stat': 'draftkings_points'}).text)
            player_dict['fanduel_points'].append(row.find('td', {'data-stat': 'fanduel_points'}).text)
            player_dict['fantasy_points_per_game'].append(row.find('td', {'data-stat': 'fantasy_points_per_game'}).text)
            player_dict['draftkings_points_per_game'].append(row.find('td', {'data-stat': 'draftkings_points_per_game'}).text)
            player_dict['fanduel_points_per_game'].append(row.find('td', {'data-stat': 'fanduel_points_per_game'}).text)

    df = pd.DataFrame.from_dict(player_dict)

    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=BEUDYFUL\\SQLEXPRESS;DATABASE=FantasyFootball;Trusted_Connection=yes;')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS dbo.DefenseRbFantasy')

    cursor.execute('''CREATE TABLE [dbo].[DefenseRbFantasy](
               	[DeRbId] [int] IDENTITY(1,1) NOT NULL,
               	[nameDefense] [nvarchar](255) NOT NULL,
               	[link] [nvarchar](255) NOT NULL,
               	[gamesPlayed] [int] NULL,
               	[rush_att] [decimal](18,2) NULL,
               	[rush_yds] [decimal](18,2) NULL,
               	[rush_td] [decimal](18,2) NULL,
               	[pass_targets] [decimal](18,2) NULL,
               	[pass_recep] [decimal](18,2) NULL,
               	[receiving_yds] [decimal](18,2) NULL,
               	[receiving_td] [decimal](18,2) NULL,
               	[fantasy_points] [nvarchar](50) NULL,
               	[draftkings_points] [nvarchar](50) NULL,
               	[fanduel_points] [nvarchar](50) NULL,
               	[fantasy_points_per_game] [decimal](18,2) NULL,
               	[draftkings_points_per_game] [decimal](18,2) NULL,
               	[fanduel_points_points_per_game] [decimal](18,2) NULL,
               ) ON [PRIMARY] ''')

    insert_query = '''INSERT INTO DefenseRbFantasy(nameDefense, link, gamesPlayed, rush_att, rush_yds,
    rush_td, pass_targets, pass_recep, receiving_yds, receiving_td, fantasy_points, draftkings_points,
    fanduel_points, fantasy_points_per_game, draftkings_points_per_game, fanduel_points_points_per_game) 
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
    for index, row in df.iterrows():
        values = (
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
        row[11], row[12], row[13], row[14], row[15])

        cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()

    return df

def defense_against_te():
    url = 'https://www.pro-football-reference.com/years/2021/fantasy-points-against-TE.htm'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                                                 'Chrome/103.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(r.text, 'html.parser')
    game_table = soup.find('table', id='fantasy_def')

    player_dict = {'name': [], 'link': [], 'gamesPlayed': [], 'targets': [], 'rec': [], 'rec_yds': [], 'rec_td': [],
                   'fantasy_points': [], 'draftkings_points': [], 'fanduel_points': [], 'fantasy_points_per_game': [],
                   'draftkings_points_per_game': [], 'fanduel_points_per_game': []}

    for team in game_table.find_all('tbody'):
        rows = team.findAll('tr')
        for row in rows:
            player_dict['name'].append(row.find('a').text)
            pl_link = row.find('a', href=True)
            player_dict['link'].append(pl_link['href'])
            player_dict['gamesPlayed'].append(row.find('td', {'data-stat': 'g'}).text)
            player_dict['targets'].append(row.find('td', {'data-stat': 'targets'}).text)
            player_dict['rec'].append(row.find('td', {'data-stat': 'rec'}).text)
            player_dict['rec_yds'].append(row.find('td', {'data-stat': 'rec_yds'}).text)
            player_dict['rec_td'].append(row.find('td', {'data-stat': 'rec_td'}).text)
            player_dict['fantasy_points'].append(row.find('td', {'data-stat': 'fantasy_points'}).text)
            player_dict['draftkings_points'].append(row.find('td', {'data-stat': 'draftkings_points'}).text)
            player_dict['fanduel_points'].append(row.find('td', {'data-stat': 'fanduel_points'}).text)
            player_dict['fantasy_points_per_game'].append(row.find('td', {'data-stat': 'fantasy_points_per_game'}).text)
            player_dict['draftkings_points_per_game'].append(
                row.find('td', {'data-stat': 'draftkings_points_per_game'}).text)
            player_dict['fanduel_points_per_game'].append(row.find('td', {'data-stat': 'fanduel_points_per_game'}).text)

    df = pd.DataFrame.from_dict(player_dict)

    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=BEUDYFUL\\SQLEXPRESS;DATABASE=FantasyFootball;Trusted_Connection=yes;')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS dbo.DefenseTeFantasy')

    cursor.execute('''CREATE TABLE [dbo].[DefenseTeFantasy](
                   	[DeTeId] [int] IDENTITY(1,1) NOT NULL,
                   	[nameDefense] [nvarchar](255) NOT NULL,
                   	[link] [nvarchar](255) NOT NULL,
                   	[gamesPlayed] [int] NULL,	
                   	[pass_targets] [decimal](18,2) NULL,
                   	[pass_recep] [decimal](18,2) NULL,
                   	[receiving_yds] [decimal](18,2) NULL,
                   	[receiving_td] [decimal](18,2) NULL,
                   	[fantasy_points] [nvarchar](50) NULL,
                   	[draftkings_points] [nvarchar](50) NULL,
                   	[fanduel_points] [nvarchar](50) NULL,
                   	[fantasy_points_per_game] [decimal](18,2) NULL,
                   	[draftkings_points_per_game] [decimal](18,2) NULL,
                   	[fanduel_points_points_per_game] [decimal](18,2) NULL,
                   ) ON [PRIMARY] ''')

    insert_query = '''INSERT INTO DefenseTeFantasy(nameDefense, link, gamesPlayed, pass_targets, pass_recep,
     receiving_yds, receiving_td, fantasy_points, draftkings_points, fanduel_points, fantasy_points_per_game, 
     draftkings_points_per_game, fanduel_points_points_per_game) 
                      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);'''
    for index, row in df.iterrows():
        values = (
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
            row[11], row[12])

        cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()

    return df

def defense_against_wr():
    url = 'https://www.pro-football-reference.com/years/2021/fantasy-points-against-WR.htm'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                                                 'Chrome/103.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(r.text, 'html.parser')
    game_table = soup.find('table', id='fantasy_def')

    player_dict = {'name': [], 'link': [], 'gamesPlayed': [], 'targets': [], 'rec': [], 'rec_yds': [], 'rec_td': [],
                   'fantasy_points': [], 'draftkings_points': [], 'fanduel_points': [], 'fantasy_points_per_game': [],
                   'draftkings_points_per_game': [], 'fanduel_points_per_game': []}

    for team in game_table.find_all('tbody'):
        rows = team.findAll('tr')
        for row in rows:
            player_dict['name'].append(row.find('a').text)
            pl_link = row.find('a', href=True)
            player_dict['link'].append(pl_link['href'])
            player_dict['gamesPlayed'].append(row.find('td', {'data-stat': 'g'}).text)
            player_dict['targets'].append(row.find('td', {'data-stat': 'targets'}).text)
            player_dict['rec'].append(row.find('td', {'data-stat': 'rec'}).text)
            player_dict['rec_yds'].append(row.find('td', {'data-stat': 'rec_yds'}).text)
            player_dict['rec_td'].append(row.find('td', {'data-stat': 'rec_td'}).text)
            player_dict['fantasy_points'].append(row.find('td', {'data-stat': 'fantasy_points'}).text)
            player_dict['draftkings_points'].append(row.find('td', {'data-stat': 'draftkings_points'}).text)
            player_dict['fanduel_points'].append(row.find('td', {'data-stat': 'fanduel_points'}).text)
            player_dict['fantasy_points_per_game'].append(row.find('td', {'data-stat': 'fantasy_points_per_game'}).text)
            player_dict['draftkings_points_per_game'].append(
                row.find('td', {'data-stat': 'draftkings_points_per_game'}).text)
            player_dict['fanduel_points_per_game'].append(row.find('td', {'data-stat': 'fanduel_points_per_game'}).text)

    df = pd.DataFrame.from_dict(player_dict)

    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=BEUDYFUL\\SQLEXPRESS;DATABASE=FantasyFootball;Trusted_Connection=yes;')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS dbo.DefenseWrFantasy')

    cursor.execute('''CREATE TABLE [dbo].[DefenseWrFantasy](
                   	[DeWrId] [int] IDENTITY(1,1) NOT NULL,
                   	[nameDefense] [nvarchar](255) NOT NULL,
                   	[link] [nvarchar](255) NOT NULL,
                   	[gamesPlayed] [int] NULL,	
                   	[pass_targets] [decimal](18,2) NULL,
                   	[pass_recep] [decimal](18,2) NULL,
                   	[receiving_yds] [decimal](18,2) NULL,
                   	[receiving_td] [decimal](18,2) NULL,
                   	[fantasy_points] [nvarchar](50) NULL,
                   	[draftkings_points] [nvarchar](50) NULL,
                   	[fanduel_points] [nvarchar](50) NULL,
                   	[fantasy_points_per_game] [decimal](18,2) NULL,
                   	[draftkings_points_per_game] [decimal](18,2) NULL,
                   	[fanduel_points_points_per_game] [decimal](18,2) NULL,
                   ) ON [PRIMARY] ''')

    insert_query = '''INSERT INTO DefenseWrFantasy(nameDefense, link, gamesPlayed, pass_targets, pass_recep,
     receiving_yds, receiving_td, fantasy_points, draftkings_points, fanduel_points, fantasy_points_per_game, 
     draftkings_points_per_game, fanduel_points_points_per_game) 
                      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);'''
    for index, row in df.iterrows():
        values = (
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
            row[11], row[12])

        cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()

    return df


def defense_against_qb():
    url = 'https://www.pro-football-reference.com/years/2021/fantasy-points-against-QB.htm'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                                                 'Chrome/103.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(r.text, 'html.parser')
    game_table = soup.find('table', id='fantasy_def')

    player_dict = {'name': [], 'link': [], 'gamesPlayed': [], 'pass_cmp': [], 'pass_att':[],
                   'pass_yds':[], 'pass_td':[], 'pass_int':[], 'two_pt_pass':[], 'pass_sacked':[],
                   'rush_att':[], 'rush_yds':[], 'rush_td':[], 'fantasy_points':[], 'draftkings_points':[],
                   'fanduel_points':[], 'fantasy_points_per_game':[], 'draftkings_points_per_game':[],
                   'fanduel_points_per_game':[]}

    for team in game_table.find_all('tbody'):
        rows = team.findAll('tr')
        for row in rows:
            player_dict['name'].append(row.find('a').text)
            pl_link = row.find('a', href=True)
            player_dict['link'].append(pl_link['href'])
            player_dict['gamesPlayed'].append(row.find('td', {'data-stat': 'g'}).text)
            player_dict['pass_cmp'].append(row.find('td', {'data-stat': 'pass_cmp'}).text)
            player_dict['pass_att'].append(row.find('td', {'data-stat': 'pass_att'}).text)
            player_dict['pass_yds'].append(row.find('td', {'data-stat': 'pass_yds'}).text)
            player_dict['pass_td'].append(row.find('td', {'data-stat': 'pass_td'}).text)
            player_dict['pass_int'].append(row.find('td', {'data-stat': 'pass_int'}).text)
            player_dict['two_pt_pass'].append(row.find('td', {'data-stat': 'two_pt_pass'}).text)
            player_dict['pass_sacked'].append(row.find('td', {'data-stat': 'pass_sacked'}).text)
            player_dict['rush_att'].append(row.find('td', {'data-stat': 'rush_att'}).text)
            player_dict['rush_yds'].append(row.find('td', {'data-stat': 'rush_yds'}).text)
            player_dict['rush_td'].append(row.find('td', {'data-stat': 'rush_td'}).text)
            player_dict['fantasy_points'].append(row.find('td', {'data-stat': 'fantasy_points'}).text)
            player_dict['draftkings_points'].append(row.find('td', {'data-stat': 'draftkings_points'}).text)
            player_dict['fanduel_points'].append(row.find('td', {'data-stat': 'fanduel_points'}).text)
            player_dict['fantasy_points_per_game'].append(row.find('td', {'data-stat': 'fantasy_points_per_game'}).text)
            player_dict['draftkings_points_per_game'].append(row.find('td', {'data-stat': 'draftkings_points_per_game'}).text)
            player_dict['fanduel_points_per_game'].append(row.find('td', {'data-stat': 'fanduel_points_per_game'}).text)

    df = pd.DataFrame.from_dict(player_dict)

    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=BEUDYFUL\\SQLEXPRESS;DATABASE=FantasyFootball;Trusted_Connection=yes;')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS dbo.DefenseQbFantasy')

    cursor.execute('''CREATE TABLE [dbo].[DefenseQbFantasy](
                   	[DeQbId] [int] IDENTITY(1,1) NOT NULL,
                   	[nameDefense] [nvarchar](255) NOT NULL,
                   	[link] [nvarchar](255) NOT NULL,
                   	[gamesPlayed] [int] NULL,	
                   	[pass_completed] [decimal](18,2) NULL,
                   	[pass_attempts] [decimal](18,2) NULL,
                   	[passing_yds] [decimal](18,2) NULL,
                   	[passing_td] [decimal](18,2) NULL,
                   	[interceptions] [decimal](18,2) NULL,
                   	[two_point_conv] [nvarchar](255) NULL,
                   	[sacks] [decimal](18,2) NULL,
                   	[rush_att] [decimal](18,2) NULL,
                   	[rush_yds] [decimal](18,2) NULL,
                   	[rush_td] [decimal](18,2) NULL,
                   	[fantasy_points] [nvarchar](50) NULL,
                   	[draftkings_points] [nvarchar](50) NULL,
                   	[fanduel_points] [nvarchar](50) NULL,
                   	[fantasy_points_per_game] [decimal](18,2) NULL,
                   	[draftkings_points_per_game] [decimal](18,2) NULL,
                   	[fanduel_points_points_per_game] [decimal](18,2) NULL,
                   ) ON [PRIMARY] ''')

    insert_query = '''INSERT INTO DefenseQbFantasy(nameDefense, link, gamesPlayed, pass_completed, pass_attempts,
    passing_yds, passing_td, interceptions, two_point_conv, sacks, rush_att, rush_yds, rush_td, fantasy_points,
    draftkings_points, fanduel_points, fantasy_points_per_game, draftkings_points_per_game, fanduel_points_points_per_game) 
                      VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
    for index, row in df.iterrows():
        values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                  row[13], row[14], row[15], row[16], row[17], row[18])

        cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()

    return df