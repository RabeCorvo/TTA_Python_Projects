#
# Python:   3.8.5
#
# Author:   Sam Breidenbach
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember, function_name(variable) _means that we pass in the variable.
#           return variable _means that we are returning the variable
#           back to the calling function.



def start(nice=0,mean=0,name=""):
   # get user's name
   name = describe_game(name)
   nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have the user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nYou chose to tempt fate again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be presented \nwith a nice fluffy kitten. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nYou stand in a large space. In front of you a single light shines \nfrom above while impenetrable darkness surrounds in all other directions.\nA stranger appears out of the inky black, silently pulling a cute \ncuddly kitten from his monk like robes and places it gently in front \nof you directly beneath the shining light. The kitten sits quietly, \nwaiting for whatever happens next. \nWill you be nice or mean? (N/M) \n>>>").lower()
        if pick == "n":
            print("\nYou look down at this kitten, so young, so precious, and something \ninside you melts.  You drop to your stomach and begin \nplaying with the kitten joyfully.  Eventually the stranger ")
            print("appears again and without a word scoops the kitten from \nthe ground and disappears from whence he came.")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nYou look down at this kitten and you feel the tingle of rage building. \nIts sin is being naive; being pure. You think to yourself that this \nis not how the world intended any creature to exist, and it  ")
            print("is up to you to teach it so. With great purpose, you draw back your leg \nand swiftly deliver a punt of clarification.  The kitten, caught \nby surprise, flies off into the black. You hope that the kitten ")
            print("has learned something this day.  \nLearned that the world is cruel and uncaring.  \nLearned that purity does not equal salvation.")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2:    # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2:    # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:           # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    # Substitues the {} wildcards with our variable values
    print("\nFinally you hear a voice call out, 'It is done, {}. \nThe kittens have been pleased and your place in their kingdom \nhas been established.  Your moral slate has been cleared of any choices ".format(name))
    print("you made in the past and forever will you be known as Cat Friend!' \nThis is weird, but you go along with it and enter a pardisal \nkingdom of infinite fluff and cuddles.")
    # call again function and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("\nYou feel a rumble emanating from the darkness around you. \nFinally a voice reverberates from the void, 'Your spirit is \nclear to all; it is as black as this gloom surrounding you. \nYour actions have decided your fate, {}. Your punishment will be just.'".format(name))
    print("The rumbling intensifies and, now terrified, you call out that \nyou were simply showing the cats the truth of the world, but to \nno response.  Suddenly a giant paw swings from in front of you ")
    print("and you find yourself flying back into the cold darkness. \nAs you soar endlessly in the abyss you think that perhaps it was \nyourself that needed a righteous punt of clarification, and fittingly, \nyou have received one.")
    # call again function and pass in our variables
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSo be it. The kittens will be waiting...always waiting...")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO': \n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice, I do not reset the name variable as that same user elected to play again
    start(nice,mean,name)


if __name__ == "__main__":
    start()
