
d1 = {}
d2 = {1: 'a', 2: 'b'}
d3 = {}
d4 = {1: 'a', 2: 'b'}
d5 = {1: 'a', 2: 'b', 3: '3'}

lst = [d1, d2, d3, d4, d5]

print(lst)

final_dict = {}
for elem in lst:
    other = tuple(elem.items())
    if final_dict.get(other):
        final_dict[other] += 1
    else:
        final_dict[other] = 1
        
final_list = []
for el in final_dict.keys():
    final_list.append(dict(list(el)))
print(final_list)
