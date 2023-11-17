import cv2

# Initialize variables to store the coordinates of the selected area
top_left = None
bottom_right = None
drawing = False
original_image = None
image = None
done = False
areas = []
qty: int = 0


def draw_rectangle(event, x, y, flags, param):
    global top_left, bottom_right, drawing, original_image, done, image, qty, areas, temp

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        image = original_image.copy()
        temp = image.copy()
        top_left = (x, y)
        cv2.rectangle(image, top_left, top_left, (0, 255, 0), 2)
        cv2.imshow("Select Area", image)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            image = temp.copy()
            bottom_right = (x, y)
            cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
            cv2.imshow("Select Area", image)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        original_image = image.copy()
        bottom_right = (x, y)
        print(f"Selected area coordinates: Top Left = {top_left}, Bottom Right = {bottom_right}")
        if top_left == bottom_right:
            done = True
            return
        if top_left is not None:
            areas.append([top_left, bottom_right])
        qty = qty + 1
        top_left = None
        # return top_left, bottom_right
        # If you want to print the coordinates of all pixels within the area
        # print("Coordinates of all pixels within the selected area:")
        # for y in range(top_left[1], bottom_right[1]):
        #     for x in range(top_left[0], bottom_right[0]):
        #         print(f"(x, y) = ({x}, {y})")


def select(image_path):
    global top_left, bottom_right, drawing, original_image, done, image
    # Read the image
    original_image = cv2.imread(image_path)
    image = cv2.imread(image_path)

    cv2.namedWindow("Select Area")
    cv2.setMouseCallback("Select Area", draw_rectangle)

    while True:
        cv2.imshow("Select Area", image)
        if cv2.waitKey(1) & 0xFF == ord('q') or done:
            break

    cv2.destroyAllWindows()
    return areas
