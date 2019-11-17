import cv2


x1 = (0,0) # top left coordinate
x2 = (0,0) # bottom right coordinate
top_left_click = False # top left click
bottom_right_click = False # bottom right click

def draw_rectangle(event, x, y, flags, params):
	global x1, x2, top_left_click, bottom_right_click
	
	if event == cv2.EVENT_LBUTTONDOWN:
		
		# reset
		if top_left_click and bottom_right_click:
			x1 = (0,0) 
			x2 = (0,0) 
			top_left_click = False 
			bottom_right_click = False

		# Top left click
		if top_left_click == False:
			top_left_click = True
			x1 = (x, y)
		# Bottom right click
		elif bottom_right_click == False:
			bottom_right_click = True
			x2 = (x,y)


def draw_static_img_on_video():
	cap = cv2.VideoCapture(0)

	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

	x = width // 2
	y = height // 2

	w = width // 4
	h = height // 4

	print("*************************************")
	print(f"width = {width} ; height = {height}")
	print(f"x = {x} ; y = {y}")
	print(f"w = {w} ; h = {h}")
	print("*************************************")

	while True:
		ret, frame = cap.read()

		cv2.rectangle(frame, 
					  (x,y),
					  (x-w, y- h),
					  color=(0,0,255),
					  thickness=4)
		cv2.imshow("frame", frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()



def draw_interactivly_on_video():
	cap = cv2.VideoCapture(0)
	cv2.namedWindow('Test')
	cv2.setMouseCallback('Test', draw_rectangle)

	while True:
		ret, frame = cap.read()

		print("************************************")
		print(f"x1 = {x1}")
		print(f"x2 = {x2}")
		print(f"top_left_click = {top_left_click}")
		print(f"bottom_right_click = {bottom_right_click}")
		print("************************************")

		if top_left_click:
			cv2.circle(frame, center=x1, color=(0,0,255), radius=3)

		if top_left_click and bottom_right_click:
			cv2.rectangle(frame, x1, x2, color=(0,0,255), thickness=3)
		
		cv2.imshow("Test", frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()


if __name__ == "__main__":
	draw_interactivly_on_video()