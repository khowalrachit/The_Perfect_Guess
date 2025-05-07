import random
computer = random.randint(0,100)
count = 1


while True:
    guess = int(input("Enter a number : "))

    if(guess == computer):
        print(f"You have guessed the correct number in {count} tries.")
        break
    elif((guess - computer)>0):
        print("You guessed higher, The number is lower than that")
        count +=1
        continue
    elif((guess - computer)<0):
        print("You guessed lower, The number is higher than that")
        count +=1
        continue


