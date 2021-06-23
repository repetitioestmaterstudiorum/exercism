nested_list = [['9', '88', '7'], ['5', '3', '2'], ['6', '6']]

# this...
new_rows = []
for row in nested_list:
    new_list = []
    for el in row:
        new_list.append(int(el))
    print(new_list)
    new_rows.append(new_list)
print(new_rows)

# ...becomes (is same as):
print([[int(el) for el in row] for row in nested_list])
