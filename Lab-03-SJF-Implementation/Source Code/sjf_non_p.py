# Shortest Job First (SJF)

process = ["p1", "p2", "p3", "p4", "p5"]
at = [3, 2, 5, 1, 6]
bt = [3, 5, 4, 3, 2]

n = len(process)

ct = [0] * n
wt = [0] * n
done = [0] * n
tat = [0] * n

time = 0
completed = 0

while completed < n:

    x = -1
    for i in range(n):

        if at[i] <= time and done[i] == 0:

            if x == -1 or bt[i] < bt[x]:
                x = i

    if x == -1:
        time += 1

    else:
        time = time + bt[x]

        ct[x] = time
        done[x] = 1
        completed += 1


for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]


print("Process\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(process[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])

sjf_avg_tat = sum(tat)/n
sjf_avg_wt = sum(wt)/n

print("\nAverage TAT =", sjf_avg_tat)
print("Average WT =", sjf_avg_wt)
print("\n")

# First Come First Serve(FCFS)
lst = [
    ["P1",3,3],
    ["p2",2,5],
    ["p3",5,4],
    ["p4",1,3],
    ["p5",6,2]
]

lst.sort(key=lambda x: x[1])


ct = []
tat = []
wt = []

time = 0

for i in lst:
    name, at, bt = i

    if time < at + 1 :
        time = at 

    time += bt
    ct.append(time)

    turnaround = time - at
    tat.append(turnaround)

    waiting = turnaround - bt
    wt.append(waiting)

print("P_id\t AT\t BT \t CT \t TAT \t WT")

for i in range(len(lst)):
    print(lst[i][0], "\t",
          lst[i][1], "\t",
          lst[i][2], "\t",
          ct[i], "\t",
          tat[i], "\t",
          wt[i], "\t")
print()
avg_tat = sum(tat) / len(tat)
print("Average Tranaround time: ",avg_tat)

avg_wt = sum(wt)/ len(wt)
print("Average Waiting time: ", avg_wt)

print("\n")

if sjf_avg_tat < avg_tat:
    print("SJF is better TAT then FCFS")

else:
    print("FCFS is better TAT then SJF")
    
if sjf_avg_wt < avg_wt:
    print("SJF is better WT then FCFS")
    
else:
    print("FCFS is better WT then SJF")
