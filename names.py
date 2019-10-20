import time
start_time = time.time()
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)
di = {}
for i in names_1:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1
for i in names_2:
    if i in di:
        di[i]+= 1
    else:
        di[i] = 1
for i in di:
    if di[i] > 1:
        duplicates.append(i)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

