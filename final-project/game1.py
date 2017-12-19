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
            self.status = {
                'day': 1,
                'health': 100,
                'miles to next checkpoint': 50}
            print(f"""Welcome, {name}. You wake up with only the clothes on your back and $50 in your pocket.""")
        def list_inventory(self):
            for k, v in self.inventory.items():
                print(f"{k} --- {v}")
        def list_status(self):
            for k,v in self.status.items():
                print(f"{k} --- {v}")
        def list_walk(self, miles = 5):
            for value in self.status.values():
                self.status.value('miles to next checkpoint') -= miles

#defining the character
a = Character(input('What is your name?\n - '))


# #a robber class
# class Robber(object):
#     def __init__(self, name):
#         self.stolen =

#actions
print(input("""What would you like to do?
1. Inventory
2. Status
3. Go forward\n - """))
if 1:
    a.list_inventory()
elif 2:
    a.list_status()
elif 3:
    a.list_walk()
else:
    print('invalid input. try again')


# a.inventory{'food'} += 1

