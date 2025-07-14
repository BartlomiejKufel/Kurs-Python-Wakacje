import sys

if len(sys.argv) > 3:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    else:
        print("Ten operator nie jest dostępny")

else:
    print("Brak wystarczającej liczby argumentów")