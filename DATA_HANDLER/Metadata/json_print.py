import os
import json
from collections import OrderedDict
import pathlib
import openpyxl

b = openpyxl.load_workbook('0. 메타데이터 정보 정리.xlsx')
sh = b.worksheets[0]

nrow = 0
outp = []

copath = 'E:\\3. 외국인 한국어 발화\\EN 선 수집 데이터\\검수완료\\10000개\\실제업로드용\json\\'

for row in sh.rows:
    if nrow == 0:
        nrow += 1
        continue

    try:
        #folder = row[1].value #폴더분리 저장 위한 경로
        
        fileName = row[2].value #speacker column 은 지우기!!!
        speakerID = row[3].value
        sentenceID = row[4].value
        recordUnit = row[5].value
        recordQuality = row[6].value
        recordDate = row[7].value
        recordTime = round(row[8].value, 2)

        Reading = ""
        ReadingLabelText = ""
        Question = row[9].value
        AnswerLabelText = row[10].value
        SentenceSpeechLV = row[11].value

        gender = row[12].value
        birthYear = row[13].value
        eduBackground = row[14].value

        country = row[15].value
        residencePeriod = row[16].value
        residenceCity = row[17].value

        languageClass = row[18].value
        motherTongue = row[19].value
        selfAssessment = row[20].value
        topikGrade = row[21].value
        LearningPeriod = row[22].value
        learningSource = row[23].value
        
    except:
        print(nrow,' err')
        continue

    dataDict = OrderedDict()

    dataDict["fileName"] = fileName+".wav"
    dataDict["file_info"] = {
        'speakerID': speakerID,
        'sentenceID': sentenceID,
        'recordUnit': recordUnit,
        'recordQuality': recordQuality,
        'recordDate': recordDate,
        'recordTime': str(recordTime)
    }
    dataDict["transcription"] = {
        'Reading': Reading,
        'ReadingLabelText': ReadingLabelText,
        'Question': Question,
        'AnswerLabelText': AnswerLabelText,
        'SentenceSpeechLV': SentenceSpeechLV
    }
    dataDict["SpeakerID"] = speakerID
    dataDict["basic_info"] = {
        'gender': gender,
        'birthYear': str(birthYear),
        'eduBackground': eduBackground
    }
    dataDict["residence_info"] = {
        'country': country,
        'residencePeriod': residencePeriod,
        'residenceCity': residenceCity
    }
    dataDict["skill_info"] = {
        'languageClass': languageClass,
        'motherTongue': motherTongue,
        'selfAssessment': selfAssessment,
        'topikGrade': topikGrade,
        'LearningPeriod': str(LearningPeriod),
        'learningSource': learningSource
    }

    jsonName = fileName+".json"

    #if not os.path.isdir(copath+folder):
    #    os.mkdir(copath+folder)    #폴더 생성
    with open(os.path.join(copath, jsonName), 'w', encoding="utf=8") as make_file:
        json.dump(dataDict, make_file, ensure_ascii=False, indent='\t')

    nrow += 1
'''
    outp.append([folderName, txtName, txtCon])

for tx in outp:
    if not os.path.isdir(copath+tx[0]):
        os.mkdir(copath+tx[0])

    txtf = open(copath+tx[0]+'\\'+tx[1], 'w', encoding='utf-8')
    txtf.write(tx[2])
    txtf.close()
'''
