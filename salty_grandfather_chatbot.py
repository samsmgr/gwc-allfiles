#salty grandfather chatbot
compassion = 5
salty = 5
lawful = 0
qualitiesg = ["Pitiless", "Merciless", "Cold-hearted", "Severe", "Uncharitable", "Of a moderate temperament", "Somewhat Sympathetic", "Kindly", "Humane", "Benevolent", "Compassionate"]
qualitiess = []
qualitiesl = ["on the right side of the law", "in a spot of trouble", "wanted by the police"]

def printsg(input):
    print("SALTY GRANDFATHER: " + input)

def play_tutorial():
    print("You are a grandchild of uncertain inclinations. Over the course of this narrative, you will choose between mercy and a sordid story of revenge, manslaughter and premediated murder, and your heart and your sense of good business.")
    print("Keep an eye on your Qualities: they will be important as you progress. Type 'Qualities' at any time to see your current status.")
    print("Your Characteristical Quality is determined by how you treat those around you, namely your Salty Grandfather and the other members of your family. It is a reflection of the course you choose to take in this narrative.")
    print("Your Legalistic Quality is a measurement of how much you've done to get on the bad side of the law, by doing things like crimes. You will want to keep an eye on this quality -- if it gets too high, the police may begin to pusue you.")

def process_input(input):
    global water_init
    global answer
    if water_init == True:
        if "yes" in answer.lower():
            printsg("Thank you, child.")
            compassion += 10
            salty -= 5
            print("tbc")
            water_init = True
        if "no" in answer.lower():
            print("tbc")
            water_init = True
    if "qualities" in answer.lower():
        print("You are " + qualitiesg[compassion].lower() + " and " + qualitiesl[lawful] + ".")

# --- Put your main program below! ---
def main():
    global username
    global water_init
    global answer
    user = input("Please input your Shrek name: ")
    username = user.upper()
    print("Would you like to play the tutorial?")
    tutorial = input()
    if "yes" in tutorial.lower():
        play_tutorial()
    printsg("Hey there, whippersnapper. It's me, your gramps. You have any water?")
    water_init = True
    while True:
        answer = input(username + " SHREK: ")
        process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
