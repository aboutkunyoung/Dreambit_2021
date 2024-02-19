from pydub import AudioSegment
import matplotlib.pyplot as plt
import scipy.fftpack
import scipy.io.wavfile
import numpy as np
import os
import shutil

def print_wavfile_info(filepath):
    wav = AudioSegment.from_wav(filepath)
    
     # 샘플레이트(44100... 24000... 8000...등)
    print("샘플레이트 : ", wav.frame_rate)
    
     # 샘플의 바이트수 1은 8비트, 2는 16비트.(비트레이트)
    print("샘플바이트 : ",  wav.sample_width*8, "bit")
    
     # 프레임의 바이트수. channel * 샘플의바이트수가 됨. 채널은 1은 모노, 2는 스테레오
    print("채널(프레임바이트) : ", int(wav.frame_width/wav.sample_width))
    print("------------------------")
    
#샘플레이트 변경(44100... 24000... 8000...등)
def wavfile_sampling_change(filepath, frame_rate):
    wav = AudioSegment.from_wav(filepath)
    wav = wav.set_frame_rate(frame_rate)
    wav.export(filepath, format='wav')
 
#비트레이트 변경
def wavfile_bitrate_change(filepath, bitrate):
    wav = AudioSegment.from_wav(filepath)
    wav = wav.set_sample_width(sample_width=bitrate)
    wav.export(filepath, format='wav')

#채널 변경(스테레오 --> 모노 변경)
def wavfile_channel_change(filepath, channel): # 1은 모노 2는 스테레오 
    wav = AudioSegment.from_wav(filepath)
    wav = wav.set_channels(channels=channel)
    wav.export(filepath, format='wav')

dir=os.getcwd()+'\\files\\'
file_list=os.listdir(dir)


print("here")
k=1
for i in file_list:
    dst=dir+i
    wav = AudioSegment.from_wav(dst)
    
    
    if wav.frame_rate == 16000 and int(wav.frame_width/wav.sample_width)==1 and (wav.sample_width*8) ==16:
        continue
    else:
        print("Not Stereo!!")
        print(dst)

    


