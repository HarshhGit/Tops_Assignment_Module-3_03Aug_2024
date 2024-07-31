# Q.13] Write a Python program to check whether a list contains a sub list.


list1 = [1,2,3,4,5,6]
sub_list = [4,5,6]

list1_len = len(list1)
sub_len = len(sub_list)

count = 0

for i in range(list1_len - sub_len + 1):
    if list1[i:i + sub_len] == sub_list:
        count = 1
        break

if count:
    print("The list1 conatins sublist.")
else:
    print("List1 doesn't contain sublist.")