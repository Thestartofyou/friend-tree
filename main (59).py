\class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.time_spent_talking = 0
    
    def add_friend(self, friend):
        self.friends.append(friend)
    
    def talk(self, duration):
        self.time_spent_talking += duration
        for friend in self.friends:
            friend.time_spent_talking += duration

# create people
alice = Person('Alice')
bob = Person('Bob')
charlie = Person('Charlie')
dave = Person('Dave')

# add friends
alice.add_friend(bob)
alice.add_friend(charlie)
bob.add_friend(charlie)
charlie.add_friend(dave)

# simulate conversations
alice.talk(10)
bob.talk(20)
charlie.talk(30)
dave.talk(40)

# create a list of people sorted by time spent talking
people = [alice, bob, charlie, dave]
people.sort(key=lambda person: person.time_spent_talking, reverse=True)

# print the tree of information
for person in people:
    print(person.name)
    for friend in person.friends:
        print('--', friend.name)
