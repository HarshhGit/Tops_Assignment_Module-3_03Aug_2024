# Q.44]  Write a Python function to check whether a number is in a given range

def in_range(num,start,end):
    return start <= num <= end

print(in_range(5,0,15))
print(in_range(15,20,10))
print(in_range(24,1,25))
print(in_range(3,10,15))
print(in_range(15,1,30))
