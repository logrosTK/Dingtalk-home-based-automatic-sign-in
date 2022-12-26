import sys
from time import sleep
import tkinter as tk
import pyautogui
import pyscreeze
import cv2
import threading
import urllib.request as urllib
import win32api

import win32con   #导入这两个模块






def method1():
    # print("执行了方法1")
    screenScale0=1
    target0= cv2.imread(r'diling.png',cv2.IMREAD_GRAYSCALE)
    screenshot0=pyscreeze.screenshot('./my_screenshot0.png')
    temp0 = cv2.imread(r'my_screenshot0.png',cv2.IMREAD_GRAYSCALE)
    theight0, twidth0 = target0.shape[:2]
    tempheight0, tempwidth0 = temp0.shape[:2]
    print("目标图“签到”宽高："+str(twidth0)+"-"+str(theight0))
    print("模板图“签到”宽高："+str(tempwidth0)+"-"+str(tempheight0))
    scaleTemp0=cv2.resize(temp0, (int(tempwidth0 / screenScale0), int(tempheight0 / screenScale0)))
    stempheight0, stempwidth0 = scaleTemp0.shape[:2]
    print("缩放后模板图“签到”宽高："+str(stempwidth0)+"-"+str(stempheight0))
    print("--------------------------------------")
    res0 = cv2.matchTemplate(scaleTemp0, target0, cv2.TM_CCOEFF_NORMED)
    mn_val0, max_val0, min_loc0, max_loc0 = cv2.minMaxLoc(res0)
    if(max_val0>=0.95):
        screenScale=1
        target= cv2.imread(r'targe.png',cv2.IMREAD_GRAYSCALE)
        screenshot=pyscreeze.screenshot('./my_screenshot.png')
        temp = cv2.imread(r'my_screenshot.png',cv2.IMREAD_GRAYSCALE)
        theight, twidth = target.shape[:2]
        tempheight, tempwidth = temp.shape[:2]
        print("目标图“去提交”宽高："+str(twidth)+"-"+str(theight))
        print("模板图“去提交”宽高："+str(tempwidth)+"-"+str(tempheight))
        scaleTemp=cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
        stempheight, stempwidth = scaleTemp.shape[:2]
        print("缩放后模板图“去提交”宽高："+str(stempwidth)+"-"+str(stempheight))
        print("--------------------------------------")
        res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
        mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)


        if(max_val>=0.9):
        # 计算出中心点
            top_left = max_loc
            bottom_right = (top_left[0] + twidth, top_left[1] + theight)
            tagHalfW=int(twidth/2)
            tagHalfH=int(theight/2)
            tagCenterX=top_left[0]+tagHalfW
            tagCenterY=top_left[1]+tagHalfH

        #top_left1 = max_loc1
        #bottom_right = (top_left1[0] + twidth1, top_left1[1] + theight1)
        #tagHalfW1=int(twidth1/2)
        #tagHalfH1=int(theight1/2)
        #tagCenterX1=top_left1[0]+tagHalfW1
        #tagCenterY1=top_left1[1]+tagHalfH1
        #左键点击屏幕上的这个位置
            pyautogui.click(tagCenterX,tagCenterY,button='left')

            sleep(2)
            screenScale1=1
            target1= cv2.imread(r'dier.png',cv2.IMREAD_GRAYSCALE)
            screenshot1=pyscreeze.screenshot('./my_screenshot1.png')
            temp1 = cv2.imread(r'my_screenshot1.png',cv2.IMREAD_GRAYSCALE)
            theight1, twidth1 = target1.shape[:2]
            tempheight1, tempwidth1 = temp1.shape[:2]
            print("目标图“提交”宽高："+str(twidth1)+"-"+str(theight1))
            print("模板图“提交”宽高："+str(tempwidth1)+"-"+str(tempheight1))
            scaleTemp1=cv2.resize(temp1, (int(tempwidth1 / screenScale1), int(tempheight1 / screenScale1)))
            stempheight1, stempwidth1 = scaleTemp1.shape[:2]
            print("缩放后模板图“提交”宽高："+str(stempwidth1)+"-"+str(stempheight1))
            print("--------------------------------------")
            res1 = cv2.matchTemplate(scaleTemp1, target1, cv2.TM_CCOEFF_NORMED)
            mn_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)
            if(max_val1>=0.9):
                top_left1 = max_loc1
                bottom_right = (top_left1[0] + twidth1, top_left1[1] + theight1)
                tagHalfW1=int(twidth1/2)
                tagHalfH1=int(theight1/2)
                tagCenterX1=top_left1[0]+tagHalfW1
                tagCenterY1=top_left1[1]+tagHalfH1

                pyautogui.click(tagCenterX1,tagCenterY1,button='left')
                print("位置是：",tagCenterX1-100,tagCenterY1-200)
                sleep(1)
                pyautogui.click(tagCenterX1-400,tagCenterY1-400,button='left')
                sleep(0.5)
                win32api.keybd_event(49, 0, 0, 0)
                sleep(0.5)
                win32api.keybd_event(49, 0, win32con.KEYEVENTF_KEYUP, 0)
                sleep(1)
                pyautogui.click(tagCenterX1,tagCenterY1,button='left')
            else:print("未发现提交2")
      #  pyautogui.click(tagCenterX1,tagCenterY1,button='left')

        #pyautogui.moveTo(tagCenterX-500, tagCenterY)
        else:print("未发现提交1")
    else:print("未发现签到")




def method2():
    # print("执行了方法2")
    root = tk.Tk()
    root.title('DDregister by TK 3.0')
    root.geometry('480x400')
    index = tk.Label(root, text='开始运行了。。。', bg='#D3D3D3', font=('微软雅黑', 10))
    index.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.15)
    btn1 = tk.Button(root, text='点击停止', bg='#D3D3D3', font=('微软雅黑', 13), command=sys.exit)
    btn1.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.15)
    root.mainloop()

def method3():
    # print("执行了方法3")
    while (1 == 1):
        method1()
        sleep(20)#等待30s运行一次，这里你可以自己改

def thread_it():  # 多线程
    thread1 = threading.Thread(target=method3)
    # thread2 = threading.Thread(target=method2)
    thread1.setDaemon(True)
    # thread2.setDaemon(True)
    thread1.start()
    # thread2.start()
    method2()

if __name__ == '__main__':
    urllib.urlretrieve('http://logros.3vhost.club/DD.png','./targe.png')#这里面的地址是“去提交”这张图片
    urllib.urlretrieve('http://logros.3vhost.club/two.png','./dier.png')
    urllib.urlretrieve('http://logros.3vhost.club/zero.png','./diling.png')
    root = tk.Tk()
    root.title('DDregister by TK 3.0')
    root.geometry('480x400')


    index1 = tk.Label(root, text='确保钉钉在最上层', bg='#D3D3D3', font=('微软雅黑', 10))
    index1.place(relx=0.25, rely=0.05, relwidth=0.6, relheight=0.15)
    index2 = tk.Label(root, text='仅适用4K分辨率', bg='#D3D3D3', font=('微软雅黑', 10))
    index2.place(relx=0.25, rely=0.2, relwidth=0.6, relheight=0.15)
    index3 = tk.Label(root, text='解决填写非签到家校本的问题', bg='#D3D3D3', font=('微软雅黑', 9))
    index3.place(relx=0.25, rely=0.35, relwidth=0.6, relheight=0.15)
    
    # 第一个按钮
    btn1 = tk.Button(root, text='点击这里运行', bg='#D3D3D3', font=('微软雅黑', 13), command=lambda:[root.destroy(),thread_it()])
    btn1.place(relx=0.25, rely=0.6, relwidth=0.6, relheight=0.15)
    root.mainloop()