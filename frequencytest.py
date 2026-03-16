number = input("enter the numbers by user : ")
user_list = number.split()
count = {}

for p in user_list:
    if p in count:
        count[p] = count[p] + 1
    else:  
        count[p] = 1

print("top three no to print: ")
for i in range(3):
    if len(count) == 0: 
        break
        
    high = None
    reapeat = -1

    for p in count:
        if count[p] > reapeat:
            reapeat= count[p]
            high = p
            
    if high is not None:
        print(f"{high} -- {reapeat} times")
        del count[high]