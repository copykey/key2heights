import cv2

class FindEtch:
    # Given a 2d array of booleans representing whether a pixel is a key
    # or not - `image` - and the length of one pixel in inches  - `cell_length`
    # - returns an array of the heights of each pin.
    def find_etches(image, cell_length):
        im2, contours, hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(image, contours, -1, (0,255,0), 3)

FindEtch.find_etches([[1,1,1],[1,1,1],[0,1,1], [0,1,1]], 0.1)

