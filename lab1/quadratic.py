import math
import sys

if len(sys.argv) > 3:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    delta = (b * b) - 4 * a * c

    if delta > 0:
        print(2)
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(x1, x2)
    elif delta == 0:
        print(1)
        x0 = -b / (2 * a)
        print(x0)
    else:
        print(0)

else:
    print("Brak wystarczającej liczby argumentów")