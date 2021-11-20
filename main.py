# Rock, Paper, Scissors game with Python
import random
import sys


def game_loop(game_ongoing=True, npc=0, player=0):
    while game_ongoing:
        player_choice = input('Please select [1] Rock, [2] Scissors, and [3] Paper \n>')

        if player_choice == '1':
            print('Player selects ROCK')
        elif player_choice == '2':
            print('Player selects SCISSORS')
        else:
            print('Player selects PAPER')

        computer_choice = random.randint(1, 3)

        if computer_choice == 1:
            print('NPC selects ROCK')
        elif computer_choice == 2:
            print('NPC selects SCISSORS')
        else:
            print('NPC selects PAPER')

        if computer_choice == 1 and player_choice == '2':
            npc += 1
        elif computer_choice == 2 and player_choice == '3':
            npc += 1
        elif computer_choice == 3 and player_choice == '1':
            player += 1
        elif computer_choice == 1 and player_choice == '3':
            npc += 1
        elif computer_choice == 2 and player_choice == '1':
            player += 1
        elif computer_choice == 3 and player_choice == '2':
            player += 1
        else:
            print('Game is a tie')

        print('Player score {} NPC score {}'.format(player, npc))
        if npc >= 3 and npc > player:
            print('NPC is the winner! You suck!')
            sys.exit()
        elif player >= 3 and player > npc:
            print('Hey you finally won!')
            sys.exit()


game_loop(True, 0, 0)
