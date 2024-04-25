def avg_wt(proc,bt,q):
	rt,t,tw,tt,n=list(bt),0,0,0,len(proc)
	while any (rt):
		for i,b in enumerate(rt):
			if b>0:
				p=min(q,b)
				t+=p
				tw+=t-p
				tt+=t
				rt[i]-=p
				return tw/n,tt/n

if _name=="main_":
			p=[2,4,5]
			bt=[4,6,7]
			q=4
			awt,atat=avg_wt(p,bt,q)
			print(f"Average waiting time={awt}")
			print(f"Average turn around time={atat}")