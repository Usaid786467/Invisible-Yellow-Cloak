
# import cv2
# import numpy as np
# import time

# print("""

# Harry :  Hey !! Would you like to try my invisibility cloak ??

#          Its awesome !!

        
#          Prepare to get invisible .....................
#     """)


# cap = cv2.VideoCapture(0)
# time.sleep(3)
# background=0
# for i in range(30):
# 	ret,background = cap.read()

# background = np.flip(background,axis=1)

# while(cap.isOpened()):
# 	ret, img = cap.read()
	
# 	# Flipping the image (Can be uncommented if needed)
# 	img = np.flip(img,axis=1)
	
# 	# Converting image to HSV color space.
# 	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 	value = (35, 35)
	
# 	blurred = cv2.GaussianBlur(hsv, value,0)
	
# 	# Defining lower range for red color detection.
# 	lower_red = np.array([0,120,70])
# 	upper_red = np.array([10,255,255])
# 	mask1 = cv2.inRange(hsv,lower_red,upper_red)
	
# 	# Defining upper range for red color detection
# 	lower_red = np.array([170,120,70])
# 	upper_red = np.array([180,255,255])
# 	mask2 = cv2.inRange(hsv,lower_red,upper_red)
	
# 	# Addition of the two masks to generate the final mask.
# 	mask = mask1+mask2
# 	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
	
# 	# Replacing pixels corresponding to cloak with the background pixels.
# 	img[np.where(mask==255)] = background[np.where(mask==255)]
# 	cv2.imshow('Display',img)
# 	k = cv2.waitKey(10)
# 	if k == 27:
# 		break
import cv2
import numpy as np
import time

print("""
Harry :  Hey !! Would you like to try my invisibility cloak ??
         Its awesome !!
        
         Prepare to get invisible .....................
         
         NOTE: Use a YELLOW colored cloth for the invisibility effect!
    """)

cap = cv2.VideoCapture(0)
time.sleep(3)
background = 0

# Capture background frames
for i in range(30):
    ret, background = cap.read()

background = np.flip(background, axis=1)

while(cap.isOpened()):
    ret, img = cap.read()
    
    if not ret:
        break
    
    # Flipping the image
    img = np.flip(img, axis=1)
    
    # Converting image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Apply Gaussian blur to reduce noise
    value = (35, 35)
    blurred = cv2.GaussianBlur(hsv, value, 0)
    
    # Defining HSV range for DARK yellow cloth detection
    # Narrower, more specific range to avoid detecting skin tones
    # Higher saturation requirement ensures only vibrant yellow is detected
    lower_yellow = np.array([18, 120, 100])
    # Upper bound for yellow
    upper_yellow = np.array([32, 255, 255])
    
    # Create mask for yellow color
    mask = cv2.inRange(blurred, lower_yellow, upper_yellow)
    
    # More aggressive morphological operations to remove noise and fill gaps
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)
    
    # Replacing pixels corresponding to cloak with the background pixels
    img[np.where(mask == 255)] = background[np.where(mask == 255)]
    
    cv2.imshow('Yellow Invisibility Cloak', img)
    
    k = cv2.waitKey(10)
    if k == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()