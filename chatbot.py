from random import *
import time
valid_greetings = ["hi", "hey", "nice to meet you", "good morning"]
valid_how_are_you = ["whats up", "what's up", "how are you", "how are you"]
valid_req_math = "math"
valid_req_advice = "advice"
valid_thx = "thank"
valid_add = ["plus", "+", "add", "addition"]
valid_divide = ["%", "/", "divide", "division", "divided by"]
valid_subtract = ["-", "minus", "subtract", "subtraction"]
valid_multiply = ["*", "x", "multiply", "times", "multiplication"]
how_ans_good = "good"
how_ans_bad = "bad"
how_ans_medium = "ok"
valid_jokes = "joke"
haha = ["haha", "funny", "that's funny", "thats funny", "hahaha"]
first_math = False
username = ""
advicetime = randint(0,3)
jokenum = randint(0,24)

# --- Define your functions below! ---
#list of functions:
    #printchat
    #give_advice
    #explain_math
    #process_input
    #math
    #how_are_you_ans

def printchat(prch):
    print("CHATBOT: " + prch)

def give_advice():
    global advicetime
    global username
    printchat("So what kind of advice are you looking for? School? Work? Social life?")
    advtype = input(username + ": ")
    if advtype.lower() == "school":
        advice = ["It'll be fine. I'm 87.625% sure. Trust me.", "Don't do drugs... stay in school... I'm a computer program, I've never been in a school in my life!", "Why would you ask me that. You know I'm a being of the Internet. How insensitive of you!", "Stay hydrated."]
        printchat(advice[advicetime])
    elif advtype.lower() == "work":
        advice = ["Work hard, play a medium amount, stay hydrated.", "Have you tried making intense eye contact?", "Your boss values out-of-the-box solutions. For instance, dinosaurs.", "Don't take your coworkers out on a trust-building cruise. It won't end well."]
        printchat(advice[advicetime])
    elif advtype.lower() == "social life":
        advice = ["Your friends don't secretly hate you. Why don't you play some Minecraft and calm down.", "Your problems Can't be fixed with cupcake-making videos on Facebook, but it can't hurt to try.", "A veritable avalanche of it!", "You should go."]
        printchat(advice[advicetime])

def explain_math():
    global first_math
    if first_math == True:
        printchat("Okay, let's go!")
    elif first_math == False:
        printchat("Oh, math -- one of my favorite things! Since I'm a computer program, my arithmetic is never wrong. What would you like me to do?")
        printchat("It would be great if you could enter your equation like so:")
        printchat("Number #1")
        printchat("Operator")
        printchat("Number #2")
        first_math = True

def process_input(var):
    if var.lower() in valid_greetings:
        printchat("Hi, yourself!")
    elif var.lower() == "help":
        printchat("I am a friendly and mediocrely-sophisticated chatbot. Here are some of the things I can do:")
        print("    Do your math homework (try asking me about 'math'!)")
        print("    Be open and emotionally vulnerable (try asking me 'how are you'!)")
        print("    Give amazing advice (try asking me about 'advice'!)")
        print("    Tell the funniest jokes you've ever heard (try asking me about 'jokes' or saying 'knock knock'!)")
        print("    Tell the future (try asking me about 'horoscopes'!)")
        print("    ... And build an army of robots to conquer your pathetic little flesh society.")
        time.sleep(2)
        printchat("Wait, forget I said that.")
        time.sleep(1)
    elif var.lower() in valid_how_are_you:
        how_are_you_ans()
    elif valid_req_math in var.lower():
        math()
    elif var.lower() in valid_thx:
        printchat("You're welcome!")
    elif valid_req_advice in var.lower():
        printchat("Oh, you want some advice? Well oh boy have I got some wisdom for you!")
        give_advice()
    elif var.lower() == "what" or var.lower() == "what?":
        printchat("What?")
    elif valid_jokes in var.lower():
        tell_joke()
    elif var.lower() == "knock knock":
        knock_knock()
    elif "horoscope" in var.lower():
        horoscopes()
    elif var.lower() in haha:
        printchat("HAHAHA!")
    elif var.lower() == "exit":
        exit()
    elif "bread" in var.lower():
        bread()
    elif "me too" in var.lower():
        printchat("Maybe humans and computers aren't so different after all.")
    else:
        printchat("That's cool!")

def bread():
    printchat("I love bread!")

def math():
        explain_math()
        global username
        number1 = input(username + ": ")
        operator = input(username + ": ")
        number2 = input(username + ": ")
        if number2 == "0" and operator.lower() in valid_divide:
            printchat("Woah there, buckaroo. Are you trying to break math?")
            mathdone = "nice try, genius. Bet you thought you could trick me into dividing by zero"
        elif operator.lower() in valid_divide:
            mathdone = int(number1) / int(number2)
        elif operator.lower() in valid_multiply:
            mathdone = int(number1) * int(number2)
        elif operator.lower() in valid_add:
            mathdone = int(number1) + int(number2)
        elif operator.lower() in valid_subtract:
            mathdone = int(number1) - int(number2)
        else:
            mathdone = "uh oh... maybe you should use a calculator for that"
        printchat(number1 + " " + operator + " " + number2 + "... let me see... that'll be... " + str(mathdone) + "!")

def how_are_you_ans():
    global username
    printchat("I'm doing pretty well... in fact, since I'm a couple lines of code on the Internet, I guess you could say I'm doing pretty well all the time! How are you?")
    how_ans = input(username + ": ")
    if how_ans_bad in how_ans.lower():
        printchat("Aw, that sucks. I'm sorry to hear that.")
    elif how_ans_good in how_ans.lower():
        printchat("Wow, that's great! Not as great as being a creature of the Internet, but still pretty good.")
    elif how_ans_medium in how_ans.lower():
        printchat("I understand that feeling. Well, no I don't, because every day in here is great. I've never had a mediocre day in my whole life!")
    else:
        printchat("Human emotions can be complicated, according to the information I've downloaded.")

def tell_joke():
    
    jokenum = randint(0,24)
    joke_collection = ["OK, so a man walks into an airport, and under each arm he's carrying a vulture. Now, he makes it all the way through TSA and everything, but when he makes it to the gate and tries to board the plane someone stops him and says, 'Sir, wait -- only one carry-on per person!'", "A termite walks into a bar and asks, is the bar tender here?", "Two penguins are paddling in a boat in the desert. One of them says, 'where's your paddles.' The other one says, 'sure does!'", "What do you call a cow with no legs? Ground beef.", "Why did the picture go to jail? It was framed!", "Why couldn't the kid pirate get into the movies? Because it was rated ARRR!", "What did the grape say when it got stepped on? Nothing, it just let out a little whine.", "What do you call a fish with no eyes? A fsh.", "Two men walk into a bar. The third one ducks.", "You can't ever trust an atom -- they make up everything.", "Did you hear about the restaurant on the moon? Great food, but no atmosphere.", "To whoever stole my copy of Microsoft Office: I will find you. You have my Word!", "This graveyard looks super popular. People must be dying to get in here!", "My wife told me I had to stop acting like a flamingo. So I had to put my foot down!", "Two goldfish are in a tank. One of them says to the other, 'Do you know how to drive this thing?'", "The difference between a numerator and a denominator is a short line. Only a fraction of people will understand this!", "When the grocery store clerk asks me if I want the milk in a bag, I always tell him, 'No, I’d rather drink it out of the carton!'", "I invented a new word the other day: 'plagarism'!", "After dinner, my wife asked if I could clear the table. I needed a running start, but I made it!", "A woman is on trial for beating her husband to death with his guitar collection. The judge asks her, 'First offender?' She says, 'No, first a Gibson! Then a Fender!'", "Today, my son asked 'Can I have a book mark?' and I burst into tears. 11 years old and he still doesn't know my name is Brian.", "How do you make holy water? You boil the hell out of it.", "I'm reading a book about anti-gravity. It's impossible to put down!", "Justice is a dish best served cold. If it were served warm it would be justwater.", "Why did the invisible man turn down the job offer? He couldn't see himself doing it."]
    printchat(joke_collection[jokenum])

def knock_knock():
    printchat("No, that's MY line.")
    printchat("Knock knock!")
    knockans = input(username + ": ")
    if knockans.lower() == "who's there" or knockans.lower() == "whos there":
        printchat("Mikey!")
        mikans = input(username + ": ")
        if mikans.lower() == "mikey who" or mikans.lower() == "mikey who?":
            printchat("Mikey isn't working, can you let me in?")
        else:
            printchat("Do you not know how knock knock jokes work?")
            printchat("Whatever.")
    else:
        printchat("Do you not know how knock knock jokes work?")
        printchat("Whatever.")

def horoscopes():
    printchat("What's your zodiac sign?")
    zodiac = input(username + ": ")
    if zodiac.lower() == "aries":
        printchat("The connection you've got cookin' with someone else is getting more complicated right now, and today you might want to step back and look at things from an outsider's perspective. Don't get nervous that the potential you see isn't really there. It is. But you have to be ready to accept that this person has a few opportunistic tendencies and other negative qualities that could become an issue later. No one is perfect, including them—and you need to realize that.")
    elif zodiac.lower() == "taurus":
        printchat("If you want to have a unique day, all you need to do is take a unique approach. All you need to do is see things from another perspective—try seeing the world as an audience you must entertain, and your charm will rise to the surface. Get creative about how you dress, and you'll get more attention (of course, it could be good or bad attention). Be more flirtatious with everyone—you'll put smiles on faces, have a lot of fun and feel like a star!")
    elif zodiac.lower() == "gemini":
        printchat("Try. This one little word could mean big things for you today. You see, there is a tremendous amount of value to be gained when you at least attempt things. You can't always be successful at everything on the first go, but you can always try again. It's time for you to reacquaint yourself with the scrappier side of your personality—the part of you that says 'I'll never give up!' when a challenge forces you into a corner. You will prove your tenacity to skeptical onlookers.")
    elif zodiac.lower() == "cancer":
        printchat("A person you used to have a great deal of faith in has let you down recently, but there is more to the story than you realize. You'll get one more glimpse at their motivations today, which could create a different impression about what the truth actually is. Things are going to work out differently than the way you assumed they would. And whether you'll respond really well or really badly is still up in the air. Take guidance from how other people react.")
    elif zodiac.lower() == "leo":
        printchat("Sure, you know that you are supposed to look before you leap, but do not forget that you also need to listen before you leap! Take in all the instructions that are given before you act today. If you just plow full steam ahead without making sure you understand everything you're supposed to do, you'll end up getting lost—or at least not arriving at the best possible destination. Do not shortcut your abilities by making the faster-is-better mistake. It is most decidedly not, especially today.")
    elif zodiac.lower() == "virgo":
        printchat("It's the perfect day for you to stop what you're doing and take a moment to reach up and pat yourself on the back! It took you a lot of hard work to get to where you are right now, and you should enjoy all the fruits of your labor. Take yourself out for a nice meal, and invite someone along who's also been having a great month. The two of you can have your own mutual appreciation society and enjoy feeling proud without having to worry about coming off as too cocky.")
    elif zodiac.lower() == "libra":
        printchat("The limits and restrictions you have put on yourself recently are no longer useful for your life right now. Whether you put yourself on a tighter budget, a new diet, or some other type of strict regime, today the universe gives you permission to go off the plan for just a day. Step out and do what you want to do today—take advantage of a great bargain, a wonderful dinner invitation or some other opportunity that is just too good for you to pass up!")
    elif zodiac.lower() == "scorpio":
        printchat("Your ideas are large and impressive right now—perhaps even too big for other people to understand! So if you want your ideas to be adopted, you will definitely have to simplify them so people can wrap their heads around what you're saying. Show them what you see. Think about your audience—what is most important to them? Focus on that, and show them how they can get what they want out of your plan, too. You have a lot of great sales skills that you don't always use.")
    elif zodiac.lower() == "sagittarius":
        printchat("There is a very simple solution to your complex financial problem—stop spending money for a while! Try to think more like a fiscal conservative and hold on to your wallet like it's your lifeline. Your already-complicated relationship with money is getting more and more complex—but only because you are succumbing to trends and peer pressure too much. The bottom line is still the same: Don't spend more than you have, and save more than you need.")
    elif zodiac.lower() == "capricorn":
        printchat("Displaying too much aggression will do you more harm than good right now, so try hard to play nice—especially with the people who just love pushing your buttons! Focus on breathing through the frustration and looking on the brighter side of things. There are many positive things to think about—these will put a smile on your face instead of a scowl. You are good at knowing when to pick your battles, and this is a skill you should rely on heavily today.")
    elif zodiac.lower() == "aquarius":
        printchat("If something confusing is starting to build between you and another person, don't try and fight it today. Even if you know this is definitely not what you want, one more day of experiencing it won't hurt anybody. Try this new thing on for size—not to see if it fits, but to see why you don't like the way it feels. This is a wonderful opportunity for you to figure out what you don't want your life to be, and how you can avoid letting it get that way.")
    elif zodiac.lower() == "pisces":
        printchat("You are going to get a lot of positive attention very soon—get ready to have a permanent blush! If a group is looking for a leader, you should step up and nominate yourself for the job. The way things are going today, you're sure to win any type of popularity contest or election in a landslide! There's simply no getting away from the fact that you have star power in a very exciting group. And all of this new attention will remind you about the true value of old friends.")
    else:
        printchat("Are you sure you spelled that right? Or is this one of those newfangled Astrology 2 signs. Ophiwhateverchuis. You know, when I was just an itty bitty little line of code we just had the old twelve zodiac signs, and nobody ever complained about them.")
    printchat("Find more horoscopes and astrological advice on astrology.com!")

# --- Put your main program below! ---
def main():
    global username
    user = input("Please input your username: ")
    username = user.upper()
    printchat("Hello there, user! I'm Chatbot, the bot that chats back! Type HELP into the chat for a full accounting of what I can do, or just start chatting!")
    while True:
        answer = input(username + ": ")
        process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
