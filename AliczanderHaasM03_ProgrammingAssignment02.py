# Aliczander Haas
# AliczanderHaasM03_ProgrammingAssignment02
# 01/02/2024

def good(harry, ron, hermione):
    return {harry, ron, hermione}
good('Harry', 'Ron', 'Hermione')


def get_odds():
    for n in range(10):
        if n % 2:
            yield n
for n in get_odds():
    print(n)