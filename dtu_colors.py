primary = {'red':[153,0,0], 'grey':[153,153,153]} 
secondary = [[255,153,0],[255,102,0],[255,0,0],[153,0,0],[255,0,153],
             [204,51,153],[153,0,102],[102,0,102],[102,0,153],[51,204,255],
             [153,204,51],[255,204,0],[51,102,204],[102,204,0]]
idx = [11,0,1,2,3,4,5,6,7,8,12,9,10,13]

for v in primary.values():
    v[0]/=255.
    v[1]/=255.
    v[2]/=255.

for v in secondary:
    v[0]/=255.
    v[1]/=255.
    v[2]/=255.

def lines(n):
    di = (len(idx)+1)//n
    return [secondary[i] for i in idx[::di][:n]]
    

#print primary
#print secondary

