import cv2
# # video_name is the video being called
# # cap = cv2.VideoCapture('20020924_juve_dk_02a.mpeg')
# # cap.set(1, 1575)  # Where frame_no is the frame you want
# # ret, frame = cap.read()  # Read the frame
# # cv2.imshow('window_name', frame)  # show frame on window


# # while True:
# #     ch = 0xFF & cv2.waitKey(1)  # Wait for a second
# #     if ch == 27:
# #         break


# # apple = [1, 2, 3, 4, 5, 6]

# # # print(apple[2:4])


# # for num in apple[2:4]:
# #     print(num)


# # cap = cv2.VideoCapture('20020924_juve_dk_02a.mpeg')
# # cap.set(1, 1575)  # Where frame_no is the frame you want

# # # Used as counter variable
# # frame = 0

# # # checks whether frames were extracted
# # success = 1


# # while success and frame <= 3999:

# #     # vidObj object calls read
# #     # function extract frames
# #     success, image = cap.read()
# #     cv2.imshow('window_name', frame)  # show frame on window
# #     frame += 1


# # while True:
# #     ch = 0xFF & cv2.waitKey(1)  # Wait for a second
# #     if ch == 27:
# #         break


#
# cap.set(1, 90)

# # Check if camera opened successfully
# if (cap.isOpened() == False):
#     print("Error opening video file")

count = 90

# Read until video is completed
cap = cv2.VideoCapture('20020924_juve_dk_02a.mpeg')
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True and count < 100:
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        count += 1
    # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Break the loop
    else:
        break

# When everything done, release
# the video capture object
# cap.release()

# # Closes all the frames
# cv2.destroyAllWindows()


# from tkinter import *
# root = Tk()

# for i in range(10):
#     myButton = Button(root, text="Click me!")
#     myButton.pack()

# root.mainloop()
