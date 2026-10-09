from collections import deque
process = ["P1","P2","P3","P4","P5"]
at = [3,0,2,1,4]
bt = [4,4,3,6,2]
pr = [2,0,1,1,3]

def table(title, ct):
    tat = [ct[i]-at[i] for i in range(5)]
    wt = [tat[i]-bt[i] for i in range(5)]

    print("\n", title)
    print("P AT BT PR CT TAT WT")

    for i in range(5):
        print(process[i], at[i], bt[i], pr[i], ct[i], tat[i], wt[i])

    print("Avg TAT =", sum(tat)/5)
    print("Avg WT =", sum(wt)/5)


def priority(tq):
    rem = bt.copy()
    ct = [0]*5
    q = {0: deque(), 1: deque(), 2: deque(), 3: deque()}
    added = set()
    time = done = 0

    while done < 5:

        for i in range(5):
            if i not in added and at[i] <= time:
                q[pr[i]].append(i)
                added.add(i)

        if not any(q.values()):
            time += 1
            continue

        p = min(k for k in q if q[k])
        i = q[p].popleft()

        run = min(tq, rem[i])

        for _ in range(run):
            rem[i] -= 1
            time += 1

            for j in range(5):
                if j not in added and at[j] <= time:
                    q[pr[j]].append(j)
                    added.add(j)

        if rem[i] == 0:
            ct[i] = time
            done += 1
        else:
            q[p].append(i)


    table("Priority - TQ " + str(tq), ct)


priority(1)
priority(3)