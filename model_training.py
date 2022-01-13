{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, InputLayer\
from tensorflow.keras.models import Sequential\
from tensorflow.keras import optimizers\
model = Sequential()\
model.add(restnet)\
model.add(Dense(512, activation='relu'))#, input_dim=(Img_Height,Img_Width,3)))\
model.add(Dropout(0.3))\
model.add(Dense(512, activation='relu'))\
model.add(Dropout(0.3))\
model.add(Dense(5, activation='softmax'))\
model.compile(loss='sparse_categorical_crossentropy',\
              optimizer=optimizers.Adam(lr=1e-4),\
              metrics=['accuracy'])\
model.summary()}