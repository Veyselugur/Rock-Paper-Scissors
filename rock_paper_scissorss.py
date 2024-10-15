import random,time

cpoint=[]
upoint=[]
print("The player who wins 5 times wins the game.")

def point():

    if len(cpoint)==5:
        print("*** Computer Won ***")
        print("Score: ",len(cpoint),"-",len(upoint))
        return quit()

    elif len(upoint)==5:
        print("*** User Worn ***")
        print("Score: ",len(cpoint)-len(upoint))

    else: return game()

    return quit()

def quit():

    ex=input("Do you want to continue the game Yes:y or No:n: ")

    if ex=="y":
        return game()

    elif ex=="n":
        print("quitting the game...")
        time.sleep(0.5)
        print("***")
        time.sleep(0.5)
        print("**")
        time.sleep(0.5)
        print("*")
        exit()

    else:
        print ("!!!Please enter a valid value!!!")
        return quit()

def game():

        while True:
            a = ["r", "p", "s"]
            compc = (random.choice(a))
            userc = input( " Rock     : 'R'\n "
                          "Paper    : 'P'\n "
                          "Scissors : 'S'.\n"
                          "Press 'E' to exit the game\n"
                          "Please choose one. : ").lower()
            if userc == "r" or userc=="p" or userc=="s":
                break

            elif userc=="e":
                quit()

            else:
                print("!!!Please enter a valid value!!!\n")
                return game()

        print("--------------------------")
        print("--------------------------")

        print("Your choice: ", userc,"\n")
        print("Choice of the computer: ", compc,"\n")

        if (userc == compc):

            print("**** Draw ****")
            print("--------------------------")
            print("--------------------------")


        elif (userc == "r" and compc == "s"):
            upoint.append(1)
            print("**** You win ****")
            print("--------------------------")
            print("--------------------------")


        elif (userc == "p" and compc == "r"):
            upoint.append(1)
            print("**** You win ****")
            print("--------------------------")
            print("--------------------------")


        elif (userc == "s" and compc == "p"):
            upoint.append(1)
            print("**** You win ****")
            print("--------------------------")
            print("--------------------------")


        else:
            print("**** You lose ****")
            print("--------------------------")
            print("--------------------------")

            cpoint.append(1)
        return point()
game()



