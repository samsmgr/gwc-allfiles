import json
from textblob import TextBlob
import matplotlib.pyplot as plt

tweetFile = open("twitter_dataset.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

def fav_fol_counter():
    favsum = 0
    for i in range(10):
        if "favorite_count" in tweetData[i]:
            favsum += tweetData[i]["favorite_count"]
        else:
            favsum += 0
    print(favsum)

    folsum = 0
    for i in range(10):
        if "followers_count" in tweetData[i]["user"]:
            folsum += tweetData[i]["user"]["followers_count"]
        else:
            folsum += 0
    print(folsum)

subjectivity_list = []
polarity_list = []

for x in range(len(tweetData)):
    text = TextBlob(tweetData[x]["text"])
    subjectivity_list.append(text.subjectivity)
    polarity_list.append(text.polarity)

plt.hist(polarity_list,bins=[-1.1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1.1])
plt.xlabel("Polarities")
plt.ylabel("Number of Tweets")
plt.title("Histogram of Tweet Polarity")
plt.axis([-1.1,1.1,0,100])
plt.grid(True)
plt.show()
