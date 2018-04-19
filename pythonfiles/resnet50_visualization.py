# -*- coding: utf-8 -*-
"""visualImagenetwithResnet50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15XyHuUEQKnT6UC-O5-cl_898NhFsa1sz
"""

#lineone:Visualizing Resnet50 model 
#http://image-net.org/about-stats
#https://arxiv.org/abs/1512.03385

#for visualising resnet50 model
!pip install -q pydot-ng
!pip install graphviz
!apt-get install graphviz

#for visvualizing resnet50 model
#note:below two packages should be imported before importing keras.
#https://stackoverflow.com/questions/49853303/how-to-install-pydot-graphviz-on-google-colab
import pydot_ng 
import graphviz

#make sure you are importing preprocess_input and decode_predictions from resnet50 model
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input,decode_predictions
import numpy as np

#imagenet weights of resnet50 is loaded into model 
model=ResNet50(weights='imagenet',include_top=True)

#This provides text based description of model
model.summary()

#for visualizing resnet50 model
from keras.utils.vis_utils import model_to_dot
from IPython.display import SVG

#block representation of the model
SVG(model_to_dot(model).create(prog='dot',format='svg'))

#further reference to source code
#https://github.com/fchollet/deep-learning-models/blob/master/resnet50.py