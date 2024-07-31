def common(list1, list2):
    common_mem = []
    for member in list1:
        if member in list2:
            common_mem.append(member)
    if common_mem:
        return True, common_mem
    else:
        return False

list1 = [22, 25, 15, 24, 16, 45]
list2 = [14, 18, 16, 10, 17, 50]

print(common(list1, list2)) 
