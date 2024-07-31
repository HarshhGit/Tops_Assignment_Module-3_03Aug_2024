# Q.11]  Write a Python program to find the second smallest number in a list.


list1 = [10,5,20,30]

if len(list1) < 2:
    print("List isn't correct!!!")
else:
    second_small = list1
    second_small.sort()
    print ("Second smallest number is: ",second_small[1])



#can't sort() list directly