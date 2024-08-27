import pandas as pd
import os
import shutil

df = pd.read_excel('0. 파일명 정리.xlsx')

copath= 'E:\\3. 외국인 한국어 발화\\EN 선 수집 데이터\\검수완료\\10000개\\실제업로드용\\new-10544'#저장될 위치
#error_list=[]

for i in range((df.shape)[0]):#전체 데이터 셋 만큼 돌기
    src=os.path.join(df.iloc[i, 0], df.iloc[i, 1])#('폴더위치', '파일명') 에 접근
    dst=str(df.iloc[i, 2])#바꾸고자 하는 이름
    
    fpath=(df.iloc[i, 0]).split('\\')[-2]
    if not os.path.exists(copath+'\\'+fpath):
        os.mkdir(copath+'\\'+fpath)
        
    shutil.copy2(src, copath+'\\'+fpath)    
        
    dst=str(df.iloc[i, 2])#바꾸고자 하는 이름
    dst=os.path.join(copath+'\\'+fpath, dst)
    try:
        os.rename(copath+'\\'+fpath+'\\'+df.iloc[i, 1], dst)    
    except:
        print("Error!")
        #errpr_list.append('copath')
