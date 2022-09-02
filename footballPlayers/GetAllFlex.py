import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc

from footballPlayers.Flex import Flex

def csv_to_list_flex():
    all_flex = []
    new_arr = []

    df = pd.read_csv('C:\\Users\\Yarnell\\Desktop\\week1_nfl.csv', usecols=[2,3,4,5,7,8])

    for i in df.values:
        arr1 = [i[0], i[1], i[2], i[3], i[4], i[5]]
        new_arr.append(arr1)
    fx_dict = {'name': [], 'id': [], 'position': [], 'salary': [], 'team': [], 'draftkings_points': []}
    for i in new_arr:
        if i[2] != 'QB' and i[2] != 'DST':
            fx = Flex()
            fx.set_name(i[0])
            fx.set_id(i[1])
            fx.set_position(i[2])
            fx.set_salary(i[3])
            fx.set_team(i[4])
            fx.set_draftkings_points(i[5])
            all_flex.append(fx)
            fx_dict['name'].append(fx.get_name())
            fx_dict['id'].append(fx.get_id())
            fx_dict['position'].append(fx.get_position())
            fx_dict['team'].append(fx.get_team())
            fx_dict['draftkings_points'].append(fx.get_draftkings_points())
            fx_dict['salary'].append(fx.get_salary())
            break

    ef = pd.DataFrame(fx_dict)
    ef.to_csv("C:\\Users\Yarnell\\Desktop\\test1.csv", encoding='utf=8', index=False)
    return all_flex