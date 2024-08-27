import os
import shutil
import pandas as pd
import openpyxl

pathdata = pd.read_excel('불가처리로 업로드 제외 건.xlsx', engine = 'openpyxl')
coPath = os.getcwd() +'\\error from results'

fName = []

usefile = []
no = 0
fcnt = 0

fnot = []

for pa in pathdata['fileName']:
    fName.append(pa)

oriPath =os.getcwd() +'\\results'


for (path, dir, files) in os.walk(oriPath):
    for filename in files:
        ext = os.path.splitext(filename)[-1]

        if ext == '.wav':
            if filename in fName:
                if fcnt < len(fName)+1:
                    fcnt = fcnt+1

                    opth = path+'\\'+filename
                    
                    try:
                        shutil.move(opth, coPath)
                        no = no + 1

                        #usefile.append([no, filename, opth])
                        print(no,filename)
                    except:
                        fnot.append(opth)
                        continue
                else:
                    break


#usefile = pd.DataFrame(usefile)
#usefile.to_excel(excel_writer='usefile csv.xlsx')    

if len(fnot) > 0:
    fnot = pd.DataFrame(fnot)
    fnot.to_excel(excel_writer='nofile csv.xlsx')

