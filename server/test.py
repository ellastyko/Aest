
# import cv2 as cv


# cap = cv.VideoCapture(0)

# # Check if the webcam is opened correctly
# if not cap.isOpened():
#     raise IOError("Cannot open webcam")

# while True:
#     ret, frame = cap.read()
#     print(frame)
#     frame = cv.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
#     cv.imshow('Input', frame)

#     c = cv.waitKey(1)
#     if c == 27:
#         break

# cap.release()
# cv.destroyAllWindows()

def select(table, fields):
    print('select')
    return action

def get(n):
    print('get')
    return 0


def action(data = {}, where = {}):
    print('where')
    return get




select ('table', ['id', 'login'], where= { }) (8)
