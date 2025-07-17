import poker

w = 50
z = '*'
title = "POKER"

def make_line(s, l):
    print(s * l)


def start(): # wyświetla tekst na samym początku
    make_line(z,w)
    print(z, ' ' * (w-4), z)
    print(z, title.center(w-4),  z)
    print(z, ' ' * (w-4), z)
    make_line(z,w)


def new_lines(h): #tworzy nowe linie
    for i in range(h):
        print()


def clear(): # "Czyści" konsolę
    print("\n" * 100)


def header(text): #wypisuje tekst ze znakami po bokach
    print(z, text.center(w - 2), z)


def show_player_bilans(i,bank): # wyświetla bilans żetonów danego gracza
    print("Gracz nr", i + 1, ", ilość żetonów:", bank[i])


def show_player_hand(i, game_deal, bank): # wyświetla wszystkie informacje o danym graczu: jakie ma karty, ile ma żetonów i jaką siłę ma jego dłoń
    show_player_bilans(i,bank)
    print(poker.cards_to_string(game_deal[i]))
    print("Siła ręki gracza:", poker.hand_rank(game_deal[i]), "\n")



def check_fold_win (n, prize_pool): #Sprawdzenie, jeśli został tylko 1 gracz to właśnie on wygrywa
    if len(poker.folded_players) == n-1:
        for i in range(n):
            if i not in poker.folded_players:
                new_lines(3)
                header("GRACZ "+str(i+1)+" WYGRAŁ!!!")
                header(str(prize_pool)+" ŻETONÓW")
                exit(0) #koniec gry

