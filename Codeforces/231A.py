# Team

num_problems = int(input())
result = 0 
for _ in range (0, num_problems):
    decisions = input() 
    if decisions.count("1") >= 2: 
        result += 1
print(result)

    