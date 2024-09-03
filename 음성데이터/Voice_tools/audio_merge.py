import wave

infiles = ["silent0.5sec.wav", "EN_F_3_R_S1-1_001.wav"]
outfile = "sounds.wav"


data= []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
output = wave.open(outfile, 'wb')

output.setparams(data[0][0])
output.writeframes(data[0][1])#무음
output.writeframes(data[1][1])#본 파일
output.writeframes(data[0][1])#무음
output.close()
