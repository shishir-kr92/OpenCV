import cv2
import time

ROOT_PATH = "/home/shishir/study/code/OpenCV"
def read_video_file():
	cap = cv2.VideoCapture(f'{ROOT_PATH}/resource/myVideo.avi')
	frame_rate = cv2.CAP_PROP_FRAME_COUNT,

	# check whether we were able to open the vide file or not
	if not cap.isOpened():
		print("ERROR: FILE NOT FOUND OR WRONG CODEC USED")

	while cap.isOpened():
		# reading the video file
		ret, frame = cap.read()

		# whether we are actaully reading anything or not
		if ret:
			time.sleep(1/12)
			cv2.imshow('frame', frame)

			if cv2.waitKey(2) & 0xFF == ord('q'):
				break
		else:

			break
if __name__ == "__main__":
	read_video_file()