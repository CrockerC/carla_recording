from os import listdir, path
import os
import sys
from PIL import Image as image
import pickle
import numpy as np
import threading
import time
import math
import cv2


# todo, write to the video while processing new frames

class process:
    def __init__(self):
        self.num_threads = 6
        self.downscaled_size = (640, 480)  # resolution of the final video
        self.sync_buff = {}
        self.threads = []
        self.batches = {}  # dictionary of paths to the batch
        self.out = None
        self.speed_at_frame = []
        self.write_thread = None
        self.framerate = 20

        self.writing_done = threading.Event()

    def process_all(self):
        speed_path = 'processed_out\\speed' + str(vidNum) + '.txt'
        video_path = 'processed_out\\video' + str(vidNum) + '.mp4'
        frames_path = 'rawFrames'

        if path.exists(video_path):
            raise FileExistsError("Error this video already exists! Please pick another video number!")

        frame_list = listdir(frames_path)

        # sort the list by number value
        frame_list = [int(f) for f in frame_list]
        frame_list = sorted(frame_list)
        frame_list = [str(f) for f in frame_list]

        self.out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), self.framerate, self.downscaled_size)

        # pass data to threads and get data back
        num_loops = math.ceil(len(frame_list) / self.num_threads)  # the number of 'chunks' that the data will be split into
        for i in range(0, num_loops*self.num_threads, self.num_threads):

            for j in range(self.num_threads):

                # avoid going over the end of the list
                if i + j + 1 > len(frame_list):
                    break

                # start the processing thread
                self.threads.append(threading.Thread(target=self.thread, args=(j, frames_path + '\\' + frame_list[i + j])))
                self.threads[j].start()

            for j in range(len(self.threads)):
                self.threads[j].join()

            try:
                self.write_thread.join()  # make sure that the writing thread has finised before starting a new one
            except AttributeError:  # since the first time it will be none
                pass
            self.write_thread = threading.Thread(target=self.write_to_video, args=(self.sync_buff.copy(),))
            self.writing_done.clear()
            self.write_thread.start()

            self.threads = []

        self.writing_done.wait()
        self.out.release()

        with open(speed_path, 'w') as f:
            frames = '\n'.join(self.speed_at_frame)
            f.write(frames)

    # todo, finish and implement this
    def write_to_video(self, frames):
        for i in range(len(self.threads)):
            for j in range(len(frames[i])):
                self.out.write(frames[i][j][0])
                self.speed_at_frame.append(frames[i][j][1])
        self.writing_done.set()

    def thread(self, tid, batch):
        data = self.process_raw(batch)
        self.sync_buff.update({tid: data})

    # loads the raw data and processes it to an RGB png format
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


if __name__ == "__main__":
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
