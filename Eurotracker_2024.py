
#This program will track the standings of Euro 2024

#Milestone 1: Create function to collect user input and calculate points in the matches, storing the points in a list
results = []
def calculate_points(results):
    
    while True: #Asks for user input until user presses 'enter' 
        hometeam = input("Home team: ")
        if hometeam == "": #Quits loop if user presses 'enter'
            break
        awayteam = input("Away team: ")
        goals_hometeam = int(input("How many goals did the home team score? "))
        goals_awayteam = int(input("How many goals did the away team score? "))
        if goals_hometeam > goals_awayteam:
            results.append(hometeam)
            results.append(hometeam)
            results.append(hometeam)
            
        elif goals_hometeam < goals_awayteam:
            results.append(awayteam)
            results.append(awayteam)
            results.append(awayteam)
            
        else:
            results.append(hometeam)
            results.append(awayteam)
            
    return(results)

print("Track the standings in group A of Euro 2024 based on the results of the matches.\nPlease state home and away teams of the matches capitalized. Press Enter to stop.")

import os
file_path = "result1.txt"

file_contents = []
if os.path.exists(file_path):
    file = open(file_path, "r")
    while True:
        content = file.readline().strip()
        if content == "":
            break
        file_contents.append(content)
        #print(file_contents)

    #print("File exists")
    
    #print(file_contents)
    file.close()

else:
    print("File does not exist")
    

group_results_m1 = calculate_points(file_contents) #Calculates standings in group based on user input regarding matchday 1

file = open("result1.txt", "w")

for team in (group_results_m1):
    file.write(team+"\n")
    
file.close()
    
#print(group_results_m1)

#Milestone 2: Create dictionary with keys and counts for printing standings

standings = {} #Initializing en empty dictionary

result_list = group_results_m1 #Initializing list for building dictionary

for team in range(len(result_list)): #Iterate over list
    team = result_list[team]  #define the key element (team)
    if team not in standings: #add team as key to the standings dictionary if not already present, and give it the count of '1'
        standings[team] = 1
    else:
        standings[team] += 1 #if team is already present as key, increment the count by 1

#print (standings)  #print the standings dictionary

#Milestone 3: Add teams with 0 points to the standings dictionary

group_a_teams = ['Germany', 'Scotland', 'Hungary', 'Switzerland'] #Define list of group teams

for team in group_a_teams: #Iterate over keys of group teams dict
    if team not in standings: # add team as key to the standings dictionary if not already present with the count of 0
        standings[team] = 0

#print(standings) #Prints the updated standings dict

#Milestone 4: create function that prints histogram bar from dictionary

def print_histogr_bar(word, count): #Prints one histogram bar, where one key kan take up to 14 spaces, and wher 'x' string is multiplied with count.
    print(f"{word : <14}: {'x' * count}")

#Milestone 5: Loop over dictionary to print histogram bars based on results from matchdays

for key in standings:
        value = standings[key]
        print_histogr_bar(str(key), (value))
