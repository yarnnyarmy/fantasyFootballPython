import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc
from footballPlayers.Wr import Wr

wr = Wr()

def get_all_wr():
    url = 'https://www.pro-football-reference.com/fantasy/WR-fantasy-matchups.htm'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                                                 'Chrome/103.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(r.text, 'html.parser')
    game_table = soup.find('table', id='fantasy_stats')

    player_dict = {'name': [], 'link': [], 'team': [], 'injury': [], 'gamesPlayed': [], 'gamesStarted': [], 'snaps': [],
                   'targets': [], 'rec': [], 'rec_yds': [], 'rec_td': [], 'fantasy_points_per_game': [],
                   'draftkings_points_per_game,': [],
                   'fanduel_points_per_game': [], 'opp': [], 'ranker': [], 'opp_fantasy_points_per_game': [],
                   'opp_draftkings_points_per_game': [], 'opp_fanduel_points_per_game': [],
                   'fantasy_points_proj_rank': [],
                   'draftkings_points_proj_rank': [], 'fanduel_points_proj_rank': []}

    for team in game_table.find_all('tbody'):
        rows = team.findAll('tr')
        for row in rows:
            player_dict['name'].append(row.find('a').text)
            pl_link = row.find('a', href=True)
            player_dict['link'].append(pl_link['href'])
            player_dict['team'].append(row.find('td', {'data-stat': 'team'}).text)
            player_dict['injury'].append(row.find('td', {'data-stat': 'injury'}).text)
            player_dict['gamesPlayed'].append(row.find('td', {'data-stat': 'g'}).text)
            player_dict['gamesStarted'].append(row.find('td', {'data-stat': 'gs'}).text)
            player_dict['snaps'].append(row.find('td', {'data-stat': 'snaps'}).text)
            player_dict['targets'].append(row.find('td', {'data-stat': 'targets'}).text)
            player_dict['rec'].append(row.find('td', {'data-stat': 'rec'}).text)
            player_dict['rec_yds'].append(row.find('td', {'data-stat': 'rec_yds'}).text)
            player_dict['rec_td'].append(row.find('td', {'data-stat': 'rec_td'}).text)
            player_dict['fantasy_points_per_game'].append(row.find('td', {'data-stat': 'fantasy_points_per_game'}).text)
            player_dict['draftkings_points_per_game,'].append(
                row.find('td', {'data-stat': 'draftkings_points_per_game'}).text)
            player_dict['fanduel_points_per_game'].append(
                row.find('td', {'data-stat': 'draftkings_points_per_game'}).text)
            player_dict['opp'].append(row.find('td', {'data-stat': 'opp'}).text)
            player_dict['ranker'].append(row.find('td', {'data-stat': 'ranker'}).text)
            player_dict['opp_fantasy_points_per_game'].append(
                row.find('td', {'data-stat': 'opp_fantasy_points_per_game'}).text)
            player_dict['opp_draftkings_points_per_game'].append(
                row.find('td', {'data-stat': 'opp_draftkings_points_per_game'}).text)
            player_dict['opp_fanduel_points_per_game'].append(
                row.find('td', {'data-stat': 'opp_fanduel_points_per_game'}).text)
            player_dict['fantasy_points_proj_rank'].append(
                row.find('td', {'data-stat': 'fantasy_points_proj_rank'}).text)
            player_dict['draftkings_points_proj_rank'].append(
                row.find('td', {'data-stat': 'draftkings_points_proj_rank'}).text)
            player_dict['fanduel_points_proj_rank'].append(
                row.find('td', {'data-stat': 'fanduel_points_proj_rank'}).text)

    df = pd.DataFrame.from_dict(player_dict)

    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=BEUDYFUL\\SQLEXPRESS;DATABASE=FantasyFootball;Trusted_Connection=yes;')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS dbo.WRFantasy')

    cursor.execute('''CREATE TABLE [dbo].[WRFantasy](
           	[WrId] [int] IDENTITY(1,1) NOT NULL,
           	[nameWr] [nvarchar](255) NOT NULL,
           	[link] [nvarchar](255) NOT NULL,
           	[team] [nvarchar](10) NOT NULL,
           	[injury] [nvarchar](255) NULL,
           	[gamesPlayed] [int] NULL,
           	[gamesStarted] [int] NULL,
           	[snaps] [nvarchar](50) NULL,
           	[pass_targets] [decimal](18,2) NULL,
           	[pass_recep] [decimal](18,2) NULL,
           	[receiving_yds] [decimal](18,2) NULL,
           	[receiving_td] [decimal](18,2) NULL,
           	[fantasy_points] [nvarchar](50) NULL,
           	[draftkings_points] [nvarchar](50) NULL,
           	[fanduel_points] [nvarchar](50) NULL,
           	[opp] [nvarchar](50) NULL,
           	[ranker] [int] NULL,
           	[opp_fantasy_points] [decimal](18,2) NULL,
           	[opp_draftkings_points] [decimal](18,2) NULL,
           	[opp_fanduel_points] [decimal](18,2) NULL,
           	[fantasy_points_proj] [int] NULL,
           	[draftkings_points_proj] [int] NULL,
           	[fanduel_points_proj] [int] NULL
           ) ON [PRIMARY] ''')

    insert_query = '''INSERT INTO WRFantasy(nameWr, link, team, injury, gamesPlayed, gamesStarted, snaps,
           pass_targets, pass_recep, receiving_yds, receiving_td, fantasy_points,
           draftkings_points, fanduel_points,opp, ranker, opp_fantasy_points, opp_draftkings_points,
           opp_fanduel_points, fantasy_points_proj, draftkings_points_proj, fanduel_points_proj) 
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
    for index, row in df.iterrows():
        values = (
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
            row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21])

        cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()

    return df


def csv_to_list_wr():

    all_wrs = []

    new_arr = []

    df = pd.read_csv('C:\\Users\\Yarnell\\Desktop\\week1_nfl.csv', usecols=[2,3,4,5,7,8])

    for i in df.values:
        arr1 = [i[0], i[1], i[2], i[3], i[4], i[5]]
        new_arr.append(arr1)
    wr_dict = {'name': [], 'id': [], 'position': [], 'salary': [], 'team': [], 'draftkings_points': []}
    for i in new_arr:
        if i[2] == 'WR/FLEX':
            wr = Wr()
            wr.set_name(i[0])
            wr.set_id(i[1])
            wr.set_position(i[2])
            wr.set_salary(i[3])
            wr.set_team(i[4])
            wr.set_draftkings_points(i[5])
            all_wrs.append(wr)
            wr_dict['name'].append(wr.get_name())
            wr_dict['id'].append(wr.get_id())
            wr_dict['position'].append(wr.get_position())
            wr_dict['team'].append(wr.get_team())
            wr_dict['draftkings_points'].append(wr.get_draftkings_points())
            wr_dict['salary'].append(wr.get_salary())

    ef = pd.DataFrame(wr_dict)
    ef.to_csv("C:\\Users\Yarnell\\Desktop\\test1.csv", encoding='utf=8', index=False)

    return all_wrs