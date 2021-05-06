# reference https://www.askpython.com/python/examples/blackjack-game-using-python

import random
import os
import time

class Card:
    def __init__(self, suit, value, cardValue):
        # Suit of the Card like Spades and Clubs
        self.suit = suit

        # Representing Value of the Card like A for Ace, K for King
        self.value = value

        # Score Value for the Card like 10 for King
        self.cardValue = cardValue
    
    def __repr__(self):
        return f"{self.suit} : {self.value}"



def blackjackGame(deck: list):
    playerCards, dealerCards = [], []
    playerScore, dealerScore = 0, 0

    # initial dealing for player and dealer
    while len(playerCards) < 2:
        # Randomly dealing a card
        playerCard = deck.pop()

        playerCards.append(playerCard)
        playerScore += playerCard.cardValue


        # Randomly dealing a card
        dealerCard = deck.pop()

        dealerCards.append(dealerCard)
        dealerScore += dealerCard.cardValue


    # print player cards and score
    print('PLAYER CARDS: ', playerCards)
    print('PLAYER SCORE: ', playerScore)

    # Print dealer cards and score, keeping in mind to hide the second card and score
    print("DEALER CARDS: ", dealerCards[0])
    if len(dealerCards) == 1:
        print("DEALER SCORE = ", dealerScore)
    else:
        print("DEALER SCORE = ", dealerScore - dealerCards[-1].cardValue)
    
    while playerScore < 21:
        choice = input("Enter H or S: ")

        if choice.upper() == 'H':    
            # Randomly dealing a card
            playerCard = deck.pop()

            playerCards.append(playerCard)
            playerScore += playerCard.cardValue
    
            print('PLAYER CARDS: ', playerCards)
            print('PLAYER SCORE: ', playerScore)
        
        if choice.upper() == 'S':
            break
    

    if playerScore == 21:
        print('PLAYER HAS A BLACKJACK')
        quit()
    
    if playerScore > 21:
        print('PLAYER IS BUSTED')
        quit()
    

    # dealer moves
    while dealerScore < 17:

        # Randomly dealing a card
        dealerCard = deck.pop()

        dealerCards.append(dealerCard)
        dealerScore += dealerCard.cardValue


    print("DEALER CARDS: ", dealerCards)
    print("DEALER SCORE = ", dealerScore)

    if dealerScore > 21:
        print('DEALER IS BUSTED. YOU WIN !!')
        quit()
    
    if dealerScore == 21:
        print('DEALER HAS BLACKJACK. PLAYER LOSSES')
        quit()

    if playerScore == dealerScore:
        print('TIE')
    elif playerScore > dealerScore:
        print('PLAYER WINS !!')
    else:
        print('DEALER WINS !!')


if __name__ == '__main__':
    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
    # The suit value 
    suitsValues = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
 
    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    # The card value
    cardValues = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(Card(suitsValues[suit], card, cardValues[card]))
    
    random.shuffle(deck)
    blackjackGame(deck)
       
