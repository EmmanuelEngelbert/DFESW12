x=range(1500,2700,1)

for i in x:
    if i%5 == 0 and i%7 == 0:
        print(i)
    else: 
        continue