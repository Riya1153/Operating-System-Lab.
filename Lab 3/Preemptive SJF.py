process = ["p1", "p2", "p3", "p4"]
at = [0,1,3,2]
bt = [4,2,2,1]

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

            if x == -1 or remaining[i] < remaining[x]:
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



if p_avg_tat < p_avg_tat :
    print ("Preemptive TAT is best.")
else:
    print("Preemptive TAT is best")

if p_avg_wt < p_avg_wt :
    print ("Preemptive WT is best.")
else:
    print("Preemptive WT is best")
