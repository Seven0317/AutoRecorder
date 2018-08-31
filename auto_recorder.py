# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/30 18:37


import cv2
import os
import xlrd
import time

PATH_SRC = os.path.join(os.getcwd(), r"resource\video_src")


# Read device info
def reader(index):
    path = os.path.join(os.getcwd(), "device_info.xlsx")
    # Open excel app
    work_book = xlrd.open_workbook(path)
    # Select sheet
    work_sheet = work_book.sheet_by_name("device_list")
    # Read info by row
    info = work_sheet.row_values(index)
    return info


# Sort files by creating time
def sort_asc(file_dir):
    file_unsort = os.listdir(file_dir)
    file_sorted = sorted(file_unsort, key=lambda x: os.path.getmtime(os.path.join(file_dir, x)), reverse=False)
    return file_sorted


# Play video on PC
def displayer(video):
    # Capture the video
    capture = cv2.VideoCapture(video)
    if capture.isOpened():
        while True:
            # read frame of video and return the result
            ret, frame = capture.read()
            # If read frame successfully
            if ret is True:
                # Time between two frames
                cv2.imshow('video', frame)
                k = cv2.waitKey(40)
            else:
                break
            # Quit from displaying
            if k == ord('q'):
                break
    capture.release()
    # Close the displaying window
    cv2.destroyAllWindows()


def recorder(device):
    # Get location parameter of buttons
    start_x = (eval(device[5])[0][0] + eval(device[5])[1][0]) // 2
    start_y = (eval(device[5])[0][1] + eval(device[5])[1][1]) // 2
    stop_x = (eval(device[6])[0][0] + eval(device[6])[1][0]) // 2
    stop_y = (eval(device[6])[0][1] + eval(device[6])[1][1]) // 2
    # List all names of videos by ascending time of creating
    videos = sort_asc(PATH_SRC)
    # Start activity of camera
    os.system("adb shell am start -n %s" % device[3])
    time.sleep(1)
    # Auto display and record the video one by one
    for video in videos:
        # Get absolute path of video
        video_name = os.path.join(PATH_SRC, video)
        # record_x = (eval(device[4])[0][0] + eval(device[4])[1][0]) // 2
        # record_y = (eval(device[4])[0][1] + eval(device[4])[1][1]) // 2
        # os.system("adb shell input tap %d %d" % (record_x, record_y)
        # time.sleep(1)
        # Start to record the video
        os.system("adb shell input tap %d %d" % (start_x, start_y))
        time.sleep(1)
        # PC displays the video
        displayer(video_name)
        time.sleep(1)
        # Phone stops recording
        os.system("adb shell input tap %d %d" % (stop_x, stop_y))
        time.sleep(2)


if __name__ == '__main__':
    device_info = reader(index=2)
    recorder(device_info)
