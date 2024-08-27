import os
import shutil
import pandas as pd
import openpyxl

usefile = []
no = 0
fnot = []

oriPath = os.getcwd()+'\\results'    #파일 불러올 경로

coPath = r'C:\Users\pc\Desktop\VAD 돌리기\split_results'  #복사될 위치


for (path, dir, files) in os.walk(oriPath):
    for filename in files:
        ext = os.path.splitext(filename)[-1]    #확장자 분리

        opth = path+'\\'+filename	#파일 원래 위치

        chName1 = os.path.splitext(filename)[0]
        chName2 = chName1.split('_')
        stID = chName2[0]
        #filename 스크립트ID 분리

        langu = stID[0:2]
        if langu=="VN":    langu="1. 베트남어"
        elif langu=="EN":    langu="2. 영어"
        elif langu=="JP":    langu="3. 일본어"
        elif langu=="CN":    langu="4. 중국어"
        elif langu=="TH":    langu="5. 태국어"
        elif langu=="EX":    langu="6. 기타"
        #언어분류
        
        cate = stID[2]
        if cate=="1": cate="1. 한국일반"
        elif cate=="2": cate="2. 한국생활l"
        elif cate=="3": cate="3. 한국생활ll"
        elif cate=="4": cate="4. 한국문화l"
        elif cate=="5": cate="5. 한국문화ll"
        #스크립트 카테고리

        if ext=='.wav':
            dp1 = "대본읽기 음성데이터"

            savefolder = "\\".join([coPath,langu,cate,dp1])
        elif ext=='.csv' or ext=='.json':
            dp1 = "대본읽기 메타데이터"        

            if ext=='.csv': dp2 = "csv"
            elif ext=='.json':  dp2 = "json"            
            savefolder = "\\".join([coPath,langu,cate,dp1,dp2])
        #확장자


        if not os.path.exists(savefolder):
            os.makedirs(savefolder)
        # 복사할 위치에 savefolder의 폴더 없을때 생성


        savepath = savefolder+'\\'+filename
        try:
            shutil.copy2(opth, savepath)

            no = no + 1
            usefile.append([filename,ext,stID,langu,cate,savefolder])

            print(no,filename,'\t',savefolder)
        except:
            fnot.append(opth)
            continue


usefile = pd.DataFrame(usefile)
usefile.to_excel(excel_writer='folderMK copy filelist.xlsx')    

if len(fnot) is not 0:
    fnot = pd.DataFrame(fnot)
    fnot.to_excel(excel_writer='nofile.xlsx')

