students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
x = list()
for i in range(len(students)):
     x.append(students[i][1])
     
x = sorted(set(x))

for i in range(len(students)):
    if students[i][1] == x[1]:
        print(students[i][0])
    
     
     

 
