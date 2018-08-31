# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/30 22:52

import os
import xlrd


# read device info
def device(index):
    path = os.path.join(os.getcwd(), "device_info.xlsx")
    work_book = xlrd.open_workbook(path)
    work_sheet = work_book.sheet_by_name("device")
    info = work_sheet.row_values(index)
    return info


if __name__ == '__main__':
    info = device(1)
    print(info)
    print(eval(info[4]))