#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
a python-opencv tool to view jpg files,the parameter is either file or dir
Created on 2014-10-23 
@author: pengfei Fu
"""
import numpy as np
import cv2
import os,sys

PARAMETER = 1
file_list = []
length = 0

LEFT = 0
RIGHT = 0
UP = 0
DOWN = 0

# move function
def move(direction,image,image1):
	rows,cols = image1.shape
	global LEFT,RIGHT,UP,DOWN
	if direction == 0:
		LEFT = LEFT - 50
	elif direction == 1:
		LEFT = LEFT + 50
	elif direction == 2:
		UP = UP - 50
	elif direction == 3:
		UP = UP + 50
	M = np.float32([[1,0,LEFT],[0,1,UP]])
	dst = cv2.warpAffine(image,M,(cols,rows))

	cv2.imshow('image',dst)
	return

# Traversal the dir
def walk_dir(dir,topdown=True):
	global file_list
	global length
	for root, dirs, files in os.walk(dir, topdown):
		for name in files:
			if "jpg" == os.path.splitext(os.path.join(root,name))[1][1:]:
				file_list.append(os.path.join(root,name))
				length = length + 1
			
# get sys parameter
# first judge the parameter number
if len(sys.argv) == 1:
	print "you should use it like this: script.py file!"
	os._exit(0)
elif (os.path.exists(sys.argv[1])) == False:
	print "your input neither is a file or a dir, please try again!"
	os._exit(0)

# judge file type
e = os.path.isfile(sys.argv[1])
if e == True:
	print "is a file"
elif (os.path.isdir(sys.argv[1])) == True:
	# here, we Traversal the dir
	dir = sys.argv[1]
	walk_dir(dir)

cur_numble = 0
img = cv2.imread(file_list[cur_numble],1)
img1 = cv2.imread(file_list[cur_numble],0)
cv2.namedWindow('image',0)
print file_list[cur_numble]
cv2.imshow('image',img)
k = cv2.waitKey(0)
while(k != 27): # if ESC key to exit
	if k == ord('n'): #if 'n' key will change to another photo 
		cur_numble += 1 
		img = cv2.imread(file_list[cur_numble],1)
		img1 = cv2.imread(file_list[cur_numble],0)
		cv2.imshow('image',img)
	elif k == ord('s'): # wait for 's' key to save and exit
		cv2.imwrite('messigray.jpg',img)
		cv2.destroyAllWindows()
		os._exit(0)
	elif k == ord('c'): # if 'c' key then to change to color photo
		cv2.imshow('image',img)
	elif k == ord('g'): # if 'g' key then to change to grey photo
		cv2.imshow('image',img1)
	if k == ord('b'): #if 'b' key bigger the photo 
		PARAMETER = PARAMETER*1.1
		res = cv2.resize(img,None,fx = PARAMETER,fy = PARAMETER,interpolation = cv2.INTER_LINEAR)
		img = res
		cv2.imshow('image',res)
	if k == ord('v'): #if 'v' key smaller the photo 
		PARAMETER = PARAMETER/1.1
		cv2.destroyWindow('image')
		cv2.namedWindow('image',0)
		img = cv2.imread(file_list[cur_numble])
		res = cv2.resize(img,None,fx = PARAMETER,fy = PARAMETER,interpolation = cv2.INTER_AREA)
		cv2.imshow('image',res)
	if k == ord('l'): #if 'l' key move the photo to left 
		move(0,img,img1)
	if k == ord('r'): #if 'l' key move the photo to left 
		move(1,img,img1)
	if k == ord('u'): #if 'l' key move the photo to left 
		move(2,img,img1)
	if k == ord('d'): #if 'l' key move the photo to left 
		move(3,img,img1)
	k = cv2.waitKey(0)
cv2.destroyAllWindows()
