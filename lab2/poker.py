import random

from sympy.strategies.core import switch

ranks_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'D', 'K', 'A']  # rangi
colors_list = ['c', 'd', 'h', 's']  #kolory
n = 3  #ilość graczy


def histogram(input):
    result_dict = {}
    for i in input:
        if i in result_dict:
            result_dict[i] += 1
        else:
            result_dict[i] = 1

    return result_dict


def deck():  #zwraca talię kart, 52 karty
    cards = []
    for rank in ranks_list:
        for color in colors_list:
            cards.append([rank, color])

    return cards


def deal(deck, n):  #rozdanie kart dla n graczy
    result = []
    picked = []

    for i in range(n):
        hand = []
        while len(hand) < 5:
            rand_card = random.randint(0, 51)
            if rand_card not in picked:
                picked.append(rand_card)
                hand.append(deck[rand_card])
        result.append(hand)
    return result


deck = deck()  #talia kart
if n * 5 > len(deck):
    print("Nie ma na tyle kart w tali")
    exit(1)

game_deal = deal(deck, n)  #rozdania w tej grze

def is_rank_sequence(hand): #sprawdzenie, czy w ręce karty są po kolei
    for i in range(2, 11):
        if (i == 2) and ('A' in hand and i in hand and i+1 in hand and i+2 in hand and i+3 in hand):
            return True
        elif (i == 7) and (i in hand and i+1 in hand and i+2 in hand and i+3 in hand and 'J' in hand):
            return True
        elif (i == 8) and (i in hand and i+1 in hand and i+2 in hand and 'J' in hand and 'D' in hand):
            return True
        elif (i == 9) and (i in hand and i+1 in hand and 'J' in hand and 'D' in hand and 'K' in hand):
            return True
        elif (i == 10) and (i in hand and 'J' in hand and 'D' in hand and 'K' in hand and 'A' in hand):
            return True
        elif i in hand and i+1 in hand and i+2 in hand and i+3 in hand and i+4 in hand:
            return True

    return False


def hand_rank(hand): #sprawdzenie wartości kart w ręce gracza
    hand_rank_list = []
    hand_color_list = []
    for card in hand:
        hand_rank_list.append(card[0])
        hand_color_list.append(card[1])

    hand_rank_histogram = histogram(hand_rank_list)
    hand_color_histogram = histogram(hand_color_list)

    is_hand_rank_sequence = is_rank_sequence(hand_rank_list)
    hand_strength = 0

    if (5 in hand_color_histogram.values()) and ('A' in hand_rank_list) and (10 in hand_rank_list) and is_hand_rank_sequence:
        hand_strength = 10 #poker królewski
    elif (5 in hand_color_histogram.values()) and is_hand_rank_sequence:
        hand_strength = 9 #poker
    elif 4 in hand_rank_histogram.values():
        hand_strength = 8 #kareta
    elif (3 in hand_rank_histogram.values()) and (2 in hand_rank_histogram.values()):
        hand_strength = 7 #full house
    elif 5 in hand_color_histogram.values():
        hand_strength = 6 #kolor
    elif is_hand_rank_sequence:
        hand_strength = 5 #strit
    elif 3 in hand_rank_histogram.values():
        hand_strength = 4 # trójka
    elif list(hand_rank_histogram.values()).count(2) == 2:
        hand_strength = 3 #dwie pary
    elif 2 in hand_rank_histogram.values():
        hand_strength = 2 #para
    else:
        hand_strength = 1 #wysoka karta

    return hand_strength

for i in range(n):
    print("Gracz nr", i+1)
    print("Siła ręki gracza:", hand_rank(game_deal[i]), "\n")

