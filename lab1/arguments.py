import sys

if len(sys.argv) > 1:
    count = 0
    result = ""
    for arg in sys.argv[1:]:
        if len(arg) >= 3:
            count += 1
            result += arg+" "

    print(count)
    print(result)
else:
    print("Brak argumentów")