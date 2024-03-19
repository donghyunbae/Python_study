import numpy as np
import matplotlib.pyplot as plt
import cv2

# image of size : 500x500, 3channels, dtype : uint8

colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

image = np.zeros((500,500,3), dtype = "uint8")
print(image)

image[:] = colors['light_gray']

separation = 40
for key in colors:
    #line(img,pt1,pt2,color,thickness=1,lineType,shift=0)
    cv2.line(image, (0, separation), (400, separation), colors['magenta'], 10)
    separation += 40

plt.subplot(121)
plt.imshow(image)
plt.title('image')
plt.show()
#show_with_matplotlib(image, 'Dictionary with some predefined colors')