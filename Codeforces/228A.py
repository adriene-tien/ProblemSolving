# Is your horseshoe on the other hoof? 

horseshoes = input().split(" ") # [1, 7, 3, 3]
dict = {} # maximum 4 entries 
result = 0 
for i in horseshoes: 
    if i in dict: 
        result += 1 
    else: 
        dict[i] = 1 
print(result)
