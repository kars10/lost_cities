#!bin/python

import random
import sys
import operator
from lost_cities import *

# initialize board (use a dictionary)
board = game_board()
# initialize other variables
game_over = False

print "Welcome to Aaron Adcock's simulation of the Lost Cities game"
print "You will be player A"

computer_play_strat = "simple"
computer_draw_strat = "simple"
print "Computer Play Strategy: \"{}\"".format(computer_play_strat)
print "Computer Draw Strategy: \"{}\"".format(computer_draw_strat)


# Begin playing the game
# TODO: Add a strategy analysis portion
while not game_over:
    # Print appropriate info
    print ""
    print board
    
    print "Player A's hand:"
    print board.hand_a

    print "Number of cards in deck: " + str(len(board.deck))
    # Player A's turn, most of this code is just to make sure that the card is valid
    print "Play a card (type discard to discard and type exit to leave)"    
    card_string = raw_input()
    played_card = card('blue', 2)

    if card_string == "exit":
        sys.exit(0)

    discard = False
    if card_string == "discard" or (card_string.split())[0] == 'discard':
        discard = True
        print "Discard a card"
        card_string = raw_input()

    played_card.set_card(card_string)
    while not played_card.is_valid():
        print "Please enter a valid card or discard: "
        card_string = raw_input()
        discard = False
        if card_string == "discard" or (card_string.split())[0] == 'discard':
            discard = True
            print "Discard a card"
            card_string = raw_input()

        if card_string == "exit":
            sys.exit(0)
        played_card.set_card(card_string)

    # Play card
    while not board.play_card(played_card, discard, 'a'):
        print "Play a card (type discard to discard and type exit to leave)"    
        card_string = raw_input()
        played_card = card('blue', 2)

        if card_string == "exit":
            sys.exit(0)

        discard = False
        if card_string == "discard" or (card_string.split())[0] == 'discard':
            discard = True
            print "Discard a card"
            card_string = raw_input()

        played_card.set_card(card_string)
        while not played_card.is_valid():
            print "Please enter a valid card or discard: "
            card_string = raw_input()
            discard = False
            if card_string == "discard" or (card_string.split())[0] == 'discard':
                discard = True
                print "Discard a card"
                card_string = raw_input()

            if card_string == "exit":
                sys.exit(0)
            played_card.set_card(card_string)

    # Draw card
    print "Draw a card (if an invalid color is input, then draw will be from deck):"
    draw_string = raw_input()
    board.draw_card(draw_string, 'a')


    if len(board.deck) == 0:
        game_over = True
    # B's turn
    if not game_over:
        success = computer_turn('b', board, computer_play_strat, computer_draw_strat, False)

    if len(board.deck) == 0:
        game_over = True

print ""
print board


if board.a_score > board.b_score:
    print "Player A wins!"
elif board.a_score < board.b_score:
    print "Player B wins!"
else:
    print "Tie."

print "Game over!"
