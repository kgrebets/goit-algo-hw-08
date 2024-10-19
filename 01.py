import heapq

def min_cost_with_heap(cables):
    if debug: print(f"Initial heap: {cables}")

    heapq.heapify(cables)
    if debug: print(f"After heapify: {cables}")
    
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        if debug: print(f"Get: {first} & {second}, heap: {cables}")

        cost = first + second
        total_cost += cost
        
        heapq.heappush(cables, cost)
        if debug: print(f"Updated heap: {cables} , cost: {total_cost}\n")
    
    return total_cost

def min_cost_without_heap(cables):
    if debug: print(f"Initial array: {cables}")
    
    total_cost = 0
    
    while len(cables) > 1:
        first = cables.pop(0)
        second = cables.pop(0)
        if debug: print(f"Get: {first} & {second}, array: {cables}")

        cost = first + second
        total_cost += cost
        
        cables.insert(0, cost)
        if debug: print(f"Updated array: {cables}, cost: {total_cost}\n")
    
    return total_cost

cables = [15, 8, 6, 12, 4]
debug = True

print("Using min heap:")
result_with_heap = min_cost_with_heap(cables.copy())
print(f"Min cost with heap: {result_with_heap}")

print("\nWithout min heap:")
result_without_heap = min_cost_without_heap(cables.copy())
print(f"Min cost without heap: {result_without_heap}")
