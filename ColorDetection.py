import cv2
import numpy as np
from PIL import Image

from SpecifyCheckingArea import select

# Read the image
source_path = 'IMG_3768.JPG'

source = cv2.imread(source_path)
areas = select(source_path)
result_final = []
for item in areas:
    top_left, bottom_right = item
    for i in range(1, 6):
        step_result = []
        image_path = f'IMG_3768_{i}.JPG'
        image = cv2.imread(image_path)

        area_source = source[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

        # Calculate the mean color in the area
        mean_color_source = np.mean(area_source, axis=(0, 2))

        area = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        # Calculate the mean color in the area
        mean_color = np.mean(area, axis=(0, 2))
        # Calculate the difference between mean color and reference color
        color_diff = np.abs(mean_color - mean_color_source)
        # Compare
        if np.all(color_diff < 5):  # The threshold of 30 is arbitrary and may need to be adjusted
            print(
                f"{image_path}: The mean color in the area {mean_color}, which is close to the reference "
                f"color {mean_color_source}.")
            print("PASS")
            result = image.copy()
            cv2.rectangle(result, top_left, bottom_right, (0, 255, 0), 2)
            result_final.append((i, "PASS"))
        else:
            print(f"{image_path}: The mean color in the area is {mean_color}, which is NOT close to the "
                  f"reference color {mean_color_source}.")
            print("FAIL")
            result = image.copy()
            cv2.rectangle(result, top_left, bottom_right, (0, 0, 255), 2)
            result_final.append((i, "FAIL"))
        cv2.imwrite(f"Results/result{top_left[0]}-{i}.jpg", result)
    result_final.sort(key=lambda x: x[0])
print(result_final)

