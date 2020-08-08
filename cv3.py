import cv2
import numpy as np
import os
import time
import random
# created by durzal
vid = 0
three = cv2.imread('three.png')
four = cv2.imread('four.png')
ace = cv2.imread('ace.png')
knife = cv2.imread('knife.PNG')
shock = cv2.imread('shock.PNG')
geforce = cv2.imread('geforce.png')
test = cv2.imread('test.png')
final_frame2 = cv2.imread('test2.jpg')
three_k_edited =  cv2.imread('three_edited.png')
four_k_edited =  cv2.imread('four_edited.png.png')
five_k_edited =  cv2.imread('ace_edited.png')
fourk_2 = cv2.imread('t2.png')
testing = cv2.imread('testing.png')
final_frame3 = cv2.imread('final_fram3.jpg')
four_test = cv2.imread('4.png')

three_k_clips = 0
four_k_clips = 0
five_k_clips = 0
shock_clips = 0
knife_clips = 0
unnamed_clips = 0
def frame_capture(file):
    # Playing video from file:
    cap = cv2.VideoCapture(file)

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    currentFrame = 0


    # Capture frame by frame
    ret, frame = cap.read()
    while ret:
        global final_frame
        ret, frame = cap.read()

        # Only take the first frame and tenth frame
#        if ret:
#            name = './data/frame%d' % vid + str(currentFrame) +  '.jpg'
#            cv2.imwrite(name, frame)
        if ret:
            name = './data/frame%d' % vid +  '.jpg'
            cv2.imwrite(name, frame)
            final_frame = frame

#        if currentFrame == 1:
#            name = './data/frame%d' % vid + str(currentFrame) +  '.jpg'
#            cv2.imwrite(name, frame)
#            break

        print(currentFrame)

        # To stop duplicate images
        currentFrame += 1

    cap.release()
    cv2.destroyAllWindows()

def frame_comparison3k():
    global three_kills
    global flag_three
    try:
        res = cv2.matchTemplate(three, final_frame, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        mean = np.mean(res)
        standard = np.std(res)
        print(mean,standard)


    except cv2.error:
        pass
    threshold = 0.8
    flag_three = False
    if np.amax(res) > threshold:
        flag_three = True
    #print(flag_three)

def frame_comparison_4k():
    global four_kills
    global flag_four
    try:
        res = cv2.matchTemplate(four, final_frame, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        mean = np.mean(res)
        standard = np.std(res)
        print(mean, standard)


    except cv2.error:
        pass
    threshold = 0.8
    flag_four = False
    if np.amax(res) > threshold:
        flag_four = True
    #print(flag_four)



def frame_comparison_5k():
    global five_kills
    global flag_ace

    try:
        res = cv2.matchTemplate(ace, final_frame, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        mean = np.mean(res)
        standard = np.std(res)
        print(mean, standard)


    except cv2.error:
        pass
    threshold = 0.8
    flag_ace = False
    if np.amax(res) > threshold:
        flag_ace = True
    #print(flag_ace)
def frame_comparison_knife():
    global knife_kill
    global flag_knife
    try:
        res = cv2.matchTemplate(knife, final_frame, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        mean = np.mean(res)
        standard = np.std(res)
        print(mean, standard)


    except cv2.error:
        pass
    threshold = 0.8
    flag_knife = False
    print(np.amax(res))
    if np.amax(res) > threshold:
        print("game broken xd")
        flag_knife = True
def frame_comparison_shock():
    global shock_kill
    global flag_shock
    try:
        res = cv2.matchTemplate(shock, final_frame, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        mean = np.mean(res)
        standard = np.std(res)
        print(mean, standard)


    except cv2.error:
        pass
    threshold = 0.8
    flag_shock = False
    if np.amax(res) > threshold:
        flag_shock = True

for file in os.listdir("C:/Users/zacky/Desktop/Coding/Python/Object detection/"):
    if file.endswith(".mp4"):
        vid += 1
        three_kills = False
        four_kills = False
        five_kills = False
        shock_kills = False
        knife_kills = False
        unname = False
        path = (os.path.join("C:/Users/zacky/Desktop/Coding/Python/Object detection/", file))
        frame_capture(path)
        frame_comparison3k()
        frame_comparison_4k()
        frame_comparison_5k()
        frame_comparison_knife()
        frame_comparison_shock()
        if flag_ace and not flag_three and not flag_four and not flag_shock and not flag_knife:
            #print("ace")
            five_kills = True
        elif flag_three and not flag_four and not flag_ace and not flag_shock and not flag_knife:
            #print("3k")
            three_kills = True
        elif flag_four and not flag_three and not flag_ace and not flag_shock and not flag_knife:
            #print("4k")
            four_kills = True
        elif flag_three and flag_four and not flag_ace and not flag_shock and not flag_knife:
            #print("4k")
            four_kills = True
        elif flag_four and flag_ace and not flag_three and not flag_shock and not flag_knife:
            #print("ace")
            five_kills = True
        elif flag_four and flag_ace and flag_three and not flag_knife:
            #print("ace")
            five_kills = True
        elif flag_shock:
            shock_kills = True
        elif flag_knife:
            knife_kills = True
        else:
            print("last frame was not how many kills AKA other")
            unname = True
        # os.rename(prev name, new name)
        if unname:
            unnamed_clips += 1
            unname_title = "unknown_k_" + str(unnamed_clips) + ".mp4"
            os.rename(file, "videos/" + str(unname_title))

        if three_kills:
            print("3k")
            three_k_clips += 1
            threek_title = "three_k_" + str(three_k_clips) + ".mp4"
            os.rename(file, "videos/" + str(threek_title))
        if four_kills:
            print("4k")
            four_k_clips += 1
            fourk_title = "four_k_" + str(four_k_clips) + ".mp4"
            os.rename(file,"videos/" + str(fourk_title))
        if five_kills:
            print("5k")
            five_k_clips += 1
            fivek_title = "five_k_" + str(five_k_clips) + ".mp4"
            os.rename(file, "videos/" + str(fivek_title))
        if knife_kills:
            print("knife_kill")
            knife_clips += 1
            knife_title = "knife_k_" + str(knife_clips) + ".mp4"
            os.rename(file, "videos/" + str(knife_title))
        if shock_kills:
            print("shock_kill")
            shock_clips += 1
            shock_title = "shock_k_" + str(shock_clips) + ".mp4"
            os.rename(file, "videos/" + str(shock_title))

        #cv2.imshow("final_frame", final_frame2)
        #cv2.waitKey(0)



