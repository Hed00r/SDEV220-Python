# Aliczander Haas
# AliczanderHaasM02_ProgrammingAssignment04
# Makes a secret number and then guesses a number until the guess is the same as the secret number

guess_me = 7
start = 1

while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1