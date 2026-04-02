grid = [
    [0,  2, -1, 3],
    [4,  0,  5, 1],
    [-1, 3,  0, 2],
    [1, -1, 4, 0]
]
second_grid = [
    [],
    [],
    [],
    []
]


num_of_signals = []
max_values = []
x_and_y = {
    "X":{
        'x_value': 'None'
    },
    "Y":
    {
        'y_value' : 'None'
    }
}
# 0 = empty, 1-9 = signal strenght, -1 = blocked cell
for list_num in range(len(grid)): #it is best to do a for x in range rather than for x in y since this method allows us to know the index
    #look for the highest value amongst them all and also max_values is the highest per row, so we kill 2 birds with one stone
    current_max_value = (max(grid[list_num]))
    max_values.append(current_max_value) 
    actual_highest_value = max(max_values) #amongst the highest values of every row take the highest
    for element in range(len(grid[list_num])):
        if grid[list_num][element] == actual_highest_value:
            x_and_y['X']['x_value'] = element #the index inside the list
            x_and_y['Y']['y_value'] = list_num #the list inside grid that it is in
    
        elif grid[list_num][element] > 0: 
           """
           why is this one 'elif'? because if we make it the leader (if-statement) then when it is 5 it will always be
           more than 0 so it will never reach the elif, whereas if we put it first (like we are doing) only be true when
           the element is = 5,else it will keeep appending to num of signals.
           """
           num_of_signals.append(element) #append to then sum after the loop and get total of signals, excluding zero or less

"""
Made two different for loops because 'if' logic messes each other up,
now what we do is iterate the same way we were doing, appending at the same list_num index the grid is currently in
"""
for list_num in range(len(grid)): #it is best to do a for x in range rather than for x in y since this method allows us to know the index
    #look for the highest value amongst them all and also max_values is the highest per row, so we kill 2 birds with one stone
    current_max_value = (max(grid[list_num]))
    max_values.append(current_max_value) 
    actual_highest_value = max(max_values) #amongst the highest values of every row take the highest
    for element in range(len(grid[list_num])):
        if grid[list_num][element] == -1:
            second_grid[list_num].append("X")
        elif grid[list_num][element] != -1:
            second_grid[list_num].append(".")


#print(x_and_y['X']['x_value'])
#print(x_and_y['Y']['y_value'])
#print(max_values)
#print(actual_highest_value)
print(second_grid)
