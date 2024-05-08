name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on dirt road, It has come to and end. You can go left or right. Which way you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk or swim. type \"walk\" to walk around or \"swim\" to swim accross: ").lower()

    if answer == "swim":
        print("You swam accross and were eaten by alligator.")
    elif answer == "walk":
        print("You walk for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly. Do you want to cross or head back (cross/back)? ").lower()

    if answer == "back":
        print("You go back and lose!")
    elif answer == "cross":
        answer = input("You cross the bridgeand meet a stranger, Do you want to talk them (yes/no)? ").lower()

        if answer == "yes":
            print("You talk to the stanger. He gave the gold to you. You win! :)")
        elif answer == "no":
            print("You ignore the stanger. He make you a Donkey. You lose! :(")
        else:
            print("Not a valid option. You lose!")
    else:
        print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose!")