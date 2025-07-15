players_chips = [] #ilość żetonów każdego gracza


def start(h, n): #ustawianie ilości żetonów na start dla każdego gracza
    result = []
    for i in range(n):
        result.append(h)

    return result


def get_from_all(h): #wzięcie od każdego gracza takiej samej ilości żetonów
    result = 0
    for i in range(len(players_chips)):
        if players_chips[i] >= h: # sprawdzenie, czy gracz ma wystarczającą ilość żetonów
            players_chips[i] -= h
            result += h
        else:
            result += players_chips[i]
            players_chips[i] = 0

    return result