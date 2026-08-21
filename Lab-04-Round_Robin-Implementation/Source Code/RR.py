# Round Robin (RR)

process = ["p1", "p2", "p3", "p4", "p5", "p6"]
at = [0, 1, 2, 3, 4, 4]
bt = [7, 4 , 15, 11, 20, 9]


n = len(process)


time_q = 5
rt = bt.copy()

ct = [0] * n
tat = [0] * n  
wt = [0] * n  
current_time = 0 

queue = []
visited = [False] * n

for i in range(n):
    if at[i] <= current_time and visited[i] == False:
        queue.append(i)
        visited[i] = True


while len(queue) > 0: 
    i = queue.pop(0)

    if rt[i] > time_q:
        current_time += time_q
        rt[i] -= time_q


    else:
        current_time += rt[i]
        rt[i] = 0
        ct[i] = current_time

    for j in range(n):
        if at[j] <= current_time and visited[j] == False:
            queue.append(j)
            visited[j] = True


    if rt[i] > 0:
        queue.append(i)

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("Process\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(process[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])


rr_avg_tat = sum(tat)/n
rr_avg_wt = sum(wt)/n

print("\nAverage TAT =", rr_avg_tat)
print("Average WT =", rr_avg_wt)
print()

# Shortest Job First

process = ["p1", "p2", "p3", "p4", "p5", "p6"]
at = [0, 1, 2, 3, 4, 4]
bt = [7, 4 , 15, 11, 20, 9]

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
print()

# First Come First Serve(FCFS)
lst = [
    ["P1",0,7],
    ["p2",1,4],
    ["p3",2,15],
    ["p4",3,11],
    ["p5",4,20],
    ["p6",4,9]
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

fcfs_avg_tat = sum(tat)/n
fcfs_avg_wt = sum(wt)/n
print("Average Tranaround time: ",fcfs_avg_tat)
print("Average Waiting time: ", fcfs_avg_wt)

print()


if rr_avg_tat < sjf_avg_tat and rr_avg_tat < fcfs_avg_tat:
    print("Round Robin is better TAT.")
elif sjf_avg_tat < rr_avg_tat and sjf_avg_tat < fcfs_avg_tat:
    print("Shortest Job First is better TAT.")
else:
    print("FCFS is better TAT.")



if rr_avg_wt < sjf_avg_wt and rr_avg_wt < fcfs_avg_wt:
    print("Round Robin is better WT.")
elif sjf_avg_wt < rr_avg_wt and sjf_avg_wt < fcfs_avg_wt:
    print("Shortest Job First is better WT.")
else:
    print("FCFS is better WT.")

