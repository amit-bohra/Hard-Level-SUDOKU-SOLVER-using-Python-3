import numpy as np
import random as rd
import time
from copy import deepcopy as dp
#mat=np.array([0,0,0,0,5,0,0,4,0,0,0,6,7,4,1,2,8,5,4,8,0,9,0,0,0,0,6,2,0,0,0,6,0,0,0,0,0,9,8,1,0,2,5,6,0,0,0,0,0,9,0,0,0,7,3,0,0,0,0,9,0,1,2,8,7,2,3,1,6,4,0,0,0,1,0,0,7,0,0,0,0],dtype='int64')
#mat=np.array([0,1,0,0,0,0,0,0,6,0,5,0,4,8,0,2,1,0,0,3,0,0,0,7,0,0,5,0,0,0,0,0,4,6,0,9,2,0,0,0,5,0,0,0,4,6,0,4,9,0,0,0,0,0,5,0,0,6,0,0,4,8,0,8,4,0,0,3,2,0,0,0,0,0,0,0,0,0,0,5,0],dtype='int64')
#mat=np.array([7,2,5,0,0,0,0,0,4,0,0,0,3,0,0,0,5,2,0,0,0,0,2,0,1,8,0,0,8,0,0,0,9,0,0,3,0,0,2,0,0,0,9,0,0,4,0,0,6,0,0,0,1,0,0,7,3,0,8,0,0,0,0,1,5,0,0,0,4,0,0,0,9,0,0,0,0,0,2,7,5,],dtype='int64')
mat=np.array([0,0,1,0,4,0,2,7,0,0,0,0,7,0,0,5,0,3,0,9,5,0,0,2,0,0,0,9,0,0,0,0,4,0,8,0,0,0,8,0,0,0,9,0,0,0,7,0,8,0,0,0,0,1,0,0,0,3,0,0,8,2,0,8,0,7,0,0,1,0,0,0,0,5,4,0,6,0,1,0,0],dtype='int64')
#mat=np.array([],dtype='int64')  #Provide the INPUT with 1D list of values and "0" implying 'Empty Space'
mat=mat.reshape((9,9))
possible=np.zeros((9,9),dtype='int64').tolist()
row_dicty={}
valist=[1,2,3,4,5,6,7,8,9]
rflag=0
score=0
count=0
box={}
ax=0
bx=3
ay=0
by=3
boxrange={}
while True:
    listy=[(x,y) for x in range(ax,bx) for y in range(ay,by)]
    count+=1
    box[count]=listy
    boxrange[count]=[ax,bx,ay,by]
    ay+=3
    by+=3
    if by>9:
        ay=0
        by=3
        ax+=3
        bx+=3
    if bx>9:
        break
boxrow={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
boxcol={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
for kr,vr in boxrange.items():
    l,g,b,t=vr
    tmpr=[]
    tmpc=[]
    for a in range(l,g):
        tmpr.append(a)
    boxrow[kr]=(tmpr)
    for n in range(b,t):
        tmpc.append(n)
    boxcol[kr]=(tmpc)
    
box_num=0
leftbox=[]
leftrow=[]
leftcol=[]
box_vals={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
print(mat)
running=True
adj_box={1:[[2,3],[4,7]],2:[[1,3],[5,8]],3:[[1,2],[6,9]],4:[[5,6],[1,7]],5:[[4,6],[2,8]],6:[[4,5],[3,9]],7:[[8,9],[1,4]],8:[[7,9],[2,5]],9:[[7,8],[3,6]]}
while(running):
    epoc=0
    possible=dp(mat)
    possible=possible.tolist()
    for h in range(1,10):
        lx,hx,ly,hy=boxrange[h]
        tmat=mat[lx:hx,ly:hy]
        tempo=tmat[mat[lx:hx,ly:hy].nonzero()].tolist()
        tempo=[x for x in tempo if x!=0]
        box_vals[h]=tempo
    q=list(mat.nonzero())
    r=list(map(lambda x,y:(x,y),q[0],q[1]))
    for i in range(9):
        for j in range(9):
            score=0
            if (i,j) in r:
                continue
            if (i,j) not in r:
                score+=1
            for key,vals in box.items():
                if (i,j) in vals:
                    box_num=key
                    break
            leftbox=frozenset(valist)-frozenset(box_vals[box_num])
            leftcol=frozenset(valist)-frozenset(mat[:,j])
            leftrow=frozenset(valist)-frozenset(mat[i,:])
            temp=list(leftbox.intersection(leftcol,leftrow))
            possible[i][j]=temp
            #print('boxings',box_num)
            for put in temp:
                rowlisty=boxrow[box_num]
                collisty= boxcol[box_num]
                norow=[x for x in rowlisty if x!=i]
                dflag=0
                rflag=0
                cflag=0
                '''print('i and j',i,j)
                print('putty',put)'''
                for lr in rowlisty:
                    for lc in collisty:
                        if mat[lr,lc]!=0:
                            dflag+=1
                        else:
                            if lr==i and lc==j:
                                continue
                            elif lr==i and lc!=j:
                                if put in mat[:,lc]:
                                    cflag+=1
                            elif lr!=i and lc==j:
                                if put in mat[lr,:]:
                                    rflag+=1
                            else:
                                if put in mat[lr,:]:
                                    rflag+=1
                                elif put in mat[:,lc]:
                                    cflag+=1
                        '''print('lc',lc)
                        print('lr',lr)
                        print('dflag',dflag)
                        print('rflag',rflag)
                        print('cflag',cflag)'''
                if dflag+cflag+rflag==8:
                    score+=1
                    dflag=0
                    rflag=0
                    cflag=0
                    break
                else:
                    dflag=0
                    rflag=0
                    cflag=0
            if score>=2:
                score=0
                '''print('box_num',box_num)
                print('ij',i,j)
                print('leftbox',leftbox)
                print('box',box_vals[box_num])
                print('leftcol',leftcol)
                print('col',mat[:,j])
                print('leftrow',leftrow)
                print('row',mat[i,:])
                print('temp',temp)
                print('put',put)'''
                mat[i][j]=put
                epoc=1
                #print(mat)
        score=0
        if len(r)==81:
            running=False
            
    if epoc==0:
        for i in range(9):
            semirow=[]
            dustyrow=[]
            for j in range(9):
                if isinstance(possible[i][j], list):
                    semirow.append([[i,j],possible[i][j]])
            for a in range(len(semirow)):
                dustyrow.extend(semirow[a][1])
            dustyrow=[x for x in dustyrow if dustyrow.count(x)==1]
            if len(dustyrow)>0:
                ind=[x[0] for x in semirow if dustyrow[0] in x[1]]
                mat[ind[0][0]][ind[0][1]]=dustyrow[0]

        for i in range(9):
            semicol=[]
            dustycol=[]
            for j in range(9):
                if isinstance(possible[j][i], list):
                    semicol.append([[j,i],possible[j][i]])
            for a in range(len(semicol)):
                dustycol.extend(semicol[a][1])
            dustycol=[x for x in dustycol if dustycol.count(x)==1]
            if len(dustycol)>0:
                ind=[x[0] for x in semicol if dustycol[0] in x[1]]
                mat[ind[0][0]][ind[0][1]]=dustycol[0]
                
        for i in range(1,10):
            semibox=[]
            dustybox=[]
            for j,l in box[i]:
                if isinstance(possible[j][l], list):
                    semicol.append([[j,l],possible[j][l]])
            for a in range(len(semicol)):
                dustybox.extend(semicol[a][1])
            dustybox=[x for x in dustybox if dustybox.count(x)==1]
            if len(dustybox)>0:
                ind=[x[0] for x in semibox if dustybox[0] in x[1]]
                mat[ind[0][0]][ind[0][1]]=dustybox[0]
                    
print()
print(mat)
print()
for i in range(9):
    print('rowsum {}'.format(i),sum(mat[i,:]))
    print('colsum {}'.format(i),sum(mat[:,i]))
        
        





















#Expert Level mat=np.array([3,0,0,0,5,2,8,7,0,0,0,0,6,0,0,4,0,1,0,0,0,0,0,0,6,5,2,0,2,0,0,0,6,0,0,0,0,0,7,0,8,0,3,0,0,0,0,0,2,0,0,0,9,0,5,3,8,0,0,0,0,0,0,4,0,6,0,0,5,0,0,0,0,9,2,7,3,0,0,0,8],dtype='int64')
