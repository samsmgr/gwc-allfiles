firstname = ["bartholomew", "ferdinand", "fred", "liberty", "aurora", "dorian"]
lastname = ["johnson", "de la vega", "adams", "smith", "moses"]

adjective = ["bitter", "burnt", "creamy", "crispy", "crumbly", "crunchy", "greasy", "juicy", "mushy", "rancid", "ripe", "salty", "sour", "unripe", "adorable", "beautiful", "clean", "drab", "elegant", "fancy", "glamorous", "handsome", "long", "magnificent", "old-fashioned", "plain", "quaint", "sparkling", "ugliest", "unsightly", "bitter", "delicious", "fresh", "greasy", "juicy", "hot", "icy", "loose", "melted", "nutritious", "prickly", "rainy", "rotten", "salty", "sticky", "strong", "sweet", "tart", "tasteless", "uneven", "weak", "wet", "wooden", "yummy", "boiling", "broken", "bumpy", "chilly", "cold", "cool", "creepy", "crooked", "cuddly", "curly", "damaged", "damp", "dirty", "dry", "dusty", "filthy", "flaky", "fluffy", "freezing", "hot", "warm", "wet", "dehydrated", "salty"]
ingredient = ["grapefruit", "foie gras", "black bean", "onion", "tomato", "kale", "xanthum gum", "peanut butter", "chocolate", "olive oil", "vinegar", "vanilla", "dried prunes", "water", "corn syrup", "sugar", "salt", "molasses", "spice", "black pepper", "tapioca", "bacon", "sesame seed", "raspberry", "wheat", "semolina", "plum", "licorice", "pineapple", "red chili pepper", "chia seed", "honey", "soybean", "pistachio", "almond", "cashew", "peanut", "kiwi", "asparagus", "apple", "avocado", "acorn squash", "artichoke", "grape", "ginger", "broccoli", "clam", "carrot", "cheese", "corn"]
dish = ["soup", "quesadilla", "fettucine", "orzo", "filet mignon", "fruit bowl", "platter", "falafel", "burger", "taco", "sandwich", "noodles", "meatballs", "linguine", "lasagna", "lamb", "kabobs", "tuna", "sushi", "bagel", "jambalaya", "stew", "hash", "grits", "gumbo", "gnocchi", "burrito", "enchilada", "dumplings", "duck", "curry", "chowder"]
appetizer = ["salad", "sashimi", "soup", "fruit bowl", "dip", "guacamole", "baba ganoush", "salsa", "bruschetta", "crepes"]
dessert = ["pie", "cupcake", "brownie", "sundae", "cake", "fudge", "ice cream", "frozen yogurt", "cookie", "pudding", "tart", "donut"]

twosy = ["playful", "preview", "quickly", "rainy", "really", "refill", "repay", "restful", "sadly", "salty", "sleepy", "slowest", "smaller", "softly", "soggy", "stopping", "subway", "sweeter", "tallest", "thankful", "thinking", "thirsty", "thoughtful", "throwing", "tractor", "treatment", "unfair", "vastly", "wanted"]
threesy = ["basketball", "bicycle", "blueberry", "broccoli", "neighborhood", "library", "umbrella", "principal", "privacy", "apricot", "piano", "potato", "piggybank", "policeman", "envelope", "telephone", "tortilla", "screwdriver", "beautiful", "computer", "hospital", "tomato", "chocolate", "spaghetti", "spiderweb", "dangerous", "dinosaur", "grandmother", "grandfather", "grasshopper", "lemonade", "tricycle"]

from random import *

var = randint(0,4)
var2 = randint(0,4)
two1 = randint(0,28)
two2 = randint(0,28)
two3 = randint(0,28)
two4 = randint(0,28)
three1 = randint(0,32)
three2 = randint(0,32)
three3 = randint(0,32)
adj1 = randint(0,(len(adjective) - 1))
adj2 = randint(0,(len(adjective) - 1))
adj3 = randint(0,(len(adjective) - 1))
desadj = randint(0,(len(adjective) - 1))
apadj1 = randint(0,(len(adjective) - 1))
apadj2 = randint(0,(len(adjective) - 1))
ing1 = randint(0,(len(ingredient) - 1))
ing2 = randint(0,(len(ingredient) - 1))
ing3 = randint(0,(len(ingredient) - 1))
desing = randint(0,(len(ingredient) - 1))
aping1 = randint(0,(len(ingredient) - 1))
aping2 = randint(0,(len(ingredient) - 1))
app1 = randint(0,(len(appetizer) - 1))
app2 = randint(0,(len(appetizer) - 1))
dis1 = randint(0,(len(dish) - 1))
dis2 = randint(0,(len(dish) - 1))
dis3 = randint(0,(len(dish) - 1))
des = randint(0,(len(dessert) - 1))

def namer():
    print(firstname[var] + " " + lastname[var2])

def haikumaker():
    print(twosy[two1] + " " + threesy[three1])
    print(twosy[two2] + " " + threesy[three2] + " " + twosy[two3])
    print(threesy[three3] + " " + twosy[two4])

def foodmaker(num):
    if num == 1:
        print(adjective[adj1] + " " + ingredient[ing1] + " " + dish[dis1])
    if num == 2:
        print(adjective[adj2] + " " + ingredient[ing2] + " " + dish[dis2])
    if num == 3:
        print(adjective[adj3] + " " + ingredient[ing3] + " " + dish[dis3])

def appmaker(num):
    if num == 1:
        print(adjective[apadj1] + " " + ingredient[aping1] + " " + appetizer[app1])
    if num == 2:
        print(adjective[apadj2] + " " + ingredient[aping2] + " " + appetizer[app2])

def dessertmaker():
            print(adjective[desadj] + " " + ingredient[desing] + " " + dessert[des])

def menumaker():
    print("experience chef sam's tasting menu of extremely appetizing foods now today!")
    print()
    print("appetizer:")
    appmaker(1)
    appmaker(2)
    print()
    print("entree:")
    foodmaker(1)
    foodmaker(2)
    foodmaker(3)
    print()
    print("dessert:")
    dessertmaker()

menumaker()

def find_the_difference():
    list = [12, 57, 79, 214, 2, 67]
    list.sort()
    diff = (list[len(list) - 1] - list[0])
    print(diff)


#create list
#add up entire list
#divide by len

def average():
    list = [5, 12, 3, 56, 24, 78, 1, 15, 44]
    i = 0
    total = 0
    while i < len(list):
        total += list[i]
        i += 1
    if i == len(list):
        avg = (total / len(list))
        print(avg)
