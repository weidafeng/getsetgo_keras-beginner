# -*- coding: utf-8 -*-
"""Copy of Inceptionv3_vizualizing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KiVtVtcwBA7FJcsKkTl-bJGZAl58WdfT
"""

#lineone:InceptionV3 model is used avgpool layer (last before layer) of the architecture is extracted and used for prediction
#http://image-net.org/about-stats
#https://arxiv.org/abs/1409.1556
#default input size for model is 299x299
#below code has been tested and executed only in colab.research.google.com .Please make sure you have enabled GPU from notebook settings before execution

#for visualising VGG19 model
!pip install -q pydot-ng
!pip install graphviz
!apt-get install graphviz

import pydot_ng
import graphviz

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

from keras.models import Model

#avg_pool
model=Model(inputs=base_model.input,outputs=base_model.get_layer('avg_pool').output)

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

#its not possible to give predictions from fc1 layer immediately ;only after passing it through softmax layer (assigning probabilities) we can use predict function to classify 
#in order to add layer you need to take a sequential initialized model and then add fc1 model along with it

from keras.models import Sequential
from keras.layers import Dense, Activation

#sequential model is initialised with model2
model2=Sequential()
#fc1 layer is added in a sequential manner to model2
model2.add(model)
#adding softmax layer for prediction
model2.add(Dense(1000,activation='softmax'))

#input is provided to model to predict the class
predictions=base_model.predict(x)

predictions.shape

#decode_predictions decodes the values of predict and provides the output
print("predict:",decode_predictions(predictions,top=2)[0])

#predictions listed given image is a pencil_sharpner with highest probability and then pencil_box at next probability 
#you can also increase the number of predictions by increasing the values of top to 3,4.. in "print("predict:",decode_predictions(predictions,top=4))""

from keras.utils.vis_utils import model_to_dot
from IPython.display import SVG

#model of base_model(complete VGG19)
SVG(model_to_dot(base_model).create(prog='dot',format='svg'))

#below you can see that model contains blocks till 'avg_pool' layer (model)
#extracted model
SVG(model_to_dot(model).create(prog='dot',format='svg'))

#after addition of dense1 layer for softmax prediction(model+softmax) 
#(extracted layer+ softmax)--->predictions
SVG(model_to_dot(model2).create(prog='dot',format='svg'))