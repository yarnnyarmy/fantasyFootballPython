import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc

from footballPlayers.Defense import Defense

defense = Defense()


def csv_to_list_df():
    all_defense = []
    new_arr = []

    df = pd.read_csv('C:\\Users\\Yarnell\\Desktop\\week1_nfl.csv', usecols=[2,3,4,5,7,8])

    for i in df.values:
        arr1 = [i[0], i[1], i[2], i[3], i[4], i[5]]
        new_arr.append(arr1)

    df_dict = {'name': [], 'id': [], 'position': [], 'salary': [], 'team': [], 'draftkings_points': []}
    for i in new_arr:
        if(i[2] == 'DST'):
            all_def = Defense()
            all_def.set_name(i[0])
            all_def.set_id(i[1])
            all_def.set_position(i[2])
            all_def.set_salary(i[3])
            all_def.set_team(i[4])
            all_def.set_draftkings_points(i[5])
            all_defense.append(all_def)
            df_dict['name'].append(all_def.get_name())
            df_dict['id'].append(all_def.get_id())
            df_dict['position'].append(all_def.get_position())
            df_dict['team'].append(all_def.get_team())
            df_dict['draftkings_points'].append(all_def.get_draftkings_points())
            df_dict['salary'].append(all_def.get_salary())

    # for qb_names in hello:
    #     print(qb_names.get_name())
        #ef.to_csv("C:\\Users\Yarnell\\Desktop\\test1.csv", encoding='utf=8', index=False)

    ef = pd.DataFrame(df_dict)
    ef.to_csv("C:\\Users\Yarnell\\Desktop\\test1.csv", encoding='utf=8', index=False)

    return all_defense
