import cv2

path = "resource"
def blend_image():
	img1 = cv2.imread(f"{path}/dog_backpack.png")
	# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	dog_img = cv2.resize(img1, dsize=(512,512))

	img2 = cv2.imread(f"{path}/watermark_no_copy.png")
	# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
	water_mark = cv2.resize(img2, dsize=(512,512))
	

	while True:
		blended_img = cv2.addWeighted(src1=dog_img, alpha=0.8, src2=water_mark, beta=0.2, gamma=0)
		cv2.imshow("blended_img", blended_img)
		# cv2.imshow("img2", water_mark)

		if cv2.waitKey(2) & 0xFF == 27:
			break
	cv2.destroyAllWindows()

if __name__ == "__main__":
 	blend_image()