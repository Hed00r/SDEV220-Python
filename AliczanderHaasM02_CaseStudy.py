# Name: Aliczander Haas
# AlicanderHaasM02_CaseStudy
# Takes first and last name inputs, and GPA inputs then tells you whether they have made the Deans List/Honor Roll

lastName = input('Please input a students last name:')
while lastName != 'ZZZ':
    firstName = input('Please input a students first name: ')
    gpa = float(input('Please input ' + firstName + "'s GPA: "))
    if gpa >= 3.5:
        print(firstName + ' ' + lastName + " Has made the Dean's List!")
    elif gpa > 3.25 and gpa <= 3.49:
        print(firstName + ' ' + lastName + " has made the Honor Roll!")
    else:
        print(firstName + '' + lastName + " has not made the Dean's List or Honor Roll :(")
    lastName = input('Please input a students last name:')