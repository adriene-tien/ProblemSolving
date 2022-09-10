# Boy or Girl

# number of distinct characters is odd: male 
# otherwise: female 

num_distinct_chars = 0 
username = input() 
dict = {}
for i in username: 
    if i not in dict: 
        num_distinct_chars += 1 
        dict[i] = 1
if num_distinct_chars % 2 == 0: 
    print("CHAT WITH HER!") 
else: 
    print("IGNORE HIM!")
    
