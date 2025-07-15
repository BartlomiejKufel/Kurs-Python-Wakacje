from numpy.ma.core import minimum

import poker
import visual
import bank

# sprawdzenie zadania 3
# hands = [[(10, 'h'), ('J', 'h'), ('D', 'h'), ('K', 'h'), ('A', 'h')], # Przykład: poker królewski        : 10
#          [('A', 'c'), ('A', 's'), ('A', 'h'), ('A', 'd'), (8, 's')],  # Przykład: kareta                 : 8
#          [(5, 'c'), (6, 'd'), (7, 'h'), (8, 's'), (9, 'd')],  # Przykład: strit                  : 5
#          [('A', 's'), (2, 'h'), (3, 'd'), (4, 'c'), (5, 's')],  # Przykład: też strit, (As jako 1) : 5
#          [(2, 'c'), (2, 'd'), (5, 'h'), (9, 's'), ('K', 'd')]   # Przykład: jedna para             : 2
#          ]
#
# for i in range(len(hands)):
#     print("Gracz nr", i+1)
#     print(poker.cards_to_string(hands[i]))
#     print("Siła ręki gracza:", poker.hand_rank(hands[i]), "\n")



n = 0  #ilość graczy
deck = poker.deck()  #talia kart
min_bid = 50 #minimalna stawka
prize_pool = 0 #pula do wygrania
player_index = 0 #index gracza


visual.start()
visual.new_lines(1)

while True:
    try:
        n = int(input("Podaj liczbę graczy (od 2 do 6): "))
        assert 2 <= n <= 6
        break
    except (ValueError, AssertionError):
        print("Zła liczba graczy! Wybierz ilość graczy od 2 do 6.")

visual.clear()


bank.players_chips = bank.start(1000, n) # rozdanie żetonów każdemu z graczy


visual.header("Twoja ręka")
visual.new_lines(1)

visual.show_player_bilans(player_index, bank.players_chips)
visual.new_lines(1)

visual.header("Póla żetonów: "+ str(prize_pool))
visual.header("Minimalny zakład: "+ str(min_bid))

visual.new_lines(1)
visual.make_line(visual.z, visual.w+2)
visual.new_lines(1)

#rozdanie kart i dorzucenie wstępnej ilości żetonów
game_deal = poker.deal(deck, n)  #rozdanie w tej grze
prize_pool = bank.get_from_all(min_bid) #wzięcie od każdego gracza po minimalnej stawce


visual.header("Twoja ręka")
visual.new_lines(1)

visual.show_player_hand(player_index, game_deal, bank.players_chips)

visual.header("Póla żetonów: "+ str(prize_pool))
visual.header("Minimalny zakład: "+ str(min_bid))

#pisz tu dalej czyli wybory gracza i botów

