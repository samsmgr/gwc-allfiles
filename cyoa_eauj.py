#cyoa idle time game
#route elektra
    #1. vision
    #2. work (morgue)
#route adonis
    #1. work
    #2. quitting? meeting
    #3. bf
import time
def cutscene(str):
    print(str)
    time.sleep(2)

#character builder quiz
print("Wolf or rabbit?")
answer = input()
if answer == "wolf" or answer == "Wolf":
    wolf = True
elif answer == "rabbit" or answer == "Rabbit":
    wolf = False

print("Deer or elk?")
answer = input()
if answer == "deer" or answer == "Deer":
    deer = True
elif answer == "elk" or answer == "Elk":
    deer = False

print("Short glory or long life?")
answer = input()
if answer == "short glory" or answer == "Short glory":
    glory = True
elif answer == "long life" or answer == "Long life":
    glory = False

answer = input("The glass is half ")
if answer == "full":
    full = True
elif answer == "empty":
    full = False

#set variables
papertiger = False
colossus = False
deceiver = False
malaise = False

#character generator
if deer == True and glory == True:
    name = "elektra"
if deer == True and glory == False:
    name = "adonis"
if deer == False and glory == True:
    name = "jupiter"
if deer == False and glory == False:
    name = "ulysses"
if wolf == True and full == True:
    desc = "it is said of you that you are a colossus. you are larger than life. they meet you and you are larger still."
    colossus = True
if wolf == True and full == False:
    desc = "some snakes have evolved to mimic almost exactly the patterns and behaviors of their more poisonous relatives. those who know what they're doing know which ones are which."
    papertiger = True
if wolf == False and full == True:
    desc = "your lot in life was small enough. it is useful for others to think it remains that way."
    deceiver = True
if wolf == False and full == False:
    desc = "you are afraid. fame would build altars out of your intestine. it would not care whether you need it."
    malaise = True
print()
cutscene("you are "+name+". "+desc)

#game start
print("are you ready to play?")
input()
cutscene("the game proceeds apace.")
print()

#elektra
if name == "elektra":
    cutscene("you begin in an apartment. the shutters are drawn. there is a faint coating of dust over almost every surface, but the windowsill and the top of the bedside drawer are worn clean with the habit of nervous hands. the noise of the city seems almost sacrilegious in this suspended moment. sanctity of filth.")
    cutscene("you are going to meet god.")
    print("will you meet her in your apartment or on the street?")
    choice = input()
    #vision of god
    if choice == "apartment" or choice == "in your apartment" or choice == "in my apartment":
        cutscene("YOU EXPERIENCE A VISION OF GOD.")
        cutscene("SHE CARESSES YOUR CHEEK.")
        cutscene("YOU HAVE NEVER FELT SO LOVED.")
        cutscene("YOU NEVER WILL AGAIN.")
        print("do you continue the vision?")
        input()
        cutscene("regardless of your petty opinions. the game proceeds apace.")
        if colossus == True:
            cutscene("GOD DOES NOT SPEAK TO YOU.")
            cutscene("YOU SPEAK TO HER.")
            cutscene("SHE SPEAKS THROUGH YOU.")
            cutscene("HER NAME IS")
            time.sleep(1)
        if papertiger == True:
            cutscene("GOD LOOKS THROUGH YOU.")
            cutscene("MOUSE BECOMES THE SUN.")
            cutscene("ADDERS DO NOT CRAWL.")
            cutscene("WHAT HAVE YOU DONE")
            time.sleep(1)
        if deceiver == True:
            cutscene("YOU ARE NOT REPENTANT.")
            cutscene("HOW CAN THIS BE.")
            cutscene("YOU ARE NOT KNOWN.")
            cutscene("THERE ARE NO STARS")
            time.sleep(1)
        if malaise == True:
            cutscene("GOD IS THE SUMMATION.")
            cutscene("SHE EXPERIENCES ENTIRELY.")
            cutscene("SHE EXPERIENCES PITY.")
            cutscene("THE PITY IS FOR YOU")
            time.sleep(1)
        cutscene("the vision ends.")
        cutscene("you go outside. this could never last forever.")
    if choice == "street" or choice == "the street" or choice == "on the street":
        cutscene("you go out on the street to meet god.")
        cutscene("she works in mysterious ways. on the street, someone says to you")
        if colossus == True:
            cutscene("don't i know you?")
        if papertiger == True:
            cutscene("you look just like someone that i. well. i knew her, once.")
        if deceiver == True:
            cutscene("can it be?")
        if malaise == True:
            cutscene("you used to be someone, didn't you? or maybe you didn't.")
        print("you say")
        input()
        cutscene("someone turns away.")
    #work/brother
    cutscene("the cold bites at your cheeks. it is unseasonably cold for this time of year, and you unseasonably dressed. you think perhaps you should have been born to a warmer clime.")
    cutscene("you are in mourning.")
    cutscene("you have recently become an orphan. this was through some unavoidable circumstance and some of your own fault.")
    cutscene("as a result of what happened, your brother is no longer speaking to you.")
    cutscene("you were always close with him. less so with your sisters, so their distance comes as no surprise.")
    cutscene("considering what happened.")
    if colossus == True:
        cutscene("it was necessary.")
    if papertiger == True:
        cutscene("you regret it.")
    if deceiver == True:
        cutscene("you do not regret it.")
    if malaise == True:
        cutscene("you wish it could have happened any other way. it probaby could have. you wish it had happened any other way.")
    print()
    cutscene("you don't have any close friends. you don't have a fiancee any more.")
    cutscene("as such, your only regular source of human contact is from your coworker, whose name you don't know.")
    cutscene("you work at a morgue.")
    cutscene("morbid, perhaps. you think it suits you.")
    morguetime = False
    while not morguetime:
        print("do you want to go there now?")
        choice = input()
        if choice == "yes":
            morguetime = True
            cutscene("to be continued")
            #elektra goes to work.adonis is her co-worker. he's thinking about quitting.
        if choice == "no":
            cutscene("you should go to work. you can't call out forever.")
            cutscene("you decide to text your brother.")
            cutscene("you say")
            input()
            time.sleep(2)
            cutscene("he probably won't respond.")
            time.sleep(2)
            cutscene("he doesn't.")
            cutscene("you decide to go to work.")

#adonis
if name == "adonis":
    cutscene("you work at a morgue.")
    cutscene("it's a little morbid. too morbid.")
    cutscene("you've been thinking about quitting.")
    cutscene("you're the kind of person who always gets told you wear your heart on your sleeve.")
    if colossus == True:
        cutscene("how could you do anything else?")
    if papertiger == True:
        cutscene("you do your best.")
    if deceiver == True:
        cutscene("whether or not it's the case.")
    if malaise == True:
        cutscene("whatever that means.")
    cutscene("you do not keep many secrets. in fact, you've told your coworker already that you want to quit.")
    cutscene("she is a sharp, thin woman. she reminds you of a ghost -- a vengeful one -- but only the living are morgue attendents.")
    cutscene("maybe i'll go into modeling, you tell elektra.")
    cutscene("you don't have the face for it, she tells you.")
    cutscene("that's a little hurtful. as is her way, you guess.")
    if colossus == True:
        cutscene("well, it's only words.")
    if papertiger == True:
        cutscene("you try not to mind it.")
    if deceiver == True:
        cutscene("well, let her think it hurts you.")
    if malaise == True:
        cutscene("you're used to it, but it still stings.")
    cutscene("you tell her, no, really.")
    cutscene("i don't care for this job. all these dead things.")
    cutscene("she says,")
    cutscene("you're already dead, adonis.")
    cutscene("i'm the only one in the whole world who's alive.")
    cutscene("you guess grief does strange things to people.")
    cutscene("if, that is, elektra grieves at all.")
    cutscene("it's hard to tell.")

#jupiter
elif name == "jupiter":
    cutscene("to be continued")

#ulysses
elif name == "ulysses":
    cutscene("an old friend of yours died the other day.")
    cutscene("well, he wasn't your friend.")
    cutscene("and he didn't die the other day.")
    cutscene("he died six months ago, as best you can tell. but you found out today.")
    cutscene("his family is probably grieving. he had four children, you think. three girls and a boy. and he had a wife.")
    cutscene("he used to tell you about her.")
    if colossus == True:
        cutscene("you don't remember much of what he said. it was a different time, back then. you've changed a lot. but he hasn't.")
        cutscene("since he's dead.")
        cutscene("the dead don't change much, you don't think.")
    if papertiger == True:
        cutscene("it always seemed like he cared for her.")
        cutscene("it's a pity, what happened.")
    if deceiver == True:
        cutscene("you wish someone had told you about him, when he died and not six months after.")
        cutscene("six months. it's a long time for a man to be dead and you to have no idea.")
        cutscene("especially for clever ulysses.")
        cutscene("although you had other things on your mind.")
    if malaise == True:
        cutscene("it's a shame, everything that happened.")
        cutscene("if you had been there, maybe it would have been very different.")
        cutscene("it's none of your business, though.")
    print()
    cutscene("you think about doing something to help, in memory of him.")
    cutscene("some kind of gesture.")
    cutscene("maybe you should get a lawyer for the girl, the daughter. an expensive one.")
    cutscene("you're not sure if she needs one.")
    cutscene("doesn't look like anyone is left to prosecute her.")
    cutscene("maybe the best thing to do is just leave it all alone. let them sort it out.")
    print("should you do that?")
    choice = input()
    if choice.lower() == "yes" or choice.lower() == "y":
        cutscene("it's for the best.")
    if choice.lower() == "no" or choice.lower() == "n":
        cutscene("no... no, you should do something. at least something.")
        cutscene("letting it sit will leave a bad taste in your mouth.")
