# - have checkpoints where you can rest
# - can die of starvation, disease, or drowning
# - can hunt (random pounds of food), set how many miles you want to go per day
# - goal: get to the end in the shortest number of days possible
# - random factors: lose clothes in river, bad weather delays, food spoils, find food or abandoned supplies

#introduction
print("""ISLAND ADVENTURE
~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~
YOU WAKE UP ON A DESERTED ISLAND. YOUR GOAL IS TO MAKE IT TO THE OTHER SIDE OF THE ISLAND,
WHERE THERE ARE SHIPS THAT CAN TAKE YOU HOME, IN THE SHORTEST AMOUNT OF TIME POSSIBLE.
GOOD LUCK (YOU'RE GONNA NEED IT).""")

#creating a character
class Character(object):
        """Character class"""
        def __init__(self, name):
            self.name = name
            self.inventory = {
            'food': 0,
            'clothes': 2,
            'money': 50}
            self.day = 1
            self.distance_left = 25
            self.total_distance = 100
            self.health = 100
            print(f"""Welcome, {name}. You wake up with only the clothes on your back and $50 in your pocket.""")
        def list_inventory(self):
            for k, v in self.inventory.items():
                print(f"""{k} --- {v}""")
        def list_status(self):
            print(f"""
            Day --- {self.day}
            Distance until next checkpoint --- {self.distance_left}
            Health --- {self.health}
            """)
        def list_walk(self, miles = 5):
            self.distance_left -= miles
            self.total_distance -= miles
            self.day += 1
            if self.inventory['food'] > 0:
                self.inventory['food'] -= 2
            print(f"""

            Day: {self.day} --- Next Checkpoint in: {self.distance_left} miles

            """)


#defining the character
a = Character(input("""What is your name? \n - """))

# #a robber class
# class Robber(object):
#     def __init__(self, name):
#         self.stolen =

#actions
b = int(input(f"""What would you like to do?
1. Inventory
2. Status
3. Go forward (miles left: {a.distance_left})\n - """))


if b == 1:
    a.list_inventory()
elif b == 2:
    a.list_status()
elif b == 3:
    a.list_walk()
else:
    print("""invalid input. try again \n - """)


if a.total_distance == 95:
    c = int(input("""You approach the edge of the dense forest.
On the outskirts of the trees seems to be a sketchy hut with an old man sitting in a lawn chair outside it.
What do you do?
1. Inventory
2. Status
3. Approach the sketchy vendor
4. Keep on walking - you don't want to cause any trouble \n - """))
    if c == 1:
        a.list_inventory()
    elif c == 2:
        a.list_status()
    elif c == 3:
        int(input("""You slowly walk towards the vendor, and he greets you with a smile.
        'Would you like to buy something?' he says. 'Here are my prices:'
            1. food --- $1 per pound
            2. clothes --- $3 per piece
            3. life advice --- $5\n - """))
    elif c == 4:
        a.list_walk()
    else:
        print("""invalid input. try again \n - """)


# a.inventory{'food'} += 1

