import cv2
import ColorDetection

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 refers to the default webcam, if you have multiple, use 1, 2, etc.

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the captured frame
    cv2.imshow('Live Camera Feed', frame)

        # Check for key pressed
    key = cv2.waitKey(1)

    # Press 'C' to capture an image
    if key == ord('c') or key == ord('C'):
        cv2.imwrite('Sources/IMG_3768_1.JPG', frame)
        cv2.destroyAllWindows()
        print("Image captured!")

        # Press 'C' to capture an image
    if key == ord('p') or key == ord('P'):
        ColorDetection.compare()
        print("Done")

    # Press 'Q' to exit
    elif key == ord('q') or key == ord('Q'):
        break
# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
