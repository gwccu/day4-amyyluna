# file name: problemSetDay4.py
strength = 5
while strength <= 10:
    print(strength)
    strength += 1
    if strength < 10:
        print('Your strength level is low :(')
    elif strength == 10:
        print('Great Job! Your strength level is at it maximum level :)')