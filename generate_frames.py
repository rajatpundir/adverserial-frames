import cv2, os, shutil
import numpy as np

def generate_frames(filename):
    try:
        shutil.rmtree('frames')
    except:
        pass
    finally:
        os.mkdir('frames')
    count = 0
    vidObj = cv2.VideoCapture(filename)
    while True: 
        success, image = vidObj.read()
        if success:
            count += 1
            # Add quality flag here.
            cv2.imwrite("./frames/%d.png" % count, image)
        else:
            print(filename + ': Generated ' + str(count) + ' frames')
            break

filename = 'videoplayback.mp4'
generate_frames(filename)

# ffmpeg -framerate 25 -i image-%05d.jpg -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p output.mp4
