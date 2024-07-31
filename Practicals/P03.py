"""Q.3]. Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings."""

user = ['abc', 'xyz', 'aba', '1221','aba']
count = 0
same = []

for i in user :
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
        same.append(i)
print(f"Fisrt and last same char string: {same}")
print(f"Number of Matching String: {count} ")