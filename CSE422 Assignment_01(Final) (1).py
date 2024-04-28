#!/usr/bin/env python
# coding: utf-8

# In[14]:


from queue import PriorityQueue
f1 = open('C:\\Files\\output\\input_01.txt','r')
f2=open('C:\\Files\\output\\input_01.txt','r')
heuristic_value={} #HEURISTIC
cost={} #PATH COST
pc_graph={}  #PATH COST GRAPH

for line in f1:
    words = line.split()
    heuristic_value[words[0]] =int(words[1]) #KEY WORD FOR DICTIONARY
#print("Heuristic Dictionary:",'\n',heuristic_value)

for p_cost in f2:
    s1=p_cost.split()
    for i in range(2,len(s1),2):
        cost[s1[i]]=int(s1[i+1]) #KEY VALUE FOR DICTIONARY
    pc_graph[s1[0]]=cost
    cost={} #CLEAR FOR NEXT ITERATION
#print("Map Dictionary:",'\n',pc)

Start_Node=input("Please Enter the Start Node : ")
Goal_Node=input("Please Enter the Destination Node : ")

path={}
dist={}
distance={}
q=PriorityQueue()
q.put((0,Start_Node))
dist[s_node] = 0
temp={}
distance[Start_Node]=dist
path[Start_Node]= None
n=[]
m=0
key=[]
d=0
c=0
e=0

while q!=(): #UNTILL EMPTY
    d=[]
    current=q.queue[0][1]
    #print(q.queue)
    g= q.get()
    for i in distance.keys(): 
        for a,b in distance[i].items():
            if a==current:
                c=i #SHORTEST DISTANCE
    d.append(current)      
    #print(c)
    #print("\n")
    if c in path.keys():
        d.append(e)  
    path[c]=d
    e=current
    #print(path)
    key.append(current)

    if (current == Goal_Node):
        break
    elif current==Start_Node:
        result=0
    else:
        if current in distance[i].keys():
            result=distance[i][current]
        else:
            for i in distance.keys():
                for k,l in distance[i].items():
                    if current in k:
                        result=l
    #print(result)


  
    for new,val in pc[current].items():
        #print(pc[current].keys())
        #print(new)
        #print(val)
        g_cost = result + int(val)
        #print(g_cost)
        if (new not in key or g_cost < distance[dist[new]]):
            key.append(new)
            #print(key)
            if current in distance:
                dist[new]=g_cost
                distance[current]=dist
                #print(distance)
            else:
                temp[new]=g_cost
                dist={}
                dist=temp.copy()
                #print(temp)
                distance[current]=dist 
                temp={}

        #print(distance)
        f_cost = g_cost + hv[new]
        #print(f_cost)
        q.put((f_cost, new))
        key=[]          
#print(distance)
if s_node in path:
    #print(path)
    final_path=[]
    for i in path.keys():
        final_path.append(i)
    final_path.append(Goal_Node)
    #print(final_path)
    print("Path: ",end='')
    print(*final_path,sep='->')
else:
    print("NO PATH FOUND")
print('\n')
print("Total distance : ",distance[i][Goal_Node],"km")


# In[9]:


import random

# Step 1: Model the selected batsman array in a suitable way
def model_batsmen(batsmen):
    return [batsman[0] for batsman in batsmen]

# Step 2: Write a fitness function
def fitness_function(selected_batsmen, target_score):
    total_runs = sum(batsman[1] for batsman in selected_batsmen)
    return total_runs - target_score

# Step 3: Write the crossover function
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Step 4: Write the mutation function
def mutation(individual, mutation_rate):
    mutated_individual = []
    for gene in individual:
        if random.random() < mutation_rate:
            mutated_individual.append(int(not gene))  # Flip the bit
        else:
            mutated_individual.append(gene)
    return mutated_individual

# Step 5: Create a population of randomly generated selected-batsman arrays
def create_population(num_population, num_batsmen):
    population = []
    for _ in range(num_population):
        individual = [random.randint(0, 1) for _ in range(num_batsmen)]
        population.append(individual)
    return population

# Step 6: Run genetic algorithm
def genetic_algorithm(batsmen, target_score, num_population, max_iterations, mutation_rate):
    population = create_population(num_population, len(batsmen))
    best_fitness = float('-inf')
    best_individual = None

    for iteration in range(max_iterations):
        fitness_scores = []
        for individual in population:
            selected_batsmen = [batsmen[i] for i in range(len(individual)) if individual[i] == 1]
            fitness = fitness_function(selected_batsmen, target_score)
            fitness_scores.append((individual, fitness))

            if fitness > best_fitness:
                best_fitness = fitness
                best_individual = selected_batsmen

        # Check if the target score is reached
        if best_fitness == 0:
            return best_individual

        # Select parents for crossover
        # Add a constant offset to ensure weights are greater than zero
        fitness_offset = abs(min(fitness for _, fitness in fitness_scores)) + 1
        parents = random.choices(fitness_scores, k=2, weights=[fitness + fitness_offset for _, fitness in fitness_scores])

        # Perform crossover and mutation
        child1, child2 = crossover(parents[0][0], parents[1][0])
        child1 = mutation(child1, mutation_rate)
        child2 = mutation(child2, mutation_rate)

        # Replace the least fit individuals in the population
        population = [individual for individual, _ in fitness_scores]
        population = sorted(population, key=lambda x: fitness_function([batsmen[i] for i in range(len(x)) if x[i] == 1], target_score), reverse=True)[:num_population - 2]
        population.append(child1)
        population.append(child2)

    # Sort the best_individual according to the original batsmen order
    best_individual = sorted(best_individual, key=lambda x: batsmen.index(x))

    return best_individual

num_batsmen = 8
batsmen=['8', '330', 'Tamim', '68', 'Shoumyo', '25', 'Shakib', '70', 'Afif', '53', 'Mushfiq', '71', 'Liton', '55', 'Mahmudullah', '66', 'Shanto', '29']
target_score= 330

# Perform genetic algorithm
num_population = 100
max_iterations = 1000
mutation_rate = 0.01

selected_batsmen = genetic_algorithm(batsmen, T, num_population, max_iterations, mutation_rate)

# Print the output
if selected_batsmen is not None:
    selected_names = [batsman[0] for batsman in selected_batsmen]
    binary_string = ''.join('1' if batsman in selected_names else '0' for batsman in batsmen)
    print(selected_names)
    print(binary_string)
else:
    print(-1)


# In[ ]:





# In[ ]:




