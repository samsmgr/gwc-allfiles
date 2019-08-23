import time
#frog time
#intro
print("You are a hard working business-frog. Every day, you commute from your home in Brooklyn to your job at Goldman Sachs and back again.")
frogname = input("Your name is ")
print("Look! You just received a text. It says...")
print("Hey " + frogname + "... what time will you be home?")
familymessage = input("It's your lovely family! You tell them: ")

#which train
valid_trainline = False
while not valid_trainline:
    print("You are eager to get back to your home Brooklyn, which is just a short walk away from the Atlantic Ave/Barclays Center station. Which trains do you want to take home: the 123, ACE, or RW?")
    trainline = input()

    #path a/c/e
    if trainline == "ACE" or trainline == "ace":
        valid_chamwtc = False
        while not valid_chamwtc:
            print("You decide to take the ACE. First things first, should you go to World Trade Center to catch the E, or head to Chambers St for the A or C?")
            acewhich = input()
            valid_trainline = True

            #path a/c
            if acewhich.lower() == "chambers st" or acewhich.lower() == "ac":
                valid_chamwtc = True
                valid_fare = False
                while not valid_fare:
                    print("You descend into the subway station. Before you are a number of turnstiles. Since you are a well-prepared frog, you have a metrocard with you. And yet... pay the fare or hop the turnstile?")
                    fareevasion = input()

                    #fare evasion
                    if fareevasion == "hop the turnstile" or fareevasion == "hop": #bad end
                        print("Uh oh! The nice friendly-looking woman in nurse's scrubs hanging around the entrance was actually an undercover cop! She writes you a ticket. How can you look your lovely family in the eye, now that you've become a criminal?")
                        print("GAME OVER.")
                        valid_fare = True

                    #fare evasion
                    if fareevasion == "pay the fare" or fareevasion == "pay": #continue
                        valid_fare = True
                        valid_updownac = False
                        while not valid_updownac:
                            print("You make it into the station without any further issues. On one side of the station, it says the trains are going to Downtown & Bklyn. On the other side, it says Uptown & The Bronx. Are you going uptown or downtown?")
                            updownac = input()

                            #up/down ac
                            if updownac.lower() == "uptown": #continue
                                valid_updownac = True
                                valid_west4 = False
                                while not valid_west4:
                                    print("You take the train uptown. After a few stops, you arrive at West 4th. Get off here? Y/N")
                                    west4getoff = input()

                                    #get off at west 4th
                                    if west4getoff.lower() == "y" or west4getoff.lower() == "yes": #continue
                                        valid_west4 = True
                                        valid_updownd = False
                                        while not valid_updownd:
                                            print("As befits the MTA-savvy "+frogname+", you realized that the A/C does not, in fact, go to Atlantic Ave/Barclays Center at all! Your only hope of success was to make it to West 4th and transfer to the D train.")
                                            print("Do you take the D uptown or downtown?")
                                            updownd = input()

                                            #up/down d
                                            if updownd.lower() == "uptown": #bad end
                                                print("Why would you even do that?")
                                                print("GAME OVER.")
                                                valid_updownd = True

                                            #up/down d
                                            if updownd.lower() == "downtown": #continue
                                                valid_updownd = True
                                                valid_dtrainatl = False
                                                while not valid_dtrainatl:
                                                    print("Good work! It's a long ride, but at long last the train pulls into Atlantic Ave/Barclays Center. Get off here? Y/N")
                                                    dtrainatlantic = input()
                                                    if dtrainatlantic.lower() == "no" or dtrainatlantic.lower() == "n": #bad end
                                                        print("Why would you even do that?")
                                                        print("GAME OVER.")
                                                        valid_dtrainatl = True
                                                    if dtrainatlantic.lower() == "y" or dtrainatlantic.lower() == "yes": #good end
                                                        print("You make it home with time to spare! Your lovely family is happy to see you.")
                                                        print("YOU WIN!")
                                                        valid_dtrainatl = True

                                    #get off at west 4th
                                    if west4getoff.lower() == "n" or west4getoff.lower() == "no": #bad end
                                        print("You stay on the train. The stations pass by, becoming more and more unfamiliar. Where are you?")
                                        print("GAME OVER.")
                                        valid_west4 = True

                            #up/down ac
                            if updownac.lower() == "downtown": #bad end
                                valid_updownac = True
                                print("You get on the train. As you wait, the stations fly by. Canal...Fulton...Jay St/Metrotech....the names become more and more unfamiliar. Nostrand, Utica, Rockaway...wait, where are you? The A/C doesn't even go to Atlantic/Barclays. You are very, very lost.")
                                print("GAME OVER.")

            #path e
            if acewhich.lower() == "world trade center" or acewhich.lower() == "wtc" or acewhich.lower() == "e" or acewhich == "E": #bad end
                 print("Uh oh... as you find out only after you step on the train, the E train only goes uptown from here, the opposite direction of where you need to go! Where even are you? You will DEFINITELY be late for dinner.")
                 print("GAME OVER.")
                 valid_chamwtc = True

    #path 1/2/3
    if trainline == "123":
        valid_trainline = True
        print("Congratulations! You chose the wrong train. You walk onto the station and there is a 823682471 hour delay. The next train comes in [error: not found] minutes. You die waiting for the train, and you never see your lovely family again. You Lose.")

    #path r/w
    if trainline == "RW":
        valid_trainline = True
        print ("Congrats you made it to the train station! Now it's time to choose if you're going to take R or W")
        rorw= input()
        if rorw == "w" or rorw == "W":
            print ("Wait... the W train doesn't even go to Brooklyn! where are you??")
            time.sleep(1)
            print ("GAME OVER")
        if rorw == "r" or rorw == "R":
            print ("Uptown or Downtown?")
            uptowndowntown = input()
            if uptowndowntown == "uptown" or uptowndowntown == "Uptown":
                print("You are now completely lost. You have no idea where to go!")
                time.sleep(1)
                print("GAME OVER.")
            if uptowndowntown == "downtown" or uptowndowntown == "Downtown":
                print("The trains zoom by and you arrive at Atlantic avenue. Do you want to get off? Y/N")
                winning2 = input()
                if winning2 == "yes" or winning2 == "Yes" or winning2 == "y" or winning2 == "Y":
                    print("You are on Atlantic Ave and you get home safely and quickly.")
                    time.sleep(1)
                    print("YOU WIN!")
                if winning2 == "no" or winning2 == "No" or winning2 == "N" or winning2 == "n":
                    print("You did not arrive at atlantic Avenue, you are lost.")



    #path superhero
    if trainline == "fly":
        print("You fly home. Yeah, "+frogname+", you're a honest business-frog by day..........and a VIGILANTE BY NIGHT! Protecting the streets of Atlantic Avenue is your sacred duty, and it is one you bear with pride. That won't stop you from being home in time for dinner, though.")
        time.sleep(2)
        print("YOU WIN!")
        valid_trainline = True
