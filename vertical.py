
import cv2
import numpy as np
import time


W, H = 640,480

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,H)

line_pos = 3
line_thick = 3
line_step = 3

generated_image = np.zeros_like(cap.read()[1])


def flip_frame(frame):
    for y in range(frame.shape[0]):
        for c in range(frame.shape[2]):
            frame[y,:,c] = np.array([val for val in reversed(frame[y,:,c])])
    return frame

while cap.isOpened():

    ret, frame = cap.read()
    frame = flip_frame(frame)
    generated_image[line_pos-line_step:line_pos,:,:] = frame[line_pos-line_step:line_pos,:,:]
    final = generated_image.copy()
    final[line_pos:,:,:] = frame[line_pos:,:,:]
    final_display_frame = final.copy()
    line_pos += line_step
    cv2.line(frame,(0,line_pos),(W,line_pos),(247,233,128),line_thick)
    cv2.line(final_display_frame,(0,line_pos),(W,line_pos),(247,229,129),line_thick)

    # cv2.imshow("Frame",frame) # Normal camera image
    cv2.imshow("final",final_display_frame) # filtered final camera image
    # cv2.imshow("generated_image",generated_image) # generated image

    if line_pos == int(H/line_step)*line_step:
        break
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

cv2.imshow("generated_image",generated_image)
cv2.imwrite(f"generated_image_{time.time()}.jpg",generated_image)
cv2.waitKey(0)
