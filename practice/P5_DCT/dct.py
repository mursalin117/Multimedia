import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.fftpack import dct, idct

def dct_2d(img):
    return dct(dct(img.T, norm='ortho').T, norm='ortho')

def idct_2d(img):
    return idct(idct(img.T, norm='ortho').T, norm='ortho')

def main():
    img = cv2.imread("close-up-of-leaf-326055.jpg", 0)
    img2 = np.copy(img)

    plt.imshow(img2, cmap='gray')
    plt.title('Original Image')
    plt.show()
    cv2.imwrite('img-1.jpg', img2)

    dct_img = dct_2d(img2)
    plt.imshow(dct_img, cmap='gray')
    plt.title('DCT Image')
    plt.show()
    cv2.imwrite('img-2.jpg', dct_img)

    idct_img = idct_2d(dct_img)
    plt.imshow(idct_img, cmap='gray')
    plt.title('IDCT Image')
    plt.show()
    cv2.imwrite('img-3.jpg', idct_img)

if __name__ == '__main__':
    main()