letter = '''Dear < |NAME| > ❤, 
            You are selected🎉🍾
            Greatings from XYZ SOFTWARE SERVICES

            HAVE A GREAT DAY, < |NAME| >
            Date: < |DATE| >
'''


name = input("Enter your name:\n ")
date = input("Enter date:\n ")


letter = letter.replace("< |NAME| >" , name)
letter = letter.replace("< |DATE| >" , date)

print(letter)