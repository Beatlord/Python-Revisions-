x = None
y = None
while True:
    try:
        lvl = input('Enter the level of your fuel in form of x/y: ')
        level = lvl.split("/")
        x = float(level[0])
        y = (float(level[1]))
        if x <= y:
            try:
                frac = (x / y) * 100
            except ZeroDivisionError:
                print('Try again, the number cant ve zero')
            else:
                if frac <= 1:
                    print('E: Your battery is empty.')
                    break
                elif frac >= 99:
                    print('F: Your battery is full.')
                    break
                else:
                    print(f'Your battery is {frac}% full')
                    break
        else:
            print('Invalid input, x should be less than y')
    except ValueError:
        print('Invalid input')
