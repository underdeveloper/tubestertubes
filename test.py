def foo2(func_list):
    # function block
    func_list.append(30)  # append an element

def foo3(func_list):
    # function block    
    del func_list[1]  # delete 2nd element

def foo4(func_list):
    # function block    
    func_list[0] = 100  # change value of 1st element

# main or caller block
list1 = [10, 20]
list2 = list1   # list1 and list2 point to same list object

print('original list:', list1)
print('list1 id:', id(list1))

print('value of list2:', list2)
print('list2 id:', id(list2))

foo2(list1)
print('\nafter foo2():', list1)
print('list1 id:', id(list1))

print('value of list2:', list2)
print('list2 id:', id(list2))

foo3(list1)
print('\nafter foo3():', list1)
print('list1 id:', id(list1))

print('value of list2:', list2)
print('list2 id:', id(list2))

foo4(list1)
print('\nafter foo4():', list1)
print('list1 id:', id(list1))

print('value of list2:', list2)
print('list2 id:', id(list2))