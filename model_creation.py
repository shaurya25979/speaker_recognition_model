{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from tensorflow.keras.applications.resnet50 import ResNet50\
from keras.models import Model\
import keras\
restnet = ResNet50(include_top=False, weights='imagenet', input_shape=(Img_Height,Img_Width,3))\
output = restnet.layers[-1].output\
output = keras.layers.Flatten()(output)\
restnet = Model(restnet.input, output)\
for layer in restnet.layers[13:]:\
    layer.trainable = False\
restnet.summary()}