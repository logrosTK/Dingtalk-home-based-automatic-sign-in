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
    screenScale=1
    target= cv2.imread(r'targe.png',cv2.IMREAD_GRAYSCALE)
    screenshot=pyscreeze.screenshot('./my_screenshot.png')
    temp = cv2.imread(r'my_screenshot.png',cv2.IMREAD_GRAYSCALE)
    theight, twidth = target.shape[:2]
    tempheight, tempwidth = temp.shape[:2]
    print("目标图宽高："+str(twidth)+"-"+str(theight))
    print("模板图宽高："+str(tempwidth)+"-"+str(tempheight))
    scaleTemp=cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
    stempheight, stempwidth = scaleTemp.shape[:2]
    print("缩放后模板图宽高："+str(stempwidth)+"-"+str(stempheight))
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
        #左键点击屏幕上的这个位置
        pyautogui.click(tagCenterX,tagCenterY,button='left')
        print("位置是：",tagCenterX,tagCenterY)
        sleep(2)
        pyautogui.click(3750,2000,button='left')
        print("位置是：",tagCenterX+750,tagCenterY+480)
        sleep(1)
        pyautogui.click(3300,1700,button='left')
        sleep(0.5)
        win32api.keybd_event(32, 0, 0, 0)
        sleep(0.5)
        win32api.keybd_event(32, 0, win32con.KEYEVENTF_KEYUP, 0)
        sleep(0.5)
        pyautogui.click(3300,1700,button='left')
        #pyautogui.moveTo(tagCenterX-500, tagCenterY)
    else:print("未发现")




def method2():
    # print("执行了方法2")
    root = tk.Tk()
    root.title('DDregister by TK')
    root.geometry('480x400')
    index = tk.Label(root, text='开始运行了。。。。', bg='#D3D3D3', font=('微软雅黑', 10))
    index.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.15)
    btn1 = tk.Button(root, text='点击停止', bg='#D3D3D3', font=('微软雅黑', 13), command=sys.exit)
    btn1.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.15)
    root.mainloop()

def method3():
    # print("执行了方法3")
    while (1 == 1):
        method1()
        sleep(30)#等待30s运行一次，这里你可以自己改

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
    root = tk.Tk()
    root.title('DDregister by TK 1.0')
    root.geometry('480x400')


    index1 = tk.Label(root, text='需将钉钉全屏', bg='#D3D3D3', font=('微软雅黑', 10))
    index1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.15)
    index2 = tk.Label(root, text='仅适用4K分辨率', bg='#D3D3D3', font=('微软雅黑', 10))
    index2.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.15)
    index3 = tk.Label(root, text='请及时关注2.0版本更新', bg='#D3D3D3', font=('微软雅黑', 10))
    index3.place(relx=0.25, rely=0.35, relwidth=0.5, relheight=0.15)
    
    # 第一个按钮
    btn1 = tk.Button(root, text='点击这里运行', bg='#D3D3D3', font=('微软雅黑', 13), command=lambda:[root.destroy(),thread_it()])
    btn1.place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.15)
    root.mainloop()