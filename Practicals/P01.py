"""Q.1]. How will you remove last object from a list?
Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?"""

list1 = [2, 33, 222, 14, 25]

#To remove last object from list we can use pop() method that removes last object if parameter isn't given
#Right now list1 [-1] object is 25 without removing object 

rem = list1.pop()

print("Removed last object", rem)
print("After using pop()", list1)

#after using pop() new object at [-1] index is 14