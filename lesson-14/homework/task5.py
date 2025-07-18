from PIL import Image
import numpy as np

# 1️ Load the image with PIL and convert to NumPy array
image = Image.open('images/birds.jpg')
img_array = np.array(image)

# 2️ Flip horizontally (left-to-right)
flipped_h = np.fliplr(img_array)

# Flip vertically (up-to-down)
flipped_hv = np.flipud(flipped_h)

# 3️ Add random noise
# Generate random noise in the range [-20, 20] for each pixel
noise = np.random.randint(-20, 21, img_array.shape, dtype='int16')

# Convert to int16 to avoid overflow when adding
noisy_image = img_array.astype('int16') + noise

# Clip to valid range [0, 255] and convert back to uint8
noisy_image = np.clip(noisy_image, 0, 255).astype('uint8')

# 4️ Brighten channels 
brightened_image = noisy_image.copy()
brightened_image[:, :, 0] = np.clip(brightened_image[:, :, 0] + 40, 0, 255)

# 5️ Apply a mask: black rectangle in the center (100x100)
h, w, _ = brightened_image.shape

# Find center coordinates
center_x, center_y = w // 2, h // 2
half_size = 50

# Rectangle coordinates
x1, x2 = center_x - half_size, center_x + half_size
y1, y2 = center_y - half_size, center_y + half_size

# Apply mask
brightened_image[y1:y2, x1:x2] = [0, 0, 0]

# 6️ Save final image using PIL
output_image = Image.fromarray(brightened_image)
output_image.save('images/birds_modified.jpg')

print("✅ Image manipulations complete. Saved as 'images/birds_modified.jpg'.")
