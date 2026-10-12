req = [3, 60, 10, 25, 30, 4]
head = 41
n = len(req)

done = [0] * n
current = head
total_movement = 0
seq = [current]

for i in range(n):
    x = -1

    min_distance = 9999

    for j in range(n):
        if done[j] == 0:
            dist = abs(req[j] - current)

            if dist < min_distance:
                min_distance  = dist
                x = j

    movement = min_distance


    print(f"{current} -> {req[x]} = {movement}")

    total_movement += movement
    current = req[x]
    seq.append(current)
    done[x] = 1

print("Total Movement: ", total_movement)
print("Sequence" , seq)
print()

# FCFS disk Schedulig

req = [3, 60, 10, 25, 30, 4]
head = 41

total_m = 0
current = head
seq = [current]


for req in req:
    movement = abs(req - current)
    print(f"{current} -> {req} = {movement}")

    total_m += movement
    current =  req

print("Total movement: ", total_m)
