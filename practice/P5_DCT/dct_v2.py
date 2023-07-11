from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

def apply_dct(image):
    height, width = image.shape
    transformed_image = np.zeros((height, width))

    for i in range(0, height, 16):
        for j in range(0, width, 16):
            block = image[i:i+16, j:j+16]
            dct_block = cv2.dct(block.astype(np.float32))
            transformed_image[i:i+16, j:j+16] = dct_block

    return transformed_image

def apply_idct(transformed_image):
    height, width = transformed_image.shape
    reconstructed_image = np.zeros((height, width))

    for i in range(0, height, 16):
        for j in range(0, width, 16):
            transformed_block = transformed_image[i:i+16, j:j+16]
            idct_block = cv2.idct(transformed_block.astype(np.float32))
            reconstructed_image[i:i+16, j:j+16] = idct_block

    return reconstructed_image

# Load the grayscale image
image = cv2.imread('close-up-of-leaf-326055.jpg', cv2.IMREAD_GRAYSCALE)

# Apply DCT
transformed_image = apply_dct(image)
# cv2.imwrite('img_v2_2.jpg', transformed_image)
# plt.imsave('img_v2_2.jpg', transformed_image)
# transformed_image.imsave('img_v2_21.jpg')

# Apply IDCT
reconstructed_image = apply_idct(transformed_image)
# cv2.imwrite('img_v2_3.jpg', reconstructed_image)
# plt.imsave('img_v2_3.jpg', reconstructed_image)
# reconstructed_image.imsave('img_v2_31.jpg')
print(np.size(transformed_image),np.size(reconstructed_image))
# Plot the transformed and reconstructed images
plt.subplot(1, 2, 1)
plt.imshow(transformed_image, cmap='gray')
plt.title('Transformed Image')

plt.subplot(1, 2, 2)
plt.imshow(reconstructed_image, cmap='gray')
plt.title('Reconstructed Image')

plt.show()