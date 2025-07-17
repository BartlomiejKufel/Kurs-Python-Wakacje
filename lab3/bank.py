players_chips = [] #ilość żetonów każdego gracza


def start(h, n): #ustawianie ilości żetonów na start dla każdego gracza
    result = []
    for i in range(n):
        result.append(h)

    return result

def player_bet(player_index, h): #funkcja do brania od gracza żetonów
    result = 0
    if players_chips[player_index] >= h: # sprawdzenie, czy gracz ma wystarczającą ilość żetonów
        players_chips[player_index] -= h
        result += h
    else:
        result = players_chips[player_index]
        players_chips[player_index] = 0

    return result

def get_from_all(h): #wzięcie od każdego gracza takiej samej ilości żetonów
    result = 0
    for i in range(len(players_chips)):
        result += player_bet(i, h)

    return result

