import random, math

MUTATION_CHANCE = 3
TOTAL = 50000
NUM_ELEMENTS = 15
POPULATION_SIZE = 5

def rand_pair(length):
    i = random.randrange(length)
    j = random.randrange(length)
    while i == j:
        i = random.randrange(length)
        j = random.randrange(length)
    if i > j:
        i, j = j, i
    return (i, j)
    
def triangular(n):
    return (n * (n + 1))//2
    
def max_inversions(n):
    return triangular(n - 1)

def make_genes(n):
    return [rand_pair(n) for _ in range(n)]    

def mutate(genes):
    return [(rand_pair(len(genes)) if random.randint(1, 100) <= MUTATION_CHANCE else gene) for gene in genes]

def crossover(g1, g2):
    assert len(g1) == len(g2)
    point = random.randint(0, len(g1) - 2)
    if random.randint(1, 2) == 1:
        g1, g2 = g2, g1
    return g1[:point+1] + g2[point+1:]
    
####################
#Inversion counter algorithm

def count_inversions(arr): 
    arr = arr[:] #Create a copy so as not to modify the original
    temp_arr = [0]*len(arr)
    return inv_helper(arr, temp_arr, 0, len(arr)-1) 
  
def inv_helper(arr, temp_arr, left, right): 
    inv_count = 0
    if left < right: 
        mid = (left + right)//2
        inv_count += inv_helper(arr, temp_arr, left, mid) 
        inv_count += inv_helper(arr, temp_arr, mid + 1, right) 
        inv_count += merge(arr, temp_arr, left, mid, right) 
    return inv_count   

def merge(arr, temp_arr, left, mid, right): 
    if arr[mid] <= arr[mid + 1]:
        return 0
    i = left     # Starting index of left subarray 
    j = mid + 1  # Starting index of right subarray 
    k = left     # Starting index of to be sorted subarray
    inv_count = 0
    # Conditions are checked to make sure that 
    # i and j don't exceed their 
    # subarray limits. 
    while i <= mid and j <= right: 
        # There will be no inversion if arr[i] <= arr[j] 
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            # Inversion will occur. 
            temp_arr[k] = arr[j] 
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid: 
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j] 
        k += 1
        j += 1

    for i in range(left, right + 1): 
        arr[i] = temp_arr[i] 
    return inv_count 
    
#End algorithm
####################

def apply_network(arr, network):
    for a, b in network:
        if arr[a] > arr[b]:
            arr[a], arr[b] = arr[b], arr[a]

class AI:
    
    def __init__(self, arr, genes=None):
        self.arr = arr[:]
        if not genes:
            genes = make_genes(len(arr))
        self.genes = genes
        
    def go(self):
        arr = self.arr
        apply_network(arr, self.genes)
        max_inv = max_inversions(len(arr))
        inv_score = 1 - count_inversions(arr) / max_inv
        return 100 * inv_score**3
        
class Evolution:
        
    def __init__(self, arr):
        self.arr = arr
        self.AI = [AI(arr) for _ in range(POPULATION_SIZE)]
        self.best_gene = None
        
    def run(self):
        scores = []
        for ai in self.AI:
            scores.append((ai, ai.go()))
        scores.sort(key=lambda t: t[1], reverse=True)
        best1, best2 = scores[:2]
        g1 = best1[0].genes
        g2 = best2[0].genes
        self.best_gene = g1
        new_ai = []
        for _ in range(len(self.AI)):
            gene = mutate(crossover(g1, g2))
            ai = AI(arr, gene)
            new_ai.append(ai)
        self.AI = new_ai

arr = list(range(NUM_ELEMENTS))
random.shuffle(arr)

print("Given array to sort: ")
print(arr)

evolve = Evolution(arr)
msg_interv = int(TOTAL ** 0.6)

def print_time(t):
    if t <= 0:
        return "0s"
    a = []
    mins = t // 60
    secs = t % 60    
    if mins > 0:
        a.append(f"{mins}m") 
    if secs > 0:
        a.append(f"{secs}s")
    return "".join(a)

import time

runs = 0
start = time.time()
for _ in range(TOTAL):
    runs += 1
    evolve.run()
    if runs % msg_interv == 0:
        now = time.time()
        estimated_total = TOTAL * (now - start) / runs 
        remaining = round(estimated_total - (now - start))
        print(f"Runs: {runs}/{TOTAL} | Approx. {print_time(remaining)} remaining")

print("Test run:")
print("Before:")
print(arr)
apply_network(arr, evolve.best_gene)
print()
print("After:")
print(arr)
