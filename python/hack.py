import random
password = random.randint(0,999)
geuss = 0
print(password)
while True:
    geuss = geuss + 1
    password = random.randint(0,999)
    if geuss == password:
        print("got")