# Aliczander Haas
# AliczanderHaas_ProgrammingAssignment02
# Assigns variable small and green to true/false, then tells you what fruit/vegetable they are

small = str(input('Is the fruit/vegetable small? yes/no '))
if small == 'yes':
    small = True
else:
    small = False

green = str(input('Is the fruit/vegetable green? yes/no '))
if green == 'yes':
    green = True
else:
    green = False

if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")
