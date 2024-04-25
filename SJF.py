def main():
    n = int(input("Enter number of processes: "))
    processes = []

    print("Enter Burst Time:")
    for i in range(n):
        bt = int(input(f"P{i+1}: "))
        processes.append(bt)

    total_wt = total_tat = 0
    waiting_time = 0

    print("P     BT     WT     TAT")
    for i, bt in enumerate(sorted(processes)):
        wt = waiting_time
        tat = wt + bt
        print(f"P{i+1}     {bt}     {wt}      {tat}")
        total_wt += wt
        total_tat += tat
        waiting_time += bt

    avg_wt = total_wt / n
    avg_tat = total_tat / n
    print(f"Average Waiting Time= {avg_wt}")
    print(f"Average Turnaround Time= {avg_tat}")


if _name_ == "_main_":
    main()