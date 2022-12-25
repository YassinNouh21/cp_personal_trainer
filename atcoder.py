import requests
from bs4 import BeautifulSoup
import gspread


# open excel sheet
gs = gspread.service_account(
    filename='I:\\cp\\script\\at_coder\\api_sheet.json')
sh = gs.open("Problem Solving")


avaible_row = 0
check_sheet = input(
    "Enter the sheet name: 0: AtCoder, 1: Codeforces , 2: GDSC")
if check_sheet == '0':
    ws = sh.worksheet("AtCoder")
elif check_sheet == '2':
    ws = sh.worksheet("GDSC")
else:
    ws = sh.worksheet("Codeforces")

for i in range(1, 100):
    if ws.cell(i, 1).value == None:
        # print(i)
        avaible_row = i
        break
# ws.update(row, avaible_row)


def update_row(start_row, data):
    for i in range(len(data)):
        ws.update_cell(start_row, i+1, data[i])


url = input("Enter the link of the problem in AtCoder: ")
result = requests.get(url)


src = result.content

soup = BeautifulSoup(result.text, 'lxml')

# Name of the problem
name_of_problem = soup.find_all('span', class_='h2')[
    0].text.strip().replace('Editorial', '')
name_of_problem.replace(' ', '')
name_of_problem = (" ").join(name_of_problem.split())

contest_name = url.split('/')[-3].upper()

type_problem = name_of_problem[0]

diffuiulty = input("Enter the difficulty of the problem: ")
has_new_idea = input("Enter if the probelm has new idea: ")

# tags for the problems
tags = []
while True:
    tag = input(
        'Enter the tags of the problem / press 0 to break / press 1 to remove the tag : ')
    if tag == '0':
        break
    elif tag == '1':
        if not tags.empty():
            tags.pop()
        continue
    else:
        tags.append(tag)


def defficulty(diffuiulty):
    if diffuiulty == '1':
        return 'Easy'
    elif diffuiulty == '2':
        return 'Medium'
    elif diffuiulty == '3':
        return 'Hard'


def check_new_idea(has_new_idea):
    if has_new_idea == '1':
        return 'Yes'
    else:
        return 'No'


dif = defficulty(diffuiulty)
idea = check_new_idea(has_new_idea)
concatenated_tags = ' - '.join(tags)

data = [contest_name, name_of_problem, url, dif, idea, concatenated_tags]

update_row(avaible_row, data)
