t=int(input())
for _ in range(t):
    s=input()
    aa={}
    i=0
    j=0
    ans=0
    for k in s:
        if(k=="N"):
            try:
                x=aa[((i,j),(i,j-1))]
                ans+=1
            except:
                ans+=5
                aa[((i,j),(i,j-1))]=1
            j-=1
                
        elif(k=="E"):
            try:
                x=aa[((i+1,j),(i,j))]
                ans+=1
            except:
                ans+=5
                aa[((i+1,j),(i,j))]=1
            i+=1
        elif(k=="W"):
            try:
                x=aa[((i,j),(i-1,j))]
                ans+=1
            except:
                ans+=5
                aa[((i,j),(i-1,j))]=1
            i-=1
        else:
            try:
                x=aa[((i,j+1),(i,j))]
                ans+=1
            except:
                ans+=5
                aa[((i,j+1),(i,j))]=1
            j+=1
    print(ans)
    
            
        
         
    

