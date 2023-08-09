import cv2


def contour_area(img):
    # to separate the object from the background
    ret, thresh = cv2.threshold(img, 127, 255, 0)

    # Find the contours of the object
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original image
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    # Get the area of the object in pixels
    area = cv2.contourArea(contours[0])
    # Convert the area from pixels to a real-world unit of measurement (e.g. cm^2)
    scale_factor = 22  # 1 pixel = 0.1 cm
    size = area * scale_factor ** 2
    size = size * 0.0001
    # Print the size of the object
    # print('Size:', size, "m^2")

    return size
