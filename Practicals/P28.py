# Q.28}  Write a Python script to sort (ascending and descending) a dictionary by value. 

days = {'tuesday':3, 'sunday':1, 'monday':2}

asc_dic = dict(sorted(days.items(), key=lambda item: item[1]))

desc_dic = dict(sorted(days.items(), key = lambda item: item[1],reverse=True))

print("Dictionary with ascending order: ")
print(asc_dic)

print("\nDictionary with descending order: ")
print(desc_dic)