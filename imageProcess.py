import cv2
import numpy as np        
import matplotlib.pyplot as plt
from scipy import ndimage
import math
from keras.models import load_model


# loading pre trained model
model = load_model('cnn_model/digit_classifier.h5')

def predictDigit(oriImg):
	test_image = oriImg.reshape(-1,28,28,1)
	return np.argmax(model.predict(test_image))


#pitting label
def putLabel(t_oriImg,label,x,y):
	font = cv2.FONT_HERSHEY_SIMPLEX
	l_x = int(x) - 10
	l_y = int(y) + 10
	cv2.rectangle(t_oriImg,(l_x,l_y+5),(l_x+35,l_y-35),(0,255,0),-1) 
	cv2.putText(t_oriImg,str(label),(l_x,l_y), font,1.5,(255,0,0),1,cv2.LINE_AA)
	return t_oriImg

# refining each digit
def imageRefiner(gray):
	oriSize = 22
	staSize = 28
	rows,cols = gray.shape
	
	if rows > cols:
		factor = oriSize/rows
		rows = oriSize
		cols = int(round(cols*factor))        
	else:
		factor = oriSize/cols
		cols = oriSize
		rows = int(round(rows*factor))
	gray = cv2.resize(gray, (cols, rows))
	
	#get padding 
	colsPadding = (int(math.ceil((staSize-cols)/2.0)),int(math.floor((staSize-cols)/2.0)))
	rowsPadding = (int(math.ceil((staSize-rows)/2.0)),int(math.floor((staSize-rows)/2.0)))
	
	#apply apdding 
	gray = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')
	return gray




def getOutput(path):
  
	oriImg = cv2.imread(path,2)
	oriImg_org =  cv2.imread(path)

	ret,thresh = cv2.threshold(oriImg,127,255,0)
	im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

	for i,n in enumerate(contours):
		epsilon = 0.01*cv2.arcLength(n,True)
		approx = cv2.approxPolyDP(n,epsilon,True)
		
		hull = cv2.convexHull(n)
		k = cv2.isContourConvex(n)
		x,y,w,h = cv2.boundingRect(n)
		
		if(hierarchy[0][i][3]!=-1 and w>10 and h>10):
			#putting boundary on each digit
			cv2.rectangle(oriImg_org,(x,y),(x+w,y+h),(0,255,0),2)
			
			
			#cropping each image and process
			finImg = oriImg[y:y+h, x:x+w]
			finImg = cv2.bitwise_not(finImg)
			finImg = imageRefiner(finImg)
			th,fnl = cv2.threshold(finImg,127,255,cv2.THRESH_BINARY)

			# getting prediction of cropped image
			pred = predictDigit(finImg)
			print(pred)
			
			# placing label on each digit
			(x,y),radius = cv2.minEnclosingCircle(n)
			oriImg_org = putLabel(oriImg_org,pred,x,y)


	return oriImg_org
