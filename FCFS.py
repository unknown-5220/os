def findwaitingtime(processes,n,bt,wt):
    wt[0]=0
    for i in range(1,n):
        wt[i]=bt[i-1]+wt[i-1]

def findturnaroundtime(processes,n,bt,wt,tat):
    for i in range(n):
        tat[i]=bt[i]+tat[i]
def findaveragetime(processes,n,bt):
    wt=[0]*n
    tat=[0]*n
    total_wt=0
    total_tat=0
    
    findwaitingtime(processes,n,bt,wt)
    findturnaroundtime(processes,n,bt,wt,tat)
    
    print("processes bt "+"wt "+"tat")
    
    for i in range(n):
        total_wt=total_wt+wt[i]
        total_tat=total_tat+tat[i]
        print(""+str(i+1)+"\t\t"+
                 str(bt[1])+"\t"+
                 str(wt[i])+"\t\t"+
                 str(tat[i]))
        print("average wt= "+ str(total_wt/n))
        print("average tat= "+ str(total_tat/n))
        
if _name_ == "_main_":       
    processes=[1,3,5]
    n=len(processes)
    
    burst_time=[2,5,9]
    
    findaveragetime(processes,n,burst_time)