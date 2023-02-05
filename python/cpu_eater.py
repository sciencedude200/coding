import random as rnd

def eat_cpu(level):
    geuss = 0
    while True:
        geuss = rnd.randint(0,level)
        answer = rnd.randint(0,level)
        if answer == geuss:
            print("got")
            
        

eat_cpu(10000000)