process = ["P1", "P2", "P3", "P4", "P5"]
at = [3, 0, 2, 1, 4]
bt = [4, 4, 3, 6, 2]
priority = [2, 6, 1, 2, 3]

ct = [8, 4, 19, 14, 16]

n = len(process)

tat = [0] * n
wt = [0] * n

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("Process AT BT Priority CT TAT WT")

for i in range(n):
    print("{:<8} {:<4} {:<4} {:<9} {:<4} {:<5}".format(
        process[i], at[i], bt[i], priority[i], ct[i], tat[i], wt[i]
    ))

avg_tat = sum(tat) / n
avg_wt = sum(wt) / n

print()
print("Average TAT =", avg_tat)
print("Average WT =", avg_wt)

print()
print("Gantt Chart:")
print("0 P2 4 P1 8 P4 14 P5 16 P3 19")
