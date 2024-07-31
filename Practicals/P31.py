# Q.31} How Do You Traverse Through A Dictionary Object In Python? 

clas = {
    "stud1": 1,
    "age": 21,
    "address": "maninagar"
}

for h in clas:
    print("\nGive only keys as output: ",h) 

for i in clas.items():
    print("\nGives keys and values as tuple output:" ,i)

for g,n in clas.items():
    print("\nGives both key and values as output: ",g,n)