# Q.46]  Write a Python function that checks whether a passed string is palindrome or not 



def palindrome(s):
    normal_str = s.replace(" ","").lower()

    return normal_str == normal_str[::-1]

user = input("Enter a string to check its palindrome or not: ")
print("Given string is palindrome : ",palindrome(user))
