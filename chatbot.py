# --- Define your functions below
def coffee():
    print("That's great! There's many benefits to drinking coffee!")
    answer = input("Do you want to know more about the benefits?")
    if answer == "yes":
        print("Coffee reduces the risk of many diseases like cancer, Alzheimer's, Parkinson's and Type 2 Diabetes!")
        answer = input("Well, that was kind of dark. Do you want to hear a coffee joke to lighten the mood?")
        if answer == "yes":
            answer = input("What do you call sad coffee?")
            if answer == "depresso" or answer == "Depresso":
                print("Haha! You got it! I gotta go now. bye.")
                quit()
            elif answer != "depresso" or answer != "Depresso":
                print("WRONG! THE ANSWER IS DEPRESSO!!!!!!")
                print("Now I am depresso because you got it wrong. I don't want to talk to you anymore...bye.")
                quit()
        elif answer == "no":
            print("Okay, bye!")
            quit()
    elif answer == "no":
        print("Okay! Byeeee!!!")
        quit()
def anticoffee():
    print("I didn't either. I like tea much better.")
    answer = input("Do you like tea?")
    if answer == "yes":
        print("Tea reduces your risk of heart attack, stroke, and cancer.")
        answer = input("Well, that was kind of dark. Do you want to hear a tea joke to lighten the mood?")
        if answer == "yes":
            answer = input("What do you call a dentist who doesn't like tea?")
            if answer == ("Denis") or answer == ("denis"):
                print("CORRECT! Fortunately for me, I'm not a dentist and I do like tea, so now I'm going to go drink some. Bye!")
                quit()
            elif answer != ("Denis") or answer != ("denis"):
                print("WRONG! The answer is Denis! Get it, because Denis is dentist without the two t's.")
                print("Speaking of, I'm late for my dentist's appointment! bye!")
                quit()
        elif answer == "no":
            print("Okay! Bye!")
            quit()
    if answer == "no":
        answer = input("Okay, do you want to talk about coffee instead?")
        if answer == "yes":
            coffee()
        elif answer == "no":
            print("Okay, bye!")
            quit()


# --- Put your main program below! ---
def intro():
    print("Hi! My name is Bob, talk to me!")
    print("Type something and hit enter.")
def chat():
    answer = input("Did you drink coffee this morning?")
    if answer == "yes":
        coffee()
    elif answer == "no":
        anticoffee()

def main():
    intro()
    while True:
        answer = input("How are you today?")
        print("That's cool!")
        chat()



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()