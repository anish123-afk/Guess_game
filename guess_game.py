import random as r

num = r.randint(1,100)
with open("game.txt", "w") as f:
    f.write(str(num))

print ("I have choosen one number between [1, 100], ")
print("Now its your turn to guess it!!!")

n = int(input("GUESS A NUMBER : "))
i = 1
while(n != num):
    if(n > num):
        print("Lower number please")
    else:
        print("Higher number please")
    n = int(input("GUESS A NUMBER : "))
    i += 1
    with open("guesses.txt", "w") as f:
        f.write(str(i))

else:
    print("Congrats!!! You are correct !!")
    with open("guesses.txt") as f:
        guess = f.read()
    print(f"You took \"{int(guess)}\" guesses ")