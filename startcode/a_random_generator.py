import random

first = ["Orange", "Supper","Mr","Stupid","Big","Goofy","Purple","The","Super"]
second = ["Monkey","Bumba","Beast","Guy","Bob","Goober","Man","Gamer","Creature"]

for i in range(10):

    random_first = random.choice(first)
    random_second = random.choice(second)
    random_number = random.randint(999,9999)
    print(random_first+random_second+str(random_number))
