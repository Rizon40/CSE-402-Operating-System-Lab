lst = [
    ["P0",3,1],
    ["p1",5,3],
    ["p2",2,2],
    ["p3",1,2],
    ["p4",6,3]
]

lst.sort(key=lambda x:x[1])

ct = []
tat = []
wt = []
current_time = 0

for i in lst:
    name, at, bt = i

    if current_time < at :
        current_time = at 

    current_time += bt
    ct.append(current_time)

    turnaround = current_time - at
    tat.append(turnaround)

    waiting = turnaround - bt
    wt.append(waiting)

print("P_id\tAT\tBT\tCT\tTAT\tWT")

for i in range(len(lst)):
    print(lst[i][0], "\t",
          lst[i][1], "\t",
          lst[i][2], "\t",
          ct[i], "\t",
          tat[i], "\t",
          wt[i], "\t")

avg_tat = sum(tat) / len(tat)
print("Average Turnaround time: ",avg_tat)
avg_wt = sum(wt)/ len(wt)
print("Average Waiting time: ", avg_wt)



