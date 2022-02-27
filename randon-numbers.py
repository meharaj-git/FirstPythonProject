import random
n = random.randint(0,50)
print(n)

n = random.randint(100, 200)
print(n)

rand_list = []
for i in range(0,10):
    n = random.randint(1,50)
    rand_list.append(n)
print(rand_list)

#Generate 5 random numbers between 10 and 30
random_list = random.sample(range(10, 40), 6)
print(random_list)
