# %%
import random

def add(list):
    temp = []
    for i in list:
        temp.append(i)
    return temp

#initialize population
population = [[2,3,5,7],[2,4,6,8],[1,3,5,7],[4,6,8,9]]

#selection
parent1, parent2 = [],[]
while parent1 == parent2:
    parent1 = population[random.randint(0,3)]
    parent2 = population[random.randint(0,3)]
print("First parent = ",parent1)
print("Second parent = ",parent2)

#crossover
crossover_point = random.randint(0,len(parent1)-1)
print("cross over point = ",crossover_point)
child = []
for i in range(crossover_point,len(parent1)):
    temp = parent1[i]
    parent1[i] = parent2[i]
    parent2[i] = temp
    child.append(add(parent1))
    child.append(add(parent2))
    temp = parent1[i]
    parent1[i] = parent2[i]
    parent2[i] = temp

#mutation
for member in child:
    mut_point = random.randint(0,len(member)-1)
    member[mut_point] = int(member[mut_point]/random.randint(1,3))

#display data
print("Now the added population are: ")
print(child)


# %%



