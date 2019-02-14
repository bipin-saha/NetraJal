#Importing Library
import cv2
import numpy as np
import dlib
from math import hypot
import pyglet
import time
import webbrowser
import requests
from gtts import gTTS
import playsound
import os
import smtplib
import config

#importing from File
from bnbphoneticparser import BanglishToBengali

#URL FAMILY
new = 2
Url="https://google.com/?#q="
stock_url = "https://www.dsebd.org/top_20_share.php"
youtube_url = "https://www.youtube.com/watch?v=so9tkS2m3Xs"
facebook_url = "https://web.facebook.com/RUSparkerS/"
ieee_url = "https://spectrum.ieee.org/"
ru_url = "http://www.ru.ac.bd/"

 
#Load sounds
sound = pyglet.media.load("sound.wav", streaming=False)
left_sound = pyglet.media.load("left.wav", streaming=False)
right_sound = pyglet.media.load("right.wav", streaming=False)
siren = pyglet.media.load("2.wav", streaming=False)

#video capture from Notebook Webcam
cap = cv2.VideoCapture(0)

#video capture from Mobile/IP Camera

#ip = input("Input IP :")
    #print(a)
#port = input("Port :")
    #print(b)
#protocol = "http://"
#name = "shot.jpg"
#final =protocol+ip+":"+port+"/"+name
#print(final)
#url = final

#creating board
board = np.zeros((1600, 2400), np.uint8)
board[:] = 255

#import dlib face shape

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Keyboard settings
keyboard = np.zeros((1200, 2400, 3), np.uint8)
keys_set_1 = {0: "@", 1: "q", 2: "w", 3: "e", 4: "r",5: "t", 6: "y", 7: "u", 8: "i", 9: "o", 10: "p", 11: ".", 
              12: "+", 13: "a", 14: "s", 15: "d", 16: "f", 17: "g", 18: "h", 19: "j", 20: "k", 21:"l", 22: "(", 23: ")",
              24: "*", 25: ",", 26: "z", 27: "x", 28: "c", 29: "v", 30: "b", 31: "n", 32: "m", 33: "_", 34: "?", 35: "-",
              36: "!", 37: "0", 38: "1", 39: "2", 40: "3", 41: "4", 42: "5", 43: "6", 44: "7", 45: "8", 46: "9", 47: "=",
              48: "spk", 49: "src", 50: "CALL", 51: "MAIL", 52:"SE", 53:"ban",
              54: "sve", 55: "tube", 56: "FB", 57: "IEEE", 58:"RU", 59:"<"
              }

keys_set_2 = {0: "@", 1: "Q", 2: "W", 3: "E", 4: "R",5: "T", 6: "Y", 7: "U", 8: "I", 9: "O", 10: "P", 11: ".", 
              12: "+", 13: "A", 14: "S", 15: "D", 16: "F", 17: "G", 18: "H", 19: "J", 20: "K", 21:"L", 22: "(", 23: ")",
              24: "*", 25: ",", 26: "Z", 27: "X", 28: "C", 29: "V", 30: "B", 31: "N", 32: "M", 33: "_", 34: "?", 35: "-",
              36: "!", 37: "0", 38: "1", 39: "2", 40: "3", 41: "4", 42: "5", 43: "6", 44: "7", 45: "8", 46: "9", 47: "=",
              48: "spk", 49: "src", 50: "CALL", 51: "MAIL", 52:"SE", 53:"ban",
              54: "sve", 55: "tube", 56: "FB", 57: "IEEE", 58:"RU", 59:"<"
              }

def draw_letters(letter_index, text, letter_light):
    # Keys
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 200
        y = 0
    elif letter_index == 2:
        x = 400
        y = 0
    elif letter_index == 3:
        x = 600
        y = 0
    elif letter_index == 4:
        x = 800
        y = 0
    elif letter_index == 5:
        x = 1000
        y = 0
    elif letter_index == 6:
        x = 1200
        y = 0
    elif letter_index == 7:
        x = 1400
        y = 0
    elif letter_index == 8:
        x = 1600
        y = 0
    elif letter_index == 9:
        x = 1800
        y = 0
    elif letter_index == 10:
        x = 2000
        y = 0
    elif letter_index == 11:
        x = 2200
        y = 0
    elif letter_index == 12:
        x = 0
        y = 200
    elif letter_index == 13:
        x = 200
        y = 200
    elif letter_index == 14:
        x = 400
        y = 200
    elif letter_index == 15:
        x = 600
        y = 200
    elif letter_index == 16:
        x = 800
        y = 200
    elif letter_index == 17:
        x = 1000
        y = 200
    elif letter_index == 18:
        x = 1200
        y = 200
    elif letter_index == 19:
        x = 1400
        y = 200
    elif letter_index == 20:
        x = 1600
        y = 200
    elif letter_index == 21:
        x = 1800
        y = 200
    elif letter_index == 22:
        x = 2000
        y = 200
    elif letter_index == 23:
        x = 2200
        y = 200
    elif letter_index == 24:
        x = 0
        y = 400
    elif letter_index == 25:
        x = 200
        y = 400
    elif letter_index == 26:
        x = 400
        y = 400
    elif letter_index == 27:
        x = 600
        y = 400
    elif letter_index == 28:
        x = 800
        y = 400
    elif letter_index == 29:
        x = 1000
        y = 400
    elif letter_index == 30:
        x = 1200
        y = 400
    elif letter_index == 31:
        x = 1400
        y = 400
    elif letter_index == 32:
        x = 1600
        y = 400
    elif letter_index == 33:
        x = 1800
        y = 400
    elif letter_index == 34:
        x = 2000
        y = 400
    elif letter_index == 35:
        x = 2200
        y = 400
    elif letter_index == 36:
        x = 0
        y = 600
    elif letter_index == 37:
        x = 200
        y = 600
    elif letter_index == 38:
        x = 400
        y = 600
    elif letter_index == 39:
        x = 600
        y = 600
    elif letter_index == 40:
        x = 800
        y = 600
    elif letter_index == 41:
        x = 1000
        y = 600
    elif letter_index == 42:
        x = 1200
        y = 600
    elif letter_index == 43:
        x = 1400
        y = 600
    elif letter_index == 44:
        x = 1600
        y = 600
    elif letter_index == 45:
        x = 1800
        y = 600
    elif letter_index == 46:
        x = 2000
        y = 600
    elif letter_index == 47:
        x = 2200
        y = 600
    elif letter_index == 48:
        x = 0
        y = 800
    elif letter_index == 49:
        x = 400
        y = 800
    elif letter_index == 50:
        x = 800
        y = 800
    elif letter_index == 51:
        x = 1200
        y = 800
    elif letter_index == 52:
        x = 1600
        y = 800
    elif letter_index == 53:
        x = 2000
        y = 800
    elif letter_index == 54:
        x = 0
        y = 1000
    elif letter_index == 55:
        x = 400
        y = 1000
    elif letter_index == 56:
        x = 800
        y = 1000
    elif letter_index == 57:
        x = 1200
        y = 1000
    elif letter_index == 58:
        x = 1600
        y = 1000
    elif letter_index == 59:
        x = 2000
        y = 1000
    
 
    width = 200
    height = 200
    th = 3 # thickness
 
    # Text settings
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 10
    font_th = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y
 
    if letter_light is True:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (255, 255, 255), -1)
        cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (51, 51, 51), font_th)
    else:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (51, 51, 51), -1)
        cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 255, 255), font_th)
 
def draw_menu():
    rows, cols, _ = keyboard.shape
    th_lines = 4 # thickness lines
    cv2.line(keyboard, (int(cols/2) - int(th_lines/2), 0),(int(cols/2) - int(th_lines/2), rows),
             (51, 51, 51), th_lines)
    cv2.putText(keyboard, "LEFT", (80, 300), font, 6, (255, 255, 255), 5)
    cv2.putText(keyboard, "RIGHT", (80 + int(cols/2), 300), font, 6, (255, 255, 255), 5)
 
def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)
 
font = cv2.FONT_HERSHEY_PLAIN
 
def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))
 
    #hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    #ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)
 
    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))
 
    ratio = hor_line_lenght / ver_line_lenght
    return ratio

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, text)
        server.sendmail(config.EMAIL_ADDRESS, config.SEND_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")

subject = "NetraJal"


 
def eyes_contour_points(facial_landmarks):
    left_eye = []
    right_eye = []
    for n in range(36, 42):
        x = facial_landmarks.part(n).x
        y = facial_landmarks.part(n).y
        left_eye.append([x, y])
    for n in range(42, 48):
        x = facial_landmarks.part(n).x
        y = facial_landmarks.part(n).y
        right_eye.append([x, y])
    left_eye = np.array(left_eye, np.int32)
    right_eye = np.array(right_eye, np.int32)
    return left_eye, right_eye
 
def get_gaze_ratio(eye_points, facial_landmarks):
    left_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                                (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                                (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                                (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                                (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                                (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)], np.int32)
    # cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)
 
    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)
    cv2.polylines(mask, [left_eye_region], True, 255, 2)
    cv2.fillPoly(mask, [left_eye_region], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)
 
    min_x = np.min(left_eye_region[:, 0])
    max_x = np.max(left_eye_region[:, 0])
    min_y = np.min(left_eye_region[:, 1])
    max_y = np.max(left_eye_region[:, 1])
 
    gray_eye = eye[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY)
    height, width = threshold_eye.shape
    left_side_threshold = threshold_eye[0: height, 0: int(width / 2)]
    left_side_white = cv2.countNonZero(left_side_threshold)
 
    right_side_threshold = threshold_eye[0: height, int(width / 2): width]
    right_side_white = cv2.countNonZero(right_side_threshold)
 
    if left_side_white == 0:
        gaze_ratio = 1
    elif right_side_white == 0:
        gaze_ratio = 5
    else:
        gaze_ratio = left_side_white / right_side_white
    return gaze_ratio
 
# Counters
frames = 0
letter_index = 0
blinking_frames = 0
frames_to_blink = 6
frames_active_letter = 9
 
# Text and keyboard settings
text = ""
keyboard_selected = "left"
last_keyboard_selected = "left"
select_keyboard_menu = True
keyboard_selection_frames = 0
 
while True:
    _, frame = cap.read()
    #frame = cv2.resize(frame, None, fx=0.8, fy=0.8)
    #img_resp = requests.get(url)
    #img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    #frame = cv2.imdecode(img_arr, -1)
    
    rows, cols, _ = frame.shape
    keyboard[:] = (26, 26, 26)
    frames += 1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # Draw a white space for loading bar
    frame[rows - 50: rows, 0: cols] = (255, 255, 255)
 
    if select_keyboard_menu is True:
        draw_menu()
 
    # Keyboard selected
    if keyboard_selected == "left":
        keys_set = keys_set_1
    else:
        keys_set = keys_set_2
    active_letter = keys_set[letter_index]
 
    # Face detection
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
 
        left_eye, right_eye = eyes_contour_points(landmarks)
 
        # Detect blinking
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
 
        # Eyes color
        cv2.polylines(frame, [left_eye], True, (0, 0, 255), 2)
        cv2.polylines(frame, [right_eye], True, (0, 0, 255), 2)
 
 
        if select_keyboard_menu is True:
            # Detecting gaze to select Left or Right keybaord
            gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
            gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)
            gaze_ratio = (gaze_ratio_right_eye + gaze_ratio_left_eye) / 2
 
            if gaze_ratio <= 0.9:
                keyboard_selected = "right"
                keyboard_selection_frames += 1
                # If Kept gaze on one side more than 15 frames, move to keyboard
                if keyboard_selection_frames == 15:
                    select_keyboard_menu = False
                    right_sound.play()
                    # Set frames count to 0 when keyboard selected
                    frames = 0
                    keyboard_selection_frames = 0
                if keyboard_selected != last_keyboard_selected:
                    last_keyboard_selected = keyboard_selected
                    keyboard_selection_frames = 0
            else:
                keyboard_selected = "left"
                keyboard_selection_frames += 1
                # If Kept gaze on one side more than 15 frames, move to keyboard
                if keyboard_selection_frames == 15:
                    select_keyboard_menu = False
                    left_sound.play()
                    # Set frames count to 0 when keyboard selected
                    frames = 0
                if keyboard_selected != last_keyboard_selected:
                    last_keyboard_selected = keyboard_selected
                    keyboard_selection_frames = 0
 
        else:
            # Detect the blinking to select the key that is lighting up
            if blinking_ratio > 5:
                # cv2.putText(frame, "BLINKING", (50, 150), font, 4, (255, 0, 0), thickness=3)
                blinking_frames += 1
                frames -= 1
 
                # Show green eyes when closed
                cv2.polylines(frame, [left_eye], True, (0, 255, 0), 2)
                cv2.polylines(frame, [right_eye], True, (0, 255, 0), 2)
 
                # Typing letter
                if blinking_frames == frames_to_blink:
                    if active_letter != "<" and active_letter != "_":
                        text += active_letter
                    if active_letter == "_":
                        text += " "
                    if active_letter == "ban":
                        bangla = "ban"
                        if bangla in text:
                            text = text.replace(bangla,'')
                        banglish2bengali = BanglishToBengali()
                        text = banglish2bengali.parse(text.strip())
                    if active_letter == "src":
                        search = "src"
                        if search in text:
                            text = text.replace(search,'')
                        webbrowser.open(Url+text,new=new)
                    if active_letter == "MAIL":
                        send_email(subject, text)
                        mail = "MAIL"
                        if mail in text:
                            text = text.replace(mail,'')
                    if active_letter == "SE":
                        webbrowser.open(stock_url,new=new)
                        stock = "SE"
                        if stock in text:
                            text = text.replace(stock,'')
                    if active_letter == "tube":
                        webbrowser.open(youtube_url,new=new)
                        tube = "tube"
                        if tube in text:
                            text = text.replace(tube,'')
                    if active_letter == "FB":
                        webbrowser.open(facebook_url,new=new)
                        facebook = "FB"
                        if facebook in text:
                            text = text.replace(facebook,'')
                    if active_letter == "IEEE":
                        webbrowser.open(ieee_url,new=new)
                        ieee = "IEEE"
                        if ieee in text:
                            text = text.replace(ieee,'')
                    if active_letter == "RU":
                        webbrowser.open(ru_url,new=new)
                        ru = "RU"
                        if ru in text:
                            text = text.replace(ru,'')
                    if active_letter == "sve":
                        save = "sve"
                        if save in text:
                            text = text.replace(save,'')
                        f = open('h.txt','w')
                        f.write(text)
                        f.close()
                    if active_letter == "CALL":
                        siren.play()
                        siren.play()
                        call = "CALL"
                        if call in text:
                            text = text.replace(call,'')
                    if active_letter == "spk":
                        speak = "spk"
                        if speak in text:
                            text = text.replace(speak,'')
                            text = gTTS(text=text, lang='en')
                            file_name ="speak_file.mp3"
                            save_location = "audio\\" + file_name
                            text.save(save_location)
                            #os_file_name = "mpg321" + " "+ file_name 
                            #os.system(os_file_name)
                            playsound.playsound(save_location, True)
                    sound.play()
                    select_keyboard_menu = True
                    # time.sleep(1)
 
            else:
                blinking_frames = 0
 
 
    # Display letters on the keyboard
    if select_keyboard_menu is False:
        if frames == frames_active_letter:
            letter_index += 1
            frames = 0
        if letter_index == 60:
            letter_index = 0
        for i in range(60):
            if i == letter_index:
                light = True
            else:
                light = False
            draw_letters(i, keys_set[i], light)
 
    # Show the text we're writing on the board
    cv2.putText(board, text, (80, 100), font, 9, 0, 3)
 
    # Blinking loading bar
    percentage_blinking = blinking_frames / frames_to_blink
    loading_x = int(cols * percentage_blinking)
    cv2.rectangle(frame, (0, rows - 50), (loading_x, rows), (51, 51, 51), -1)
 
 
    cv2.imshow("Frame", cv2.resize(frame,(320,240)))
    cv2.imshow("Virtual keyboard", cv2.resize(keyboard,(1200,400)))
    cv2.imshow("Board", cv2.resize(board,(800,250)))
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# Release handle to the webcam
#video_capture.release()
cv2.destroyAllWindows()
