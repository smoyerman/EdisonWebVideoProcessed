from flask import Flask, Response
import cv2
import numpy as np

class Camera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    # Reset camera capture size for faster processing
	self.cap.set(3,480)
	self.cap.set(4,360)

    def get_frame(self):
	ret, frame = self.cap.read()
    # Apply laplacian edge detection to image
	laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    # Write out original and edge detected images at once
	cv2.imwrite('blah.jpg',np.hstack((frame,laplacian)))
	return open('blah.jpg', 'rb').read()


app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
