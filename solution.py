import csv
from functools import reduce

def get_volume(dims):
    return reduce(lambda x,y: x*y, dims, 1)

def knapsack(items, maxvolume):
    """
    Knapsack implementation that takes in items and volume of knapsack, and
    returns the list of items to maxmise value in knapsack, minimizing weight
    when they are draws

    Parameters
    ----------
    items : list of tuples: (id, price, volume, weight)
        All possible items that fit in the knapsack
    maxvolume : int
        Volume of knapsack

    Returns
    -------
    result: list
        Items that are part of the optimal solution
    """

    bestvalues = [[0 for _ in range(maxvolume+1)] for _ in range(len(items) + 1)]
    weights = [[0 for _ in range(maxvolume+1)] for _ in range(len(items) + 1)]

    for i in range(1, len(items)+1):
        _, value, volume, weight = items[i-1]
        for v in range(1, maxvolume+1):
            if volume > v:
                # Item can not fit in knapsack
                bestvalues[i][v] = bestvalues[i-1][v]
                weights[i][v] = weights[i-1][v]
            elif bestvalues[i-1][v] > bestvalues[i-1][v-volume] + value:
                # Not choosing item gives higher value
                bestvalues[i][v] = bestvalues[i-1][v]
                weights[i][v] = weights[i-1][v]
            elif bestvalues[i-1][v] == bestvalues[i-1][v-volume] + value:
                # Both not choosing item and choosing item gives same value,
                # decide based on weight
                bestvalues[i][v] = bestvalues[i-1][v]
                weights[i][v] = min(weights[i-1][v], weights[i-1][v-volume] + weight)
            else:
                # Choosing item gives higher value
                bestvalues[i][v] = bestvalues[i-1][v-volume] + value
                weights[i][v] = weights[i-1][v-volume] + weight

    result = []
    volume = maxvolume
    for i in range(len(items), 0, -1):
        more_value = bestvalues[i][volume] > bestvalues[i - 1][volume]
        less_weight = weights[i][volume] < weights[i-1][volume]
        if more_value or less_weight:
            # For item, if there is a increase of bestvalues or decrease of
            # weights, it is part of the optimal solution
            result.append(items[i - 1])
            volume -= items[i-1][2]
    result.reverse()

    return result

tote_dims = [45,30,35]
tote_dims.sort()
tote_volume = get_volume(tote_dims)

memoize = {}
items = [] #(id, price, volume, weight)
rejected = 0
# Get items from csv and remove those that dont fit in tote
with open('products.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        item = [int(x) for x in row]
        item_dims = item[2:5]
        item_dims.sort()
        fit = (item_dims[0] <= tote_dims[0] and item_dims[1] <= tote_dims[1] and item_dims[2] <= tote_dims[2])
        if fit:
            items.append((item[0], item[1], get_volume(item_dims), item[5]))
        else:
            rejected +=1
    print("Number of items that do not fit the tote: {}".format(rejected))

optimal_items = knapsack(items, tote_volume)
print(optimal_items)
