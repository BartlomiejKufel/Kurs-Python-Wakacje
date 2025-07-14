import sys

if len(sys.argv) > 1:
    print("Argumenty:")
    for item in sys.argv[1:]:
        print(item, type(item))
else:
    print("Brak argumentów")