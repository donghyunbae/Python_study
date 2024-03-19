import numpy as np
import matplotlib.pyplot as plt
import cv2


colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}
'''
image = np.zeros((20, 20, 3), dtype="uint8")
imageRGB = image[:,:,::-1]

# We are going to see how cv2.line() works modifying the parameter lineType:
cv2.line(image, (5, 0), (20, 15), colors['yellow'], 1, cv2.LINE_4)
cv2.line(image, (0, 0), (20, 20), colors['red'], 1, cv2.LINE_AA)
cv2.line(image, (0, 5), (15, 20), colors['green'], 1, cv2.LINE_8)

image2 = np.zeros((300,300,3), dtype="uint8")
image2RGB = image2[:,:,::-1]
# Writing Text
# <Drawing text>                    cv2.putText(img, text, org(텍스트의 왼쪽아래 모서리 좌표), fonrFace, fontScale, color, thickness=1, lineType=8, bottomLeftOrigin=False)
cv2.putText(image2, "DongHyun", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['red'], 2, cv2.LINE_4)
cv2.putText(image2, "DongHyun", (10,70), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['blue'], 2, cv2.LINE_4)
cv2.putText(image2, "DongHyun", (10,110), cv2.FONT_HERSHEY_SIMPLEX, 0.9, colors['green'], 2, cv2.LINE_4)

'''
#=======================================================================================================================
image = np.zeros((400, 1200, 3), dtype="uint8")

# More functions related to text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2.5
thickness = 5
text = "abcdefghijklmnopqrstuvwxyz"
circle_radius = 10

# get the size of the text
ret, baseline = cv2.getTextSize(text, font, font_scale, thickness)

# get the text width and text hegit from ret
text_width, text_height = ret

#center the text in the image
text_x = int(round((image.shape[1] - text_width) / 2))
text_y = int(round((image.shape[0] + text_height) / 2))

# draw this point for reference:
cv2.circle(image, (text_x, text_y), circle_radius, colors['green'], -1)

# draw the rectangle (bounding box of the text)
cv2.rectangle(image, (text_x, text_y + baseline), (text_x + text_width - thickness, text_y - text_height), colors['blue'], thickness)

cv2.circle(image, (text_x, text_y + baseline), circle_radius, colors['red'], -1)
cv2.circle(image, (text_x + text_width - thickness, text_y - text_height), circle_radius, colors['cyan'], -1)

# draw the baseline line
cv2.line(image, (text_x, text_y + int(round(thickness/2))), (text_x + text_width - thickness, text_y + int(round(thickness/2))), colors['yellow'], thickness)

# Write the text centered in the image
cv2.putText(image, text, (text_x, text_y), font, font_scale, colors['magenta'], thickness)


plt.figure(1)
plt.imshow(image)
plt.title("image")
'''
plt.figure(2)
plt.imshow(imageRGB)
plt.title("imageRGB")
plt.figure(3)
plt.imshow(image2)
plt.title("image2")
plt.figure(4)
plt.imshow(image2RGB)
plt.title("image2RGB")
plt.figure(5)
plt.imshow(image3)
plt.title("image3")
'''
plt.show()