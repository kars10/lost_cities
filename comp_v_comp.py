#!bin/python

import random
import sys
import operator
from lost_cities import *

print "Welcome to computer vs computer Lost Cities." 

# pick strategies.  This interface is poor, but it works for now.
print "Please enter a string which represents player a's play strategy: "
a_play_strat = raw_input()

print "Please enter a string which represents player a's draw strategy: "
a_draw_strat = raw_input()

print "Please enter a string which represents player b's play strategy: "
b_play_strat = raw_input()

print "Please enter a string which represents player b's draw strategy: "
b_draw_strat = raw_input()

print "How many games would you like them to play against each other? "
num_games = int(raw_input())


a_first_wins = 0
b_first_wins = 0
a_last_wins = 0
b_last_wins = 0

ties = 0

a_first_avg_score = 0
b_first_avg_score = 0
a_last_avg_score = 0
b_last_avg_score = 0

for x in range(num_games):
    # Do half of the games with A plays first and half with B plays first
    if x < (num_games/2):
        result = play_game('a', a_play_strat, a_draw_strat,'b', b_play_strat, b_draw_strat)
        if result['winner'] == 'A':
            a_first_wins += 1
        elif result['winner'] == 'T':
            ties += 1
        elif result['winner'] == 'B':
            b_last_wins += 1

        a_first_avg_score += int(result['a_score'])
        b_last_avg_score += int(result['b_score'])
    else:
        result = play_game('b', b_play_strat, b_draw_strat, 'a', a_play_strat, a_draw_strat)
        if result['winner'] == 'A':
            a_last_wins += 1
        elif result['winner'] == 'T':
            ties += 1
        elif result['winner'] == 'B':
            b_first_wins += 1

        b_first_avg_score += int(result['b_score'])
        a_last_avg_score += int(result['a_score'])

# Present statistical results
print "Results: Player A won " + str(1.0 * (a_first_wins + a_last_wins) / num_games) + " Player B won " + str(1.0 * (b_first_wins + b_last_wins) / num_games)
print "Ties: " + str(ties)
print "Player A's average score was " + str(1.0 * (a_first_avg_score + a_last_avg_score) / num_games)
print "Player B's average score was " + str(1.0 * (b_first_avg_score + b_last_avg_score) / num_games)
print "When Player A goes first, A wins " + str((2.0 * a_first_wins) / num_games)
print "When Player A goes first, A's average score is " + str((2.0 * a_first_avg_score) / num_games) + " while B's average is " + str((2.0 * b_last_avg_score) / num_games)
print "When Player B goes first, B wins " + str((2.0 * b_first_wins) / num_games)
print "When Player B goes first, B's average score is " + str((2.0 * b_first_avg_score) / num_games) + " while A's average is " + str((2.0 * a_last_avg_score) / num_games)
