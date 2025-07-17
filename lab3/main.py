from numpy.ma.core import minimum

import poker
import visual
import bank
import time
import random

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
all_in = False

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
players_hands = poker.deal(deck, n)  #rozdanie w tej grze
prize_pool = bank.get_from_all(min_bid) #wzięcie od każdego gracza po minimalnej stawce



while True:
    sel_option = 0  # opcja wybrana przez gracza

    if all_in: # jeśli któryś z graczy wejdzie all in
        break
    if player_index not in poker.folded_players: # jeśli gracz spasował te instrukcje się nie wykonają
        visual.header("Twoja ręka")
        visual.new_lines(1)

        visual.show_player_hand(player_index, players_hands, bank.players_chips)

        visual.header("Póla żetonów: " + str(prize_pool))
        visual.header("Minimalny zakład: " + str(min_bid))

        visual.new_lines(1)


        if bank.players_chips[player_index] < min_bid:
            print("1. All in")
            print("3. Spasuj (fold)")
            while True:
                try:
                    sel_option = int(input("Wybierz opcje 1 lub 3: "))
                    assert 1 == sel_option or sel_option == 3
                    break
                except (ValueError, AssertionError):
                    print("Zła opcja! Wybierz liczbę od 1 lub 3.")

        else:
            print("1. Sprawdź (call)")
            print("2. Podbij (raise)")
            print("3. Spasuj (fold)")
            print("4. Czekaj (check)")
            while True:
                try:
                    sel_option = int(input("Wybierz opcje (od 1 do 4): "))
                    assert 1 <= sel_option <= 4
                    break
                except (ValueError, AssertionError):
                    print("Zła opcja! Wybierz liczbę od 1 do 4.")

        if sel_option == 1: #Sprawdzić
            if min_bid >= bank.players_chips[player_index]:
                visual.header("ALL IN!")
                all_in = True
            visual.header("Gracz "+str(player_index+1)+" sprawdza")
            prize_pool += bank.player_bet(player_index, min_bid)

        elif sel_option == 2: #Podbić
            while True:
                try:
                    bid = int(input("Wybierz stawkę do podbicia(musi być większa lub równa zakładowi minimalnemu): "))
                    assert min_bid <= bid <= bank.players_chips[player_index]
                    if bid == bank.players_chips[player_index]:
                        visual.header("ALL IN!")
                        all_in = True
                    break
                except (ValueError, AssertionError):
                    print("Zła liczba żetonów!")
            visual.header("Gracz "+str(player_index+1)+" podbija stawkę o "+str(bid))
            prize_pool += bank.player_bet(player_index, bid)
            min_bid = bid

        elif sel_option == 3: #Spasować
            poker.player_fold(player_index)
            visual.header("Gracz "+str(player_index+1)+" spasował")

        elif sel_option == 4: #Czekać
            visual.header("Gracz "+str(player_index+1)+" czeka")

        time.sleep(2)
        visual.clear()
        #koniec instrukcji gracza


    # instrukcje botów

    #Dokończ pisanie instrukcji botów
    for i in range(1, n):
        if i not in poker.folded_players:
            visual.check_fold_win(n, prize_pool)  # sprawdzenie, czy w grze został 1 gracz
            bot_option = 4  # ustawianie opcji bota na czekanie
            if sel_option != 4 or sel_option != 3:  # jeśli gracz nie czeka lub pasuje to losowana jest opcja
                bot_option = random.randint(1, 3)  # losowanie wyboru bota

            if bot_option == 1:  # Bot Sprawdza
                visual.header("Gracz " + str(i + 1) + " sprawdza")

            elif bot_option == 2:  # Bot Podbija
                visual.header("Gracz " + str(i + 1) + " podbija stawkę o ?")

            elif bot_option == 3:  # Bot Pasuje
                poker.player_fold(i)
                visual.header("Gracz " + str(i + 1) + " spasował")

            elif bot_option == 4:  # Bot Czeka
                visual.header("Gracz " + str(i + 1) + " czeka")

            time.sleep(1)

    visual.check_fold_win(n,prize_pool) #sprawdzenie, czy w grze został 1 gracz

