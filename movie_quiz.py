import time
#what does your degree of extremely specific julie andrews knowledge say about you?

rightanswer = 0
print("in The Sound of Music, actress Julie Andrews played Maria von Trapp. How old is she now?")
answer = input()
if answer == "83":
    rightanswer +=1
print("Acclaimed actress Julie Andrews has received many awards over her lifetime. Which of her awards is appended on her name?")
answer = input()
if answer == "DBE" or answer == "dbe" or answer == "dame" or answer == "Dame":
    rightanswer +=1
print("How many years were between the time of Julie Andrews' first appearance in the West End and her first appearance on Broadway?")
answer = input()
if answer == "6" or answer == "6 years":
    rightanswer +=1
print("YOUR RESULTS...")
time.sleep(3)
if rightanswer == 0:
    print("Experts would agree that you know some things about Julie Andrews, but not very many. Definitely none of the things we were expecting you to know.")
if rightanswer == 1 or rightanswer == 2:
    print("Wow! Either you know something about Julie Andrews, or you are moderately lucky!")
if rightanswer == 3:
    print("You are a real Julie Andrews fan. I am so proud of you. Really, from the bottom of my heart, I must congratulate you, #1 Julie Andrews fan.")
