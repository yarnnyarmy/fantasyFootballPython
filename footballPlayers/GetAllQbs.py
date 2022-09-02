import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc
from footballPlayers.Qb import Qb

allQbs = Qb()


depth_qb = []

player_dict = {'name': [], 'link': [], 'team': [], 'injury': [], 'gamesPlayed': [], 'gamesStarted': [],
               'snaps': [], 'pass_cmp': [], 'pass_att': [], 'pass_yds': [], 'pass_td': [], 'pass_int': [],
               'pass_sacked': [], 'rush_att': [], 'rush_yds': [], 'rush_td': [], 'fantasy_points_per_game': [],
               'draftkings_points_per_game': [], 'fanduel_points_per_game': [], 'opp': [], 'ranker': [],
               'opp_fantasy_points_per_game': [], 'opp_draftkings_points_per_game': [],
               'opp_fanduel_points_per_game': [],
               'fantasy_points_proj_rank': [], 'draftkings_points_proj_rank': [], 'fanduel_points_proj_rank': []}

player_dict_qb = {'name': [], 'stat': []}


def getQbFromTeam(team, year):
    team = team
    year = year
    url = f'https://www.pro-football-reference.com/teams/{team}/{year}_advanced.htm'

    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                                                 'Chrome/103.0.0.0 Safari/537.36'})

    soup = BeautifulSoup(r.text, 'html.parser')

    game_table = soup.find('table', class_='stats_table sortable')

    player_dict = {'name':[], 'link':[], 'age':[], 'pos':[], 'gamesPlayed':[], 'gamesStarted':[],
                   'passComp':[], 'passAtt':[], 'yards':[], 'passTargetYds':[], 'passAirYds':[],
                   'passAirYdsCom':[]}
    for team in game_table.find_all('tbody'):
        rows = team.findAll('tr')
        for row in rows:
            player_dict['name'].append(row.find('a').text)
            pl_link = row.find('a', href=True)

            player_dict['link'].append(pl_link['href'])
            player_dict['age'].append(row.find('td', {'data-stat': 'age'}).text)
            player_dict['pos'].append(row.find('td', {'data-stat': 'pos'}).text)
            player_dict['gamesPlayed'].append(row.find('td', {'data-stat': 'g'}).text)
            player_dict['gamesStarted'].append(row.find('td', {'data-stat': 'gs'}).text)
            player_dict['passComp'].append(row.find('td', {'data-stat': 'pass_cmp'}).text)
            player_dict['passAtt'].append(row.find('td', {'data-stat': 'pass_att'}).text)
            player_dict['yards'].append(row.find('td', {'data-stat': 'pass_yds'}).text)
            player_dict['passTargetYds'].append(row.find('td', {'data-stat': 'pass_target_yds'}).text)
            player_dict['passAirYds'].append(row.find('td', {'data-stat': 'pass_air_yds'}).text)
            player_dict['passAirYdsCom'].append(row.find('td', {'data-stat': 'pass_air_yds_per_cmp'}).text)

    df = pd.DataFrame.from_dict(player_dict)

    return df


def getAllQbs():
    url = 'https://www.pro-football-reference.com/fantasy/QB-fantasy-matchups.htm'
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                                                 'Chrome/103.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(r.text, 'html.parser')

    game_table = soup.find('table', id='fantasy_stats')

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
            player_dict['pass_cmp'].append(row.find('td', {'data-stat': 'pass_cmp'}).text)
            player_dict['pass_att'].append(row.find('td', {'data-stat': 'pass_att'}).text)
            player_dict['pass_yds'].append(row.find('td', {'data-stat': 'pass_yds'}).text)
            player_dict['pass_td'].append(row.find('td', {'data-stat': 'pass_td'}).text)
            player_dict['pass_int'].append(row.find('td', {'data-stat': 'pass_int'}).text)
            player_dict['pass_sacked'].append(row.find('td', {'data-stat': 'pass_sacked'}).text)
            player_dict['rush_att'].append(row.find('td', {'data-stat': 'rush_att'}).text)
            player_dict['rush_yds'].append(row.find('td', {'data-stat': 'rush_yds'}).text)
            player_dict['rush_td'].append(row.find('td', {'data-stat': 'rush_td'}).text)
            player_dict['fantasy_points_per_game'].append(row.find('td', {'data-stat': 'fantasy_points_per_game'}).text)
            player_dict['draftkings_points_per_game'].append(row.find('td', {'data-stat': 'draftkings_points_per_game'}).text)
            player_dict['fanduel_points_per_game'].append(row.find('td', {'data-stat': 'fanduel_points_per_game'}).text)
            player_dict['opp'].append(row.find('td', {'data-stat': 'opp'}).text)
            player_dict['ranker'].append(row.find('td', {'data-stat': 'ranker'}).text)
            player_dict['opp_fantasy_points_per_game'].append(row.find('td', {'data-stat': 'opp_fantasy_points_per_game'}).text)
            player_dict['opp_draftkings_points_per_game'].append(row.find('td', {'data-stat': 'opp_draftkings_points_per_game'}).text)
            player_dict['opp_fanduel_points_per_game'].append(row.find('td', {'data-stat': 'opp_fanduel_points_per_game'}).text)
            player_dict['fantasy_points_proj_rank'].append(row.find('td', {'data-stat': 'fantasy_points_proj_rank'}).text)
            player_dict['draftkings_points_proj_rank'].append(row.find('td', {'data-stat': 'draftkings_points_proj_rank'}).text)
            player_dict['fanduel_points_proj_rank'].append(row.find('td', {'data-stat': 'fanduel_points_proj_rank'}).text)

    df = pd.DataFrame.from_dict(player_dict)

    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=BEUDYFUL\\SQLEXPRESS;DATABASE=FantasyFootball;Trusted_Connection=yes;')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS dbo.QBFantasy')

    cursor.execute('''CREATE TABLE [dbo].[QBFantasy](
	[QbId] [int] IDENTITY(1,1) NOT NULL,
	[nameQb] [nvarchar](255) NOT NULL,
	[link] [nvarchar](255) NOT NULL,
	[team] [nchar](10) NOT NULL,
	[injury] [nvarchar](255) NULL,
	[gamesPlayed] [int] NULL,
	[gamesStarted] [int] NULL,
	[snaps] [nvarchar](50) NULL,
	[pass_cmp] [decimal](18,2) NULL,
	[pass_att] [decimal](18,2) NULL,
	[pass_yds] [decimal](18,2) NULL,
	[pass_td] [nvarchar](50) NULL,
	[pass_int] [decimal](18,2) NULL,
	[pass_sacked] [decimal](18,2) NULL,
	[rush_att] [decimal](18,2) NULL,
	[rush_yds] [decimal](18,2) NULL,
	[rush_td] [decimal](18,2) NULL,
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

    insert_query = '''INSERT INTO QBFantasy(nameQb, link, team, injury, gamesPlayed, gamesStarted, snaps, pass_cmp, pass_att, pass_yds, pass_td, pass_int,
    pass_sacked, rush_att, rush_yds, rush_td, fantasy_points, draftkings_points, fanduel_points, opp, ranker, opp_fantasy_points, opp_draftkings_points,
    opp_fanduel_points, fantasy_points_proj, draftkings_points_proj, fanduel_points_proj) 
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
    for index, row in df.iterrows():
        values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],  row[13], row[14],
                  row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26])
        cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()

    l3 = list(player_dict.values())
    dflist = pd.DataFrame(l3)

    player_new_dict = {'name' : []}
    player_new_dict['name'].append(dflist[0].get(0))
    return player_dict






def get_qbs_projections():
    url = 'https://www.fantasypros.com/nfl/projections/leaders.php'

    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                                 ' AppleWebKit/537.36 (KHTML, like Gecko) '
                                                 'Chrome/103.0.0.0 Safari/537.36'})

    soup = BeautifulSoup(r.text, 'html.parser')

    game_table = soup.find('table', {"class" :'table full-width'})



    for team in game_table.find_all('tbody'):
        rows = team.findAll('tr')
        for row in rows:
            player_dict_qb['name'].append(row.find('a').text)
            player_dict_qb['stat'].append(row.find('strong').text)

    df = pd.DataFrame.from_dict(player_dict_qb)

    return df



def csv_to_list_qbs():
    all_qbs = []
    new_arr = []

    df = pd.read_csv('C:\\Users\\Yarnell\\Desktop\\week1_nfl.csv', usecols=[2,3,4,5,7,8])

    for i in df.values:
        arr1 = [i[0], i[1], i[2], i[3], i[4], i[5]]
        new_arr.append(arr1)
    qb_dict = {'name': [], 'id': [], 'position': [], 'salary': [], 'team': [], 'draftkings_points': []}
    for i in new_arr:
        if i[2] == 'QB':
            qb = Qb()
            qb.set_name(i[0])
            qb.set_id(i[1])
            qb.set_position(i[2])
            qb.set_salary(i[3])
            qb.set_team(i[4])
            qb.set_draftkings_points(i[5])
            all_qbs.append(qb)
            qb_dict['name'].append(qb.get_name())
            qb_dict['id'].append(qb.get_id())
            qb_dict['position'].append(qb.get_position())
            qb_dict['team'].append(qb.get_team())
            qb_dict['draftkings_points'].append(qb.get_draftkings_points())
            qb_dict['salary'].append(qb.get_salary())


    ef = pd.DataFrame(qb_dict)
    ef.to_csv("C:\\Users\Yarnell\\Desktop\\test1.csv", encoding='utf=8', index=False)

    return all_qbs