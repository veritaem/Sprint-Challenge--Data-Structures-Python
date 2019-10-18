import time
start_time = time.time()
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
names = names_1 + names_2
#----RUNTIME COMPLEXITY
'''
I suspect that because it includes two for loops that both fully complete 
(ie. no chopping-up of one list like we had that one week) then i suspect this original solution is O(n^2),
where n represents a list, and the exponent representing number of lists.
'''

duplicates = []
#for name_1 in names_1:
#    for name_2 in names_2:
#        if name_1 == name_2:
#            duplicates.append(name_1)


di = {}

for i in names:
    if i in di:
        di[i] += 1
    else:
        di[i] = 1
for i in di:
    if di[i] > 1:
        duplicates.append(i)

'''
using a dictionary cuts time down significantly.  now the loop does one thing to create the dict, and then 
does one thing to append, so it should(?) be O(n) to create and O(1) to check?
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

