# Priority Non-Preemptive

process = ["p1", "p2", "p3", "p4", "p5"]
at = [0,1,2,3,5]
bt = [3,4,6,4,2]
priority = [3,2,4,6,10]

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

            if x == -1 or priority[i] < priority[x]:
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

non_P_avg_tat = sum(tat)/n
non_p_avg_wt = sum(wt)/n

print("\nAverage TAT =", non_P_avg_tat)
print("Average WT =", non_p_avg_wt)
print("\n")


# Priority Preemptive

process = ["p1", "p2", "p3", "p4", "p5"]
at = [0,1,2,3,5]
bt = [3,4,6,4,2]
priority = [3,2,4,6,10]


n = len(process)

ct = [0] * n
wt = [0] * n
tat = [0] * n

tq= 1
remaining = bt.copy()
time = 0
completed = 0

while completed < n:

    x = -1
    for i in range(n):

        if at[i] <= time and remaining[i] > 0:

            if x == -1 or priority[i] < priority[x]:
                x = i

    if x == -1:
        time += 1

    else:
        if remaining[x] > tq:
            time += tq
            remaining[x] -= tq

        else:
            time += remaining[x]
            remaining[x] = 0
            ct[x] = time
            completed += 1


for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]


print("Process\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(process[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])

p_avg_tat = sum(tat)/n
p_avg_wt = sum(wt)/n

print("\nAverage TAT =", p_avg_tat)
print("Average WT =", p_avg_wt)
print("\n")



if non_P_avg_tat < p_avg_tat :
    print ("Non Preemptive Priority TAT is best.")
else:
    print("Preemptive Priority TAT is best")

if non_p_avg_wt < p_avg_wt :
    print ("Non Preemptive Priority WT is best.")
else:
    print("Preemptive Priority WT is best")
