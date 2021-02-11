from os import listdir
import re
import cv2
import sys

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
frames_path = '_out'

frame_list = listdir(frames_path)
speed_at_frame = []

for frame in frame_list:
    pattern = '(?<=-).*(?=\.)'
    match = re.search(pattern, frame)
    speed_at_frame.append(float(match.group(0)))

with open(speed_path, 'w') as f:
    for frame in speed_at_frame:
        f.write(str(frame) + '\n')

frame = cv2.imread(frames_path + '\\' + frame_list[0])
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(video_path, fourcc, 20, (width, height))

for name in frame_list:
    frame = cv2.imread(frames_path + '\\' + name)
    out.write(frame)

out.release()
