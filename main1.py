import cv2
import mediapipe as mp 
import pyautogui 

cam=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_w,screen_h=pyautogui.size()
index_y=0
while True:
    _,frame=cam.read()
    frame=cv2.flip(frame,1)
    frame_h,frame_w,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*frame_w)
                y=int(landmark.y*frame_h)
                if id == 8:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    index_x=screen_w/frame_w*x 
                    index_y=screen_h/frame_h*y
                    pyautogui.moveTo(index_x,index_y)
                    


                if id == 4:
                        cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                        thumb_x=screen_w/frame_w*x 
                        thumb_y=screen_h/frame_h*y
                        print( abs(index_y - thumb_y))
                        if abs(index_y - thumb_y) < 20:
                            print("clicke")
                            pyautogui.click()
                            pyautogui.sleep(1)

            



    cv2.imshow("V Mouse",frame)
    cv2.waitKey(1)