import os
import cv2
import numpy as np

train_dir=r"C:\Users\User\Desktop\Aluri Sri Moukthika\SLIDER\DETECTION\New folder"
test_dir=r"C:\Users\User\Desktop\Aluri Sri Moukthika\SLIDER\DETECTION\New folder"

# define the image dimensions and number of classes
img_height,img_width=28,28
num_classes=2

# create empty lists to store the training data
train_data,train_labels=[], []
test_data,test_labels = [], []

# loop through the training directory and load the images and labels
for label in os.listdir(train_dir):
    label_dir=os.path.join(train_dir,label)
    for filename in os.listdir(label_dir):
        img_path=os.path.join(label_dir,filename)
        img=cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
        # img = cv2.resize(img, (img_height, img_width))
        train_data.append(img)
        train_labels.append(int(label))

# loop through the testing data directory and load the images and labels
for label in os.listdir(test_dir):
    label_dir = os.path.join(test_dir, label)
    for filename in os.listdir(label_dir):
        img_path = os.path.join(label_dir, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (img_height, img_width))
        test_data.append(img)
        test_labels.append(int(label))

# convert the data and labels to numpy arrays
train_data = np.array(train_data) / 255.0
train_labels = np.array(train_labels)
test_data = np.array(test_data) / 255.0
test_labels = np.array(test_labels)