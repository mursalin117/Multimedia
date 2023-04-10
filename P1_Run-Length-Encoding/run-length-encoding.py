import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img_path = 'close-up-of-leaf-326055.jpg'
    img = cv.imread(img_path, 0)
    img = cv.resize(img, (400, 300))
    print(img.shape)
    plt.imsave("img.jpg", img, cmap='gray')

    file = open("img_compressed.txt", "w+")

    row, col = img.shape
    # for i in range(row):
    #     for j in range(col):
    #         cnt = 0
    #         k = j
    #         while(k < col):
    #             print("i = " + str(i) + "; j = " + str(j))
    #             if (img[i][j] == img[i][k]):
    #                 cnt += 1
    #                 if (cnt == 255):
    #                     st = ''
    #                     st += chr(img[i][j])
    #                     st += chr(cnt)
    #                     file.write(st)
    #                     j = k
    #                     break
    #             else :
    #                 st = ''
    #                 st += chr(img[i][j])
    #                 st += chr(cnt)
    #                 file.write(st)
    #                 j = k
    #                 break
    #             k += 1

if __name__ == '__main__':
    main()
