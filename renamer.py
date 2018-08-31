# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/30 19:33

from auto_recorder import sort_asc
from auto_recorder import PATH_SRC
import os


PWD = os.getcwd()
PATH_DST = os.path.join(PWD, r"resource\video_dst")


def rename(ref, dst):
    sorted_ref = sort_asc(ref)
    sorted_dst = sort_asc(dst)
    for i in range(len(sorted_ref)):
        name_new = sorted_ref[i].split('.')[0]
        ori = os.path.join(dst, sorted_dst[i])
        fin = os.path.join(dst, name_new + '.mp4')
        os.rename(ori, fin)


if __name__ == '__main__':
    rename(PATH_SRC, PATH_DST)

