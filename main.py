#Q1
print("Enter the number of friends joining (including you):")
try:
    n = int(input().strip())
except ValueError:
    print("\nNo one is joining for the party")
else:
    if n <= 0:
        print("\nNo one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        friends = {}
        for _ in range(n):
            name = input().strip()
            friends[name] = 0
        print()
        print(friends)

#Q2
print("Enter the number of friends joining (including you):")
try:
    n = int(input().strip())
except ValueError:
    print("\nNo one is joining for the party")
else:
    if n <= 0:
        print("\nNo one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        friends = {}
        for _ in range(n):
            name = input().strip()
            friends[name] = 0

        print("\nEnter the total bill value:")
        total_bill = float(input().strip())

        share = round(total_bill / n, 2)
        for k in friends:
            friends[k] = share

        print()
        print(friends)
#Q3
import random

print("Enter the number of friends joining (including you):")
try:
    n = int(input().strip())
except ValueError:
    print("\nNo one is joining for the party")
else:
    if n <= 0:
        print("\nNo one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        friends = {}
        for _ in range(n):
            name = input().strip()
            friends[name] = 0

        print("\nEnter the total bill value:")
        total_bill = float(input().strip())

        print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input().strip()

        if answer == "Yes":
            lucky = random.choice(list(friends.keys()))
            print(f"\n{lucky} is the lucky one!")
            payers = n - 1
            share = 0 if payers == 0 else round(total_bill / payers, 2)
            for k in friends:
                friends[k] = 0 if k == lucky else share
        else:
            print("\nNo one is going to be lucky")
            share = round(total_bill / n, 2)
            for k in friends:
                friends[k] = share

        print()
        print(friends)

#Q4
import random

print("Enter the number of friends joining (including you):")
try:
    n = int(input().strip())
except ValueError:
    print("\nNo one is joining for the party")
else:
    if n <= 0:
        print("\nNo one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        friends = {}
        for _ in range(n):
            name = input().strip()
            friends[name] = 0

        print("\nEnter the total bill value:")
        total_bill = float(input().strip())

        print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
        answer = input().strip()

        if answer == "Yes":
            lucky = random.choice(list(friends.keys()))
            print(f"\n{lucky} is the lucky one!")
            payers = n - 1
            share = 0 if payers == 0 else round(total_bill / payers, 2)
            for k in friends:
                friends[k] = 0 if k == lucky else share
        else:
            print("\nNo one is going to be lucky")
            share = round(total_bill / n, 2)
            for k in friends:
                friends[k] = share

        print()
        print(friends)