process = ["P1", "P2", "P3", "P4", "P5"]
at = [2, 3, 0, 1, 1]
bt = [5, 1, 2, 3, 6]

n = len(process)

ct = [0] * n
tat = [0] * n
wt = [0] * n
done = [0] * n

time = 0
completed = 0

while completed < n:
    x = -1

    for i in range(n):
        if at[i] <= time and done[i] == 0:
            if x == -1 or bt[i] < bt[x]:
                x = i

    if x == -1:
        time = time + 1
    else:
        time = time + bt[x]
        ct[x] = time
        done[x] = 1
        completed = completed + 1

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("SJF RESULT")
print(f"{'Process':<10}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")

for i in range(n):
    print(f"{process[i]:<10}{at[i]:<6}{bt[i]:<6}{ct[i]:<6}{tat[i]:<6}{wt[i]:<6}")

sjf_avg_tat = sum(tat) / n
sjf_avg_wt = sum(wt) / n

print()
print("Average TAT =", sjf_avg_tat)
print("Average WT =", sjf_avg_wt)

print()
print()


# FCFS
processes = [
    ["P1", 2, 5],
    ["P2", 3, 1],
    ["P3", 0, 2],
    ["P4", 1, 3],
    ["P5", 1, 6]
]

processes.sort(key=lambda x: x[1])

time = 0
total_tat = 0
total_wt = 0

print("FCFS RESULT")
print(f"{'Process':<10}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")

for p in processes:
    pid = p[0]
    arrival = p[1]
    burst = p[2]

    if time < arrival:
        time = arrival

    time = time + burst
    completion = time
    turnaround = completion - arrival
    waiting = turnaround - burst

    total_tat = total_tat + turnaround
    total_wt = total_wt + waiting

    print(f"{pid:<10}{arrival:<6}{burst:<6}{completion:<6}{turnaround:<6}{waiting:<6}")

fcfs_avg_tat = total_tat / len(processes)
fcfs_avg_wt = total_wt / len(processes)

print()
print("Average TAT =", fcfs_avg_tat)
print("Average WT =", fcfs_avg_wt)

print()
print()


if sjf_avg_tat < fcfs_avg_tat:
    print("SJF is better TAT than FCFS")
else:
    print("FCFS is better TAT than SJF")

if sjf_avg_wt < fcfs_avg_wt:
    print("SJF is better WT than FCFS")
else:
    print("FCFS is better WT than SJF")
