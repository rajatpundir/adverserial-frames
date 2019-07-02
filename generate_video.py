import cv2, os, shutil
import numpy as np

def convert_frames_to_video(filename = './video.avi', fps = 25.0):
    files = [f for f in os.listdir('./frames/') if os.path.isfile(os.path.join('./frames/', f))]
    files_num = []
    for f in files:
        files_num.append(int(f.split('.')[0]))
    files_num = sorted(files_num)
    files = files_num
    frame_array = []
    for i in range(len(files)):
        filename = './frames/' + str(files[i]) + '.jpg'
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        frame_array.append(img)
    print(len(frame_array))
    out = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
    print('Success')

convert_frames_to_video()
