import random

#1. Create a list of first names
first_names = ["John", "Paul", "George", "Ringo", "Abby", "Kate", "Michael", "Noah", "Ava", "Olivia", "Liam", "Mia", "Jacob", "Charlotte", "Ethan", "Emily", "James", "Sofia", "Alexander", "Harper"]

#2. Create a list of last names
last_names = ["Smith", "Jones", "Williams", "Brown", "Davis", "Wilson", "Martin", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Thompson", "Robinson", "Walker", "Young", "Hall", "Allen", "Wood"]

#3. Combine them randomly into a list of 100 full names
full_names = []
for i in range(100):
    full_names.append(random.choice(first_names) + " " + random.choice(last_names))

print(full_names)