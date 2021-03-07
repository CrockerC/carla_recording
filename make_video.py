from os import listdir
import re
import cv2
import sys
from PIL import Image as image
import pickle
import numpy as np

try:
    vidNum = int(sys.argv[1])
except IndexError:
    print("IndexError: Must give vidNum")
    sys.exit(-1)
except ValueError:
    print("ValueError: Must give integer")
    sys.exit(-1)

if vidNum < 0:
    raise TypeError("TypeError: vidNum must be a positive integer")

speed_path = 'processed_out\\speed' + str(vidNum) + '.txt'
video_path = 'processed_out\\video' + str(vidNum) + '.mp4'
frames_path = 'rawFrames'

frame_list = listdir(frames_path)

# sort the list by number
frame_list = [int(f) for f in frame_list]
frame_list = sorted(frame_list)
frame_list = [str(f) for f in frame_list]

speed_at_frame = []

downscaled_size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_path, fourcc, 20, downscaled_size)

# todo, thread and add a progress bar
for frame_batch in frame_list:
    path = frames_path + "\\" + frame_batch
    with open(path, "br") as f:
        data = pickle.load(f)
        for frame in data:  # 0: frame name, 1: frame bytes, 2: frame resolution, 3: car speed (kph)
            speed_at_frame.append(frame[3])
            png_data = image.frombytes('RGB', frame[2], frame[1], 'raw', 'BGRX')
            png_data.thumbnail(downscaled_size, image.ANTIALIAS)
            R, G, B = png_data.split()
            png_data = image.merge('RGB', (B, G, R))
            png_data = np.array(png_data)
            out.write(png_data)

with open(speed_path, 'w') as f:
    for frame in speed_at_frame:
        f.write(str(frame) + '\n')

out.release()
