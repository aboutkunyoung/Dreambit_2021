import os
import shutil
import pandas as pd
import openpyxl

coPath = 'C:\\Users\\pc\\Desktop\\VAD연습\\files'



file_list=os.listdir('C:\\Users\\pc\\Desktop\\159999 VAD 돌리기\\files')


cnt=0

errorList=[]

for file in file_list:
    src='C:\\Users\\pc\\Desktop\\159999 VAD 돌리기\\files\\'+file




    
    shutil.move(src, coPath)
    cnt+=1
    
        #print('error')
        #errorList.append(file)

    if cnt%100==0 or cnt==68664:
        print(cnt)
        
    if cnt==68664:
        break
    
