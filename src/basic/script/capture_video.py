import numpy as np
import cv2

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out  = cv2.VideoWriter('resource/output.avi', fourcc, 20.0, (640 , 480))
def main():
	cap = cv2.VideoCapture(0)
	while True:
		if not cap.isOpened():
			cap.open()
		ret, frame = cap.read()
		grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
		out.write(frame)

		cv2.imshow("frame", grey)
		if cv2.waitKey(1) and 0xFF == ord('q'):
			break
	cap.release()
	out.release()
	cap.destroyAllWindows()


if __name__ == "__main__":
	main()