import random
from HillClimbing import HillClimbing

epochs:int = 100
state:list[int] = [0,1,2,3,4]
aditional_information = [
    [0, 10, 15, 20, 25],  
    [10, 0, 35, 30, 40],  
    [15, 35, 0, 45, 50],  
    [20, 30, 45, 0, 55],  
    [25, 40, 50, 55, 0] 
]

def objective_function(aditional_information, state):
    distance = 0
    num_cities:int = len(state)
    
    for i in range(num_cities):
        current_city = state[i]
        next_city = state[(i + 1) % num_cities]  
        distance += aditional_information[current_city][next_city]
        
    return -distance

def neighboursFunction(state:list[any], index:int, only_one = False)->list[list[any]]:
    if only_one:
        neighbour = state[:]
        
        pos = index
        while pos == index:    
            pos = random.randrange(len(state))
        
        neighbour[pos], neighbour[index] = neighbour[index], neighbour[pos]

        return neighbour

    neighbours = []
    for i in range(len(state)):
        if index == i:
            continue
    
        neighbour = state[:]
        neighbour[i], neighbour[index] = neighbour[index], neighbour[i]
        
        neighbours.append(neighbour)        
    return neighbours

tsp = HillClimbing(state, aditional_information, objective_function, neighboursFunction)

tsp.Print(tsp.state)
tsp.HillClimbing(tsp.RandomMutationhillClimbing, epochs, True)
tsp.Print(tsp.state)