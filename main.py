import random
l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
l3=[1,2,3,4,5]
l4=[1,2,3,4,5]
f1,f2,f3,f4=0,0,0,0
pl=[['a',0],['b',0],['c',0],['d',0]]
hm={'a':5,'b':5,'c':5,'d':5}
ai,bi,ci,di=-1,-1,-1,-1
p1=0
for i in range(20):
    if i==19 or len(pl)==1:
        op=pl[-1][0]
        print(f"the winner is {op}")
        break
    
    if len(l1)==1:
        l1=[1,2,3,4,5]
    if len(l2)==1:
        l2=[1,2,3,4,5]
    if len(l3)==1:
        l3=[1,2,3,4,5]
    if len(l4)==1:
        l4=[1,2,3,4,5]
        
    for i in range(len(pl)):
        if f1==0:
            if pl[i][0]=='a':
                ai=i
        if f2==0:
            if pl[i][0]=='b':
                bi=i
        if f3==0:
            if pl[i][0]=='c':
                ci=i
        if f4==0:
            if pl[i][0]=='d':
                di=i
            
    st=set(l1)
    if f1==0 and ai<len(pl):
        while True:
         print(l1)
         p1=int(input("enter number within your options : "))
         if p1 in st:
             pl[ai][1]=p1
             l1.remove(p1)
             break
    else:
        print("you lost")
    
    if f2==0 and ci<len(pl):
        p2=random.choice(l2)
        l2.remove(p2)
        pl[bi][1]=p2
    if f3==0 and ci<len(pl):
        p3=random.choice(l3)
        l3.remove(p3)
        pl[ci][1]=p3
    if f4==0 and di<len(pl):
        p4=random.choice(l4)
        l4.remove(p4)
        pl[di][1]=p4
    tm={}
    for i in pl:
        if i[1] in tm:
            tm[i[1]]+=1
        else:
            tm[i[1]]=1
    sl1=[]
    sl2=[]
    
    for i in range(len(pl)):
        if tm[pl[i][1]]>1:
            sl2.append(pl[i])
        else:
            sl1.append(pl[i])
    if len(sl1)>=1:
        sl1=sorted(sl1,key=lambda x:x[1])
        
    sl1.extend(sl2)
    pl=list(sl1)
    hm[pl[-1][0]]-=1
    z=pl.pop()
    pl.insert(0,z)
    
    print(hm)

    for i in range(len(pl)):
        if f1==0:
            if pl[i][0]=='a':
                ai=i
        if f2==0:
            if pl[i][0]=='b':
                bi=i
        if f3==0:
            if pl[i][0]=='c':
                ci=i
        if f4==0:
            if pl[i][0]=='d':
                di=i
    print(pl)

    if f1==0 and ai<len(pl):
        if hm[pl[ai][0]]==0:
            pl.pop(ai)
            ai=4
            f1=1
    if f2==0 and bi<len(pl):
        if hm[pl[bi][0]]==0:
            pl.pop(bi)
            bi=4
            f2=1
    if f3==0 and ci<len(pl):
        if hm[pl[ci][0]]==0:
            pl.pop(ci)
            ci=4
            f3=1
    if f4==0 and di<len(pl):
        if hm[pl[di][0]]==0:
            pl.pop(di)
            di=4
            f4=1
