#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
def fitness(selected_batsmen, average_runs, target_run):
    total_runs = sum([average_runs[i] for i in range(len(selected_batsmen)) if selected_batsmen[i] == 1])
    if total_runs == target_run:
        return total_runs
    else:
        return 0
    
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(individual, mutation_rate):
    mutated_individual = individual[:]
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            if mutated_individual[i] == 0:
                mutated_individual[i] = 1
        else:
            mutated_individual[i] = 0
    return mutated_individual

def generate_population(num_individuals, num_batsmen):
    population = []
    for i in range(num_individuals):
        individual = [random.randint(0, 1) for i in range(num_batsmen)]
        population.append(individual)
    return population

def genetic_algorithm(num_individuals, num_batsmen, average_runs, target_run, mutation_rate, max_iterations):
    population = generate_population(num_individuals, num_batsmen)
    
    for _ in range(max_iterations):
        fitness_scores = [fitness(individual, average_runs, target_run) for individual in population]
        fittest_individuals = [individual for individual, fitness_score in zip(population, fitness_scores) if fitness_score > 0]
        if target_run in fitness_scores:
            winning_individual = population[fitness_scores.index(target_run)]
            return winning_individual
        
        new_generation = fittest_individuals[:]
        while len(new_generation) < num_individuals:
            parent1, parent2 = random.choices(fittest_individuals, k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            new_generation.extend([child1, child2])

        population = new_generation

    return -1  

f= open('C:\\Files\\output\\input1.txt', mode='r')
line=f.read()
#print(line)
lines=line.split('\n')
#print(lines)
list_01=' '.join(lines)
list_02=list_01.split( )
print(list_02)
list_03=[]
for i in range(2,len(list_02),2):
    list_03.append(list_02[i])
print(list_03)
list_04=[]
for i in range(3,len(list_02),2):
    list_04.append(list_02[i])
print(list_04)
average_runs=[]
average_runs = [int(i) for i in list_04]
#print(average_runs)
target_run=int(list_02[1])
#print(target_run)
num_batsmen=int(list_02[0])
#print(num_batsmen)
num_individuals = 100
#num_batsmen = 8
#average_runs = [68, 25, 70, 53, 71, 55, 66,29]
#target_run = 330
mutation_rate = 0.1
max_iterations = 1000

winning_combination = genetic_algorithm(num_individuals, num_batsmen, average_runs, target_run, mutation_rate, max_iterations)
if winning_combination:
    print("Winning combination:", winning_combination)
    for i in winning_combination:
        print(i, end='')
else:
    pass


# In[ ]:




