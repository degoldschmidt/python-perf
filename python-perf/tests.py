import math, random
import numpy as np
from timer import timed
import cv2 as cv
from tqdm import tqdm

@timed
def append_numbers(dims):
    outlist = []
    for i in range(dims):
        outlist.append(i)
    return outlist

@timed
def gen_random_numbers(dims):
    outlist = []
    for i in range(dims):
        outlist.append(random.random())
    return outlist

@timed
def process_video(nframes, display=False):
    filename = '/home/degoldschmidt/Downloads/cam03_2019-09-20T13_33_28.avi'
    cap = cv.VideoCapture(filename)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    for i in tqdm(range(nframes)):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        if display:
            cv.imshow('frame', cv.resize(gray,(700,700)))
            if cv.waitKey(1) == ord('q'):
                break

@timed
def square_numbers(dims):
    outlist = []
    for i in range(dims):
        outlist.append(i*i)
    return outlist