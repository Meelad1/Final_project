## Meelad Doroodchi, Final Project 
## Need all of these imports not only for the visualization but to convert the csv to a dataframe to be able to use the
## data in code. 

import csv
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Implementing a Binary Search Tree to print out the top 5 teams with most total goals scored(goals for and goals
# against combined)
class BST:
    def __init__(self, team, data):
        self.left = None
        self.right = None
        self.team = team
        self.data = data

def insert(root, team, data):

    if root == None:
        return BST(team, data)
    elif root.data == data:
        return root
    elif root.data > data:
        root.left = insert(root.left, team, data)
    else:
        root.right = insert(root.right, team,  data)
    return root

#inorder printing
lst = []
def inorder_list(root):
    if root != None:
        inorder_list(root.left)
        lst.append((root.team, root.data)) 
        inorder_list(root.right)
    return lst


if __name__ == "__main__":

    file = open('FIFA - 2014.csv')
    csv_2014 = csv.reader(file)
    header = next(csv_2014)
    list_2014 = []

    for row in csv_2014:
        total = row[6] + row[7]
        dic = { 
            'team' : row[1],
            'goal_for' : row[6], 
            'goal_against': row[7], 
            'total' : abs(int(row[6]) + int(row[7]))
        }
        list_2014.append(dic)

## opens the 2018.csv file and reads it to a dataframe with the csv.reader
    file = open('FIFA - 2018.csv')
    csv_2018 = csv.reader(file)
    header = next(csv_2018)
    list_2018 = []


    for row in csv_2018:
        total = row[6] + row[7]
        dic = { 
            'team' : row[1],
            'goal_for' : row[6], 
            'goal_against': row[7], 
            'total' : abs(int(row[6]) + int(row[7]))
        }
        list_2018.append(dic)

    
    root = BST(list_2014[0]['team'], list_2014[0]['total'])
    for i in range(1, len(list_2014)):
        insert(root, list_2014[i]['team'], list_2014[i]['total'])
    print('Top 5 Teams based on Total Goals in 2014')
    top_5_2014 = inorder_list(root)[-1:-6:-1]

    root = BST(list_2018[0]['team'], list_2018[0]['total'])
    for i in range(1, len(list_2018)):
        insert(root, list_2018[i]['team'], list_2018[i]['total'])
    top_5_2018 = inorder_list(root)[-1:-6:-1]


### Visualization putting the data in a Dataframe and then visualizing it using seaborn and a barplot to show
## the top 5 teams in each world cup based on total goals(goals for and goals against combined)
    df = pd.DataFrame(top_5_2014, columns=["team", "total"])
    print(df)
    sns.barplot (x = 'team', y = 'total', data=df )
    plt.title("Top 5 Teams in the 2014 World Cup based on Total Goals") 
    plt.show()


    df = pd.DataFrame(top_5_2018, columns=["team", "total"])
    print(df)
    sns.barplot (x = 'team', y = 'total', data=df )
    plt.title("Top 5 Teams in the 2018 World Cup based on Total Goals") 
    plt.show()