import cv2


# Windows --- *'DIVX'
# Mac or LINUX --- *'XVID'
root_path = "/home/shishir/study/code/OpenCV"
def capture_video():
	cap = cv2.VideoCapture(0)

	if not cap.isOpened():
		cap.open()
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	writer = cv2.VideoWriter(f'{root_path}/resource/myVideo.avi',
		                     cv2.VideoWriter_fourcc(*'XVID'),
		                     cv2.CAP_PROP_FRAME_COUNT,
		                     (width, height))

	print(f"width  : {width}")
	print(f"height : {height}")
	while True:
		ret, frame = cap.read()
		# print(f"ret : {ret}")

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		writer.write(frame)
		cv2.imshow('RBG', frame)
		# cv2.imshow('GRAY', gray)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	writer.release()
	cv2.destroyAllWindows()


if __name__ == "__main__":
	print("inside main")
	capture_video()