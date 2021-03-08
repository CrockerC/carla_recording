from os import listdir
import re
import cv2
import sys
from PIL import Image as image
import pickle
import numpy as np
import threading
import time
import math


class process:
    def __init__(self):
        self.num_threads = 6
        self.downscaled_size = (640, 480)
        self.sync_buff = {}
        self.threads = []
        self.batches = {}  # dictionary of paths to the batch
        self.sem = threading.Semaphore()

    def process_all(self):
        speed_path = 'processed_out\\speed' + str(vidNum) + '.txt'
        video_path = 'processed_out\\video' + str(vidNum) + '.mp4'
        frames_path = 'rawFrames'

        frame_list = listdir(frames_path)

        # sort the list by number
        frame_list = [int(f) for f in frame_list]
        frame_list = sorted(frame_list)
        frame_list = [str(f) for f in frame_list]

        speed_at_frame = []

        out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), 20, self.downscaled_size)

        # pass data to threads and get data back
        num_loops = math.ceil(len(frame_list) / self.num_threads)
        for i in range(0, num_loops*self.num_threads, self.num_threads):

            for j in range(self.num_threads):
                if i + j + 1 > len(frame_list):
                    break
                self.threads.append(threading.Thread(target=self.thread, args=(j, frames_path + '\\' + frame_list[i + j])))
                self.threads[j].start()

            for j in range(len(self.threads)):
                self.threads[j].join()

            for j in range(len(self.threads)):
                for k in range(len(self.sync_buff[j])):
                    out.write(self.sync_buff[j][k][0])
                    speed_at_frame.append(self.sync_buff[j][k][1])

            self.threads = []

        out.release()

        with open(speed_path, 'w') as f:
            frames = '\n'.join(speed_at_frame)
            f.write(frames)

    def thread(self, tid, batch):
        data = self.process_raw(batch)
        self.sem.acquire()
        self.sync_buff.update({tid: data})
        self.sem.release()

    def process_raw(self, batch):
        processed = []
        with open(batch, "br") as f:
            data = pickle.load(f)
            for frame in data:  # 0: frame name, 1: frame bytes, 2: frame resolution, 3: car speed (kph)
                speed = str(frame[3])
                png_data = image.frombytes('RGB', frame[2], frame[1], 'raw', 'BGRX')
                png_data.thumbnail(self.downscaled_size, image.ANTIALIAS)
                R, G, B = png_data.split()
                png_data = image.merge('RGB', (B, G, R))
                png_data = np.array(png_data)
                processed.append((png_data, speed))

        return processed



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

writer = process()
start = time.time()
writer.process_all()
print(time.time() - start)
