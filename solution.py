import csv

def get_volume(dims):
    return reduce(lambda x,y: x*y, dims, 1)

tote_dims = [45,30,35]
tote_dims.sort()
tote_volume = get_volume(tote_dims)

items = [] #[id, price, volume, weight]
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
            items.append([item[0], item[1], get_volume(item_dims), item[5]])
        else:
            rejected +=1
    print("Number of items that do not fit the tote: {}".format(rejected))
