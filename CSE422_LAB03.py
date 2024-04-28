#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def generate_random_points():
    return [random.randint(10, 120) for i in range(8)]

def alpha_beta_pruning(node, alpha, beta, level):
    points = generate_random_points()
    if level == 3:  
        return node

    if level % 2 == 0:  
        value = float('-inf')
        for child in points:
            value = max(value, alpha_beta_pruning(child, alpha, beta, level + 1))
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else: 
        value = float('inf')
        for child in points:
            value = min(value, alpha_beta_pruning(child, alpha, beta, level + 1))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value
    
def calculate_points_and_winner(student_id):
    a, b, c, d, e, f, g, h = map(int, student_id)
    points = generate_random_points()
    print("Generated 8 random points between the minimum and maximum point limits:", points)
    min_points = e
    max_points = int(str(h) + str(g)) * 1.5
    total_points_to_win = int(str(h) + str(g))
    achieved_points = alpha_beta_pruning(points, float('-inf'), float('inf'), 0)
    print("Total points to win:", total_points_to_win)
    print("Achieved point by applying alpha-beta pruning =", achieved_points)

    if achieved_points >= total_points_to_win:
        print("The winner is Optimus Prime")
    else:
        print("The Winner is Megatron")

    

def simulate_shuffled_games(student_id, S):
    optimus_wins = 0
    print("After the shuffle: ")
    for x in range(S):
        random.seed(x) 
        points = generate_random_points()
        achieved_points = alpha_beta_pruning(points, float('-inf'), float('inf'), 0)
        #print(str(achieved_points))
        achieved_points = alpha_beta_pruning(points, float('-inf'), float('inf'), 0)
        print('List of all points values from each shuffle:',achieved_points)
    total_points_to_win = int(str(student_id[-1]) + str(student_id[-2]))
    

    if achieved_points >= total_points_to_win:
        optimus_wins += 1

    return optimus_wins

#Input_01(Task_01)
student_id_1 = "21181237"
calculate_points_and_winner(student_id_1)

#Input_02(Task_02)
S = int(student_id_1[3])  # Number of times to shuffle and simulate games
optimus_wins = simulate_shuffled_games(student_id_1, S)
print(f" Won {optimus_wins} times out of {S} number of shuffles")


# In[ ]:


from queue import PriorityQueue

f = open('/content/Input file 1','r')
g=open('/content/Input file 1','r')

heuristic={}
#PATH COST
pc={}
#PATH COST GRAPH
graph={}

for line in f:
  words = line.split()
  heuristic[words[0]] =int(words[1])
print(heuristic)

for pcost in g:
  s=pcost.split()
  #print(s1)
  for i in range(2,len(s),2):
    pc[s[i]]=int(s[i+1])
  graph[s[0]]=pc
  #CLEAR FOR NEXT ITTRATION
  pc={}
print(graph)


start=input("Enter starting point: ")
end=input("Enter ending point: ")

q = PriorityQueue()
q.put((0, start))
link = {}
cost= {}
path=[]
optimal_dist = 0
link[start] = None
cost[start] = 0

while not q.empty():
    current_node = q.get()[-1]
    #print(current_node)
    if current_node == end:
        break

    for key, value in graph[current_node].items():
        update_cost = cost[current_node] + value
        if key not in cost or update_cost < cost[key]:
            cost[key] = update_cost
            val = update_cost + heuristic[key]
            q.put((val, key))
            link[key] = current_node

if end not in link:
    print("No path found")
else:
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = link[current_node]
    path.reverse()

#optimal_dis
for i in range(len(path) - 1):
    optimal_dist += graph[path[i]][path[i+1]]

print("Path:", " -> ".join(path))
print("Total Distance:", optimal_dist)

