""" Q.8] Write a Python function that takes a list and returns a new list with unique
elements of the first list. """


def unique_elm(l):
    l = list(set(l))
    return l


list1 = [10,20,15,25,10,30]
print(f"First list without unique elements: {list1}")

print("List with unique elements: " ,unique_elm(list1))


#using typecasting to remove duplicate and than again converting into list