from random import randint

planets = ["Mercury", "Venus", "Earth",
           "Mars", "Jupiter", "Saturn",
           "Uranus", "Neptune"]

def task1():
    idx = randint(0, 7)
    planet = planets[idx]
    idx += 1
    print('What is the position of', planet, 'relative to the Sun?')
    pos = int(input())
    correct = pos == idx
    if correct:
        print('That is correct.')
    else:
        print('That is not correct.')
    print(planet, 'is planet number', idx, 'from the Sun.')
    return correct

def task2():
    idx = randint(0, 7)
    planet = planets[idx]
    idx += 1
    print('What is the name of planet number', idx, 'from the Sun?')
    name = input()
    correct = name == planet
    if correct:
        print('That is correct.')
    else:
        print('That is not correct.')
    print(planet, 'is planet number', idx, 'from the Sun.')
    return correct


def task3():
    idx = randint(0, 6)
    planet = planets[idx]
    print('The name of the planet that comes after', planet, 'is...')
    name = input()
    next_planet = planets[idx + 1]
    correct = name == next_planet
    if correct:
        print('That is correct.')
    else:
        print('That is not correct.')
    print(next_planet, 'comes after', planet)
    return correct


# Task 4
def quiz():
    count = 0
    if task1():
        count += 1
    if task2():
        count += 1
    if task3():
        count += 1
    print('You got', count, 'out of 3 answers right.')

# Explorer task
def guess():
    idx = randint(0, 7)
    planet = planets[idx]
    correct = False
    hinted_pos = False
    hinted_neighbor = False
    while not correct:
        name = input('Guess the planet: ')
        if name == '':
            # continue means ignore (not run) the remain code bellow
            # and loop again (go to `while not correct:`)
            # It similar to 'break' (ignore remain code) but loop again
            continue
        if planet[0] != name[0]:
            print('The first letter is', planet[0])
            continue
        correct = name == planet
        if correct:
            print("You've got it!:")
        else:
            if not hinted_pos:
                print('It is planet number', idx + 1, 'from the Sun.')
                hinted_pos = True
            elif not hinted_neighbor:
                if idx > 0:
                    print('It comes after', planets[idx - 1])
                else:
                    print('It comes before', planets[1])
                hinted_neighbor = True
                continue
            else:
                print('Try again')
        

quiz()
guess()
