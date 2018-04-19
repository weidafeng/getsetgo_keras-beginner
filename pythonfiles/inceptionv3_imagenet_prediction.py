# -*- coding: utf-8 -*-
"""Inceptionv3_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JF02WB6fbyYgMJszGFizN92wBRrguT52
"""

#lineone:InceptionV3 model is used to classify a image (given:url of a image)-(keras)
#http://image-net.org/about-stats
#https://arxiv.org/abs/1409.1556
#default input size for model is 299x299
#below code has been tested and executed only in colab.research.google.com .Please make sure you have enabled GPU from notebook settings before execution

#mistakes made by me
#gave input shape as (224,224) whereas default input shape of Inceptionv3 is (299,299)
#used vggs keras.application.vgg instead of inceptionv3 here "from keras.applications.inception_v3 import preprocess_input,decode_predictions"

#make sure you are importing preprocess_input and decode_predictions from inceptionv3 model
from keras.applications.inception_v3 import InceptionV3
from keras.layers import Input
from keras.applications.inception_v3 import preprocess_input,decode_predictions
from keras.preprocessing import image

#For visualising picture
from matplotlib import pyplot as plt
# %matplotlib inline

input_tensor=Input(shape=(299,299,3))
#you can give custom input with input_tensor

base_model=InceptionV3(input_tensor=input_tensor,weights='imagenet',include_top=True)

#image is loaded from url
#you can use imread to load loacally 
from urllib.request import urlopen

#url of the image is stored in url_link1
#(299,299) is the target size of Inceptionv3 model
urllink=urlopen("https://5.imimg.com/data5/OX/YI/MY-19292667/green-color-sharpener-500x500.jpg")
img=image.load_img(urllink,target_size=(299,299))
import numpy as np

#preprocessing input image
x=image.img_to_array(img)
x=np.expand_dims(x,axis=0)
x=preprocess_input(x)

#input is provided to model to predict the class
predictions=base_model.predict(x)

predictions.shape

#decode_predictions decodes the values of predict and provides the output
print("predict:",decode_predictions(predictions,top=2)[0])

#predictions listed given image is a pencil_sharpner with highest probability and then pencil_box at next probability 
#you can also increase the number of predictions by increasing the values of top to 3,4.. in "print("predict:",decode_predictions(predictions,top=4))""