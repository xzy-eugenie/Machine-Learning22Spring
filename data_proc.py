import pandas as pd
import numpy as np

lst = []

with open('log.txt', 'r') as f:
    tmp = []
    num = 0 
    line = f.readline()
    while line:
        #line = line.strip('\n')
        line = line.split(' ')
        if not num % 7:
            if len(tmp)>0:
                lst.append(tmp)
            tmp = []
            tmp.append(int(line[0]))
            tmp.append(float(line[1]))
            if len(line) == 2:
                tmp.append(1e-3)
            else:
                tmp.append(float(line[2]))
        else:
            tmp.append(float(line[1]))
        num += 1
        line = f.readline()
df = pd.DataFrame(lst, columns=['num', 'lamda', 'beta','L1','L2','L_inf','psnr','L0','asr'])
def solve(x):
    mysum = sum(x['num'])
    l0 = round(sum(x['L0']*x['num'])/mysum,1)
    l1 = round(sum(x['L1']*x['num'])/mysum,3)
    l2 = round(sum(x['L2']*x['num'])/mysum,3)
    l_inf = round(sum(x['L_inf']*x['num'])/mysum, 3)
    psnr = round(sum(x['psnr']*x['num'])/mysum, 3)
    return [l0,l1,l2,l_inf,psnr]
data = df.groupby(['beta','lamda']).apply(solve)
print(data)
data.to_csv('data.csv')
