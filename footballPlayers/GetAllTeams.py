import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyodbc

from footballPlayers.GetAllDefenses import csv_to_list_df
from footballPlayers.GetAllFlex import csv_to_list_flex
from footballPlayers.GetAllQbs import csv_to_list_qbs
from footballPlayers.GetAllRbs import csv_to_list_rb
from footballPlayers.GetAllTes import csv_to_list_te
from footballPlayers.GetAllWrs import csv_to_list_wr


def get_all_teams():

    rb_list = []
    wr_list = []
    wr_rb_list = []
    all_teams_list = []
    wr_te_rb_list = []
    wr_te_rb_flx_list = []
    qb_rb_wr_te_flx_list = []
    all_teams_dict = {'qb_name':[],'qb_salary':[], 'qb_id':[], 'rb1_name':[], 'rb1_salary':[], 'rb1_id':[], 'rb2_name':[], 'rb2_salary':[], 'rb2_id':[],
                      'wr1_name':[],'wr1_salary':[], 'wr1_id':[],'wr2_name':[], 'wr2_salary':[], 'wr2_id':[], 'wr3_name':[], 'wr3_salary':[], 'wr3_id':[],
                      'te_name':[], 'te_salary':[], 'te_id':[], 'flex_name':[], 'flex_salary':[], 'flex_id':[], 'defense_name':[], 'defense_salary':[], 'defense_id':[]}
    qb = csv_to_list_qbs()
    rb = csv_to_list_rb()
    wr = csv_to_list_wr()
    te = csv_to_list_te()
    defense = csv_to_list_df()
    flex = csv_to_list_flex()

    print("Adding all running backs")
    for a in range(len(rb)):
        firstNameRb = rb[a].get_name()
        firstNameRbId = rb[a].get_id()
        firstNameRbSalary = rb[a].get_salary()
        firstNameRbTeam = rb[a].get_team()
        firstNameRbPosition = rb[a].get_position()
        firstNameRbDkPoints = rb[a].get_draftkings_points()

        for b in range(a):
            rb_newArr = []
            rb_newArr.append(rb[b].get_name())
            rb_newArr.append(rb[b].get_id())
            rb_newArr.append(rb[b].get_salary())
            rb_newArr.append(rb[b].get_team())
            rb_newArr.append(rb[b].get_position())
            rb_newArr.append(rb[b].get_draftkings_points())
            rb_newArr.append(firstNameRb)
            rb_newArr.append(firstNameRbId)
            rb_newArr.append(firstNameRbSalary)
            rb_newArr.append(firstNameRbTeam)
            rb_newArr.append(firstNameRbPosition)
            rb_newArr.append(firstNameRbDkPoints)
            rb_list.append(rb_newArr)

    print("All running backs added")
    print(len(rb_list))
    print("Adding all wide receivers")
    for c in range(len(wr)):
        firstNameWr = wr[c].get_name()
        firstNameWrId = wr[c].get_id()
        firstNameWrSalary = wr[c].get_salary()
        firstNameWrTeam = wr[c].get_team()
        firstNameWrPosition = wr[c].get_position()
        firstNameWrDkPoints = wr[c].get_draftkings_points()
        for d in range(c):
            secondNameWr = wr[d].get_name()
            secondNameWrId = wr[d].get_id()
            secondNameWrSalary = wr[d].get_salary()
            secondNameWrTeam = wr[d].get_team()
            secondNameWrPosition = wr[d].get_position()
            secondNameWrDkPoints = wr[d].get_draftkings_points()
            for e in range(d):
                wr_newArr = []
                wr_newArr.append(wr[e].get_name())
                wr_newArr.append(wr[e].get_id())
                wr_newArr.append(wr[e].get_salary())
                wr_newArr.append(wr[e].get_team())
                wr_newArr.append(wr[e].get_position())
                wr_newArr.append(wr[e].get_draftkings_points())
                wr_newArr.append(secondNameWr)
                wr_newArr.append(secondNameWrId)
                wr_newArr.append(secondNameWrSalary)
                wr_newArr.append(secondNameWrTeam)
                wr_newArr.append(secondNameWrPosition)
                wr_newArr.append(secondNameWrDkPoints)
                wr_newArr.append(firstNameWr)
                wr_newArr.append(firstNameWrId)
                wr_newArr.append(firstNameWrSalary)
                wr_newArr.append(firstNameWrTeam)
                wr_newArr.append(firstNameWrPosition)
                wr_newArr.append(firstNameWrDkPoints)
                wr_list.append(wr_newArr)

    print("All wide receivers added")
    print(len(wr_list))

    print("Adding running backs and wide receivers together")
    for o in rb_list:
        if len(wr_rb_list) > 2000000:
            break
        for p in wr_list:
            add_combo = []
            add_combo.append(o[0])
            add_combo.append(o[1])
            add_combo.append(o[2])
            add_combo.append(o[6])
            add_combo.append(o[7])
            add_combo.append(o[8])
            add_combo.append(p[0])
            add_combo.append(p[1])
            add_combo.append(p[2])
            add_combo.append(p[6])
            add_combo.append(p[7])
            add_combo.append(p[8])
            add_combo.append(p[12])
            add_combo.append(p[13])
            add_combo.append(p[14])
            wr_rb_list.append(add_combo)
            if len(wr_rb_list) > 2000000:
                break
    print("All running backs and wide receivers added")
    print(len(wr_rb_list))
    rb_list.clear()
    wr_list.clear()
    print(rb_list)
    print(wr_list)
    print("Adding rbs and Wide Receivers and tight ends together")
    for h in wr_rb_list:
        if len(wr_te_rb_list) > 10000000:
            break
        for i in te:
            salary = i.get_salary() + h[2] + h[5] + h[8] + h[11] + h[14]
            if salary <= 50000:
                list_new_te_wr = []
                list_new_te_wr.append(h[0])
                list_new_te_wr.append(h[1])
                list_new_te_wr.append(h[2])
                list_new_te_wr.append(h[3])
                list_new_te_wr.append(h[4])
                list_new_te_wr.append(h[5])
                list_new_te_wr.append(h[6])
                list_new_te_wr.append(h[7])
                list_new_te_wr.append(h[8])
                list_new_te_wr.append(h[9])
                list_new_te_wr.append(h[10])
                list_new_te_wr.append(h[11])
                list_new_te_wr.append(h[12])
                list_new_te_wr.append(h[13])
                list_new_te_wr.append(h[14])
                list_new_te_wr.append(i.get_name())
                list_new_te_wr.append(i.get_id())
                list_new_te_wr.append(i.get_salary())
                wr_te_rb_list.append(list_new_te_wr)
                if len(wr_te_rb_list) > 10000000:
                    break

    print(len(wr_te_rb_list))
    wr_rb_list.clear()
    print(wr_rb_list)
    print("Adding wide receivers, running backs, tight ends, and flex together")
    for j in flex:
        if len(wr_te_rb_flx_list) > 10000000:
            break
        for k in wr_te_rb_list:
            salaryJk = j.get_salary() + k[2] + k[5] + k[8] + k[11] + k[14] + k[17]
            if salaryJk <= 50000:
                if j.get_id() != k[1] and j.get_id() != k[4] and j.get_id() != k[7] and j.get_id() != k[10]\
                        and j.get_id() != k[13]  and j.get_id() != k[16]:
                    list_new_flx_def = []

                    list_new_flx_def.append(k[0])
                    list_new_flx_def.append(k[1])
                    list_new_flx_def.append(k[2])
                    list_new_flx_def.append(k[3])
                    list_new_flx_def.append(k[4])
                    list_new_flx_def.append(k[5])
                    list_new_flx_def.append(k[6])
                    list_new_flx_def.append(k[7])
                    list_new_flx_def.append(k[8])
                    list_new_flx_def.append(k[9])
                    list_new_flx_def.append(k[10])
                    list_new_flx_def.append(k[11])
                    list_new_flx_def.append(k[12])
                    list_new_flx_def.append(k[13])
                    list_new_flx_def.append(k[14])
                    list_new_flx_def.append(k[15])
                    list_new_flx_def.append(k[16])
                    list_new_flx_def.append(k[17])
                    list_new_flx_def.append(j.get_name())
                    list_new_flx_def.append(j.get_id())
                    list_new_flx_def.append(j.get_salary())
                    wr_te_rb_flx_list.append(list_new_flx_def)
                    if len(wr_te_rb_flx_list) > 10000000:
                        break

    print("Wide receivers, running backs, tight ends, and flex length is ")
    print(len(wr_te_rb_flx_list))
    wr_te_rb_list.clear()
    print(wr_te_rb_list)
    print("Adding quarterback to the rest of the list")
    for l in qb:
        if len(qb_rb_wr_te_flx_list) > 10000000:
            break
        for m in wr_te_rb_flx_list:
            total_salary = l.get_salary() + m[2] + m[5] + m[8] + m[11] + m[14] + m[17] + m[20]
            if total_salary <= 50000:
                new_arr = []
                new_arr.append(l.get_name())
                new_arr.append(l.get_id())
                new_arr.append(l.get_salary())
                new_arr.append(m[0])
                new_arr.append(m[1])
                new_arr.append(m[2])
                new_arr.append(m[3])
                new_arr.append(m[4])
                new_arr.append(m[5])
                new_arr.append(m[6])
                new_arr.append(m[7])
                new_arr.append(m[8])
                new_arr.append(m[9])
                new_arr.append(m[10])
                new_arr.append(m[11])
                new_arr.append(m[12])
                new_arr.append(m[13])
                new_arr.append(m[14])
                new_arr.append(m[15])
                new_arr.append(m[16])
                new_arr.append(m[17])
                new_arr.append(m[18])
                new_arr.append(m[19])
                new_arr.append(m[20])
                qb_rb_wr_te_flx_list.append(new_arr)
                if len(qb_rb_wr_te_flx_list) > 10000000:
                    break
    print("QB added to list")
    print(len(qb_rb_wr_te_flx_list))
    wr_te_rb_flx_list.clear()
    print(wr_te_rb_flx_list)

    print("Adding defense to the list")
    for q in defense:
        if len(all_teams_list) > 10000000:
            break
        for r in qb_rb_wr_te_flx_list:
            last_salary = q.get_salary() + r[2] + r[5] + r[8] + r[11] + r[14] + r[17] + r[20] + r[23]
            if last_salary < 50000:
                last_new = []
                last_new.append(r[0])
                last_new.append(r[1])
                last_new.append(r[2])
                last_new.append(r[3])
                last_new.append(r[4])
                last_new.append(r[5])
                last_new.append(r[6])
                last_new.append(r[7])
                last_new.append(r[8])
                last_new.append(r[9])
                last_new.append(r[10])
                last_new.append(r[11])
                last_new.append(r[12])
                last_new.append(r[13])
                last_new.append(r[14])
                last_new.append(r[15])
                last_new.append(r[16])
                last_new.append(r[17])
                last_new.append(r[18])
                last_new.append(r[19])
                last_new.append(r[20])
                last_new.append(r[21])
                last_new.append(r[22])
                last_new.append(r[23])
                last_new.append(q.get_name())
                last_new.append(q.get_id())
                last_new.append(q.get_salary())
                all_teams_list.append(last_new)
                all_teams_dict['qb_name'].append(last_new[0])
                all_teams_dict['qb_id'].append(last_new[1])
                all_teams_dict['qb_salary'].append(last_new[2])
                all_teams_dict['rb1_name'].append(last_new[3])
                all_teams_dict['rb1_id'].append(last_new[4])
                all_teams_dict['rb1_salary'].append(last_new[5])
                all_teams_dict['rb2_name'].append(last_new[6])
                all_teams_dict['rb2_id'].append(last_new[7])
                all_teams_dict['rb2_salary'].append(last_new[8])
                all_teams_dict['wr1_name'].append(last_new[9])
                all_teams_dict['wr1_id'].append(last_new[10])
                all_teams_dict['wr1_salary'].append(last_new[11])
                all_teams_dict['wr2_name'].append(last_new[12])
                all_teams_dict['wr2_id'].append(last_new[13])
                all_teams_dict['wr2_salary'].append(last_new[14])
                all_teams_dict['wr3_name'].append(last_new[15])
                all_teams_dict['wr3_id'].append(last_new[16])
                all_teams_dict['wr3_salary'].append(last_new[17])
                all_teams_dict['te_name'].append(last_new[18])
                all_teams_dict['te_id'].append(last_new[19])
                all_teams_dict['te_salary'].append(last_new[20])
                all_teams_dict['flex_name'].append(last_new[21])
                all_teams_dict['flex_id'].append(last_new[22])
                all_teams_dict['flex_salary'].append(last_new[23])
                all_teams_dict['defense_name'].append(q.get_name())
                all_teams_dict['defense_id'].append(q.get_id())
                all_teams_dict['defense_salary'].append(q.get_salary())
                if len(all_teams_list) > 10000000:
                    break
    print("All players added")
    print(len(all_teams_list))
    qb_rb_wr_te_flx_list.clear()
    print(qb_rb_wr_te_flx_list)
    ef = pd.DataFrame(all_teams_dict)
    print("Adding to csv")
    ef.to_csv(
    "C:\\Users\Yarnell\\Desktop\\test1.csv",encoding='utf=8', index=False)
    print("All teams added to csv!")

    print("Connecting to the database")
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=BEUDYFUL\\SQLEXPRESS;DATABASE=FantasyFootball;Trusted_Connection=yes;')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS dbo.AllGameTeams')

    cursor.execute('''CREATE TABLE [dbo].[AllGameTeams](
	[TeamsId] [int] IDENTITY(1,1) NOT NULL,
	[Qb_Name] [nvarchar](255) NOT NULL,
	[QbId] [int] NOT NULL,	
	[Qb_Salary] [int] NOT NULL,
	[Rb_Name1] [nvarchar](255) NOT NULL,
	[RbId1] [int] NOT NULL,	
	[Rb_Salary1] [int] NOT NULL,
	[Rb_Name2] [nvarchar](255) NOT NULL,
	[RbId2] [int] NOT NULL,
	[Rb2_Salary] [int] NOT NULL,
	[Wr_Name1] [nvarchar](255) NOT NULL,
	[WrId1] [int] NOT NULL,	
	[Wr_Salary1] [int] NOT NULL,
	[Wr_Name2] [nvarchar](255) NOT NULL,
	[WrId2] [int] NOT NULL,	
	[Wr_Salary2] [int] NOT NULL,
	[Wr_Name3] [nvarchar](255) NOT NULL,
	[WrId3] [int] NOT NULL,	
	[Wr_Salary3] [int] NOT NULL,
	[Te_Name] [nvarchar](255) NOT NULL,
	[TeId] [int] NOT NULL,	
	[Te_Salary] [int] NOT NULL,
	[Flex_Name] [nvarchar](255) NOT NULL,
	[FlexId] [int] NOT NULL,	
	[Flex_Salary] [int] NOT NULL,
	[Defense_Name] [nvarchar](255) NOT NULL,
	[DefenseId] [int] NOT NULL,	
	[Defense_Salary] [int] NOT NULL,)''')

    insert_query = '''INSERT INTO AllGameTeams(Qb_Name, QbId,Qb_Salary,  Rb_Name1, RbId1, Rb_Salary1, Rb_Name2, RbId2,
    Rb2_Salary, Wr_Name1, WrId1, Wr_Salary1, Wr_Name2, WrId2, Wr_Salary2, Wr_Name3, WrId3, Wr_Salary3, Te_Name, TeId, Te_Salary, 
    Flex_Name, FlexId, Flex_Salary, Defense_Name, DefenseId, Defense_Salary) 
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
    for index, row in ef.iterrows():
        values = (
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
            row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24],
            row[25], row[26])

        cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()

    qb_rb_wr_te_flx_list.clear()
    print("All teams added to the database")
    return all_teams_list

# all_teams_dict = {'qb_salary':[], 'qb_id':[], 'rb1_salary':[], 'rb1_id':[], 'rb2_salary':[], 'rb2_id':[],
#                       'wr1_salary':[], 'wr1_id':[], 'wr2_salary':[], 'wr2_id':[], 'wr3_salary':[], 'wr3_id':[],
#                       'te_salary':[], 'te_id':[], 'flex_salary':[], 'flex_id':[], 'defense_salary':[], 'defense_id':[]}