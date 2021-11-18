# Rock, Paper, Scissors game with Python
import random

# variable for the NPC selection. Based on a random Integer between range of 0 - 2.
npc_selection = random.randint(0, 2)
# variable to store the computers score
npc_score = 0
# variable to store the players score
player_score = 0
player_selection = input("Please selection your choice [0] Rock, [1] Paper, and [2] Scissors. \n>")
# variable for collection the players input based on integer selection/assignment.
converted_selection = int(player_selection)


# Function for getting NPC choice.
def npc_turn():
    selection = npc_selection
    if selection == 0:
        return "NPC selects rock"
    elif selection == 1:
        return "NPC selects Paper"
    else:
        return "NPC selects Scissors"


# Victory/scoring of game
def scoring():
    global player_score, npc_score
    if converted_selection == 0 and npc_selection == 1:
        npc_score += 1
    elif converted_selection == 1 and npc_selection == 2:
        npc_score += 1
    elif converted_selection == 2 and npc_selection == 0:
        npc_score += 1
    elif converted_selection == 0 and npc_selection == 2:
        player_score += 1
    elif converted_selection == 1 and npc_selection == 0:
        player_score += 1
    elif converted_selection == 2 and npc_selection == 1:
        player_score += 1
    else:
        return "Match is a tie"


def round_one():
    npc_turn()
    print(npc_turn())
    scoring()
    print("Players score is ", player_score)
    print("NPC score is ", npc_score)


round_one()
# Testing NPC_selection is working correctly and is the proper range.
# print(npc_selection)
