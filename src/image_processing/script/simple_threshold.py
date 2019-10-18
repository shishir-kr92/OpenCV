import cv2

path="/home/shishir/study/code/openCV/resource/"

def threshold_img():
	img = cv2.imread(f"{path}/crossword.jpg",0)
	print(img.shape)
	cv2.imshow("raw", img)

	## if the pixel in greater then threshold value, it is assigned	one value
	## else it is assigned another value.cv2.imshow("raw", img)

	#if s(x,y) > trunc the s(x,y) = max_val else 0
	retVal_binary, binary_img = cv2.threshold(img, 150, 200, type=cv2.THRESH_BINARY)
	print("************binary***************")
	print(f"min = {binary_img.min()}")
	print(f"max = {binary_img.max()}")


	#if s(x,y) > trunc the s(x,y) = 0 else max_val
	retVal_binary, binary_img_inv = cv2.threshold(img, 150, 200, type=cv2.THRESH_BINARY_INV)
	print("************binary inverse***************")
	print(f"min = {binary_img_inv.min()}")
	print(f"max = {binary_img_inv.max()}")

	#if s(x,y) > trunc the s(x,y) = trunc else keep it as it is
	retVal_binary, trunc_img = cv2.threshold(img, 170, 255, type=cv2.THRESH_TRUNC)
	print("************trunc***************")
	print(f"min = {trunc_img.min()}")
	print(f"max = {trunc_img.max()}")

	# if s(x,y) > trunc  keep it as it is else change it to zero, max_val is ignored
	retVal_binary, tozero_img = cv2.threshold(img, 170, 255, type=cv2.THRESH_TOZERO)
	print("************tozero***************")
	print(f"min = {tozero_img.min()}")
	print(f"max = {tozero_img.max()}")

	# if s(x,y) > trunc  change it to zero else keep it as it is, max_val is ignored
	retVal_binary, tozero_img_inv = cv2.threshold(img, 170, 255, type=cv2.THRESH_TOZERO_INV)
	print("************tozero inverse***************")
	print(f"min = {tozero_img_inv.min()}")
	print(f"max = {tozero_img_inv.max()}")

	cv2.imshow("raw", img)
	cv2.imshow("binary", binary_img)
	cv2.imshow("binary_inv", binary_img_inv)
	cv2.imshow("trunc", trunc_img)
	cv2.imshow("tozero_img", tozero_img)
	cv2.imshow("tozero_img_inv", tozero_img_inv)

	cv2.waitKey(-1)

if __name__ == "__main__":
	threshold_img()