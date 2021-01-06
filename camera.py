import cv2
from imutils.video import WebcamVideoStream
import face_recognition
from PIL import Image



class VideoCamera:
    def __init__(self):
        self.stream = WebcamVideoStream(src=0).start()

    def __del__(self):
        self.stream.stop()

    def get_frame(self):
        frame = self.stream.read()
        face_locations = face_recognition.face_locations(frame)
        for top, right, bottom, left in face_locations:
            # Adds the rectangle around detected location of the faces
            cv2.rectangle(frame,
                          (left, top),
                          (right, bottom),
                          (0, 255, 0),
                          2)
            # print(emotion_predictions)
        ret, jpeg = cv2.imencode(".jpg", frame)
        data = []
        data.append(jpeg.tobytes())
        return data