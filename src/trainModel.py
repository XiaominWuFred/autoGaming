# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import math
from keras import Sequential
from keras.layers import Dense, Flatten, Activation, Dropout, Conv2D, MaxPooling2D
from PIL import Image
import random


def loadImgs():
    Imgs = []

    for i in range(1000):
        image = Image.open('../train/shang/'+str(i)+'.png')
        npImg = np.array(image)
        Imgs.append([npImg,0])

        print('loading shang: '+str(i))
    
    for i in range(1000):
        image = Image.open('../train/xia/'+str(i)+'.png')
        npImg = np.array(image)
        Imgs.append([npImg,1])

        print('loading xia: '+str(i))
        
    for i in range(1000):
        image = Image.open('../train/zuo/'+str(i)+'.png')
        npImg = np.array(image)
        Imgs.append([npImg,2])

        print('loading zuo: '+str(i))
    
    for i in range(1000):
        image = Image.open('../train/you/'+str(i)+'.png')
        npImg = np.array(image)
        Imgs.append([npImg,3])

        print('loading you: '+str(i))
    
    Imgs = np.array(Imgs)
    print(Imgs.shape)
    
    random.shuffle(Imgs)
    
    imgs = []
    labels = []
    
    for each in Imgs:
        imgs.append(each[0])
        labels.append(each[1])
        
    imgs = np.array(imgs)
    labels = np.array(labels)
    print(imgs.shape)
    print(labels)
    
    train_images = imgs[0:3600]
    train_labels = labels[0:3600]
    test_images = imgs[3600:]
    test_labels = labels[3600:]
    
    return (train_images, train_labels), (test_images, test_labels)

# Download MNIST dataset.
#mnist = keras.datasets.mnist
#(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

(train_images, train_labels), (test_images, test_labels) = loadImgs()


# Normalize the input image so that each pixel value is between 0 to 1.
train_images = train_images / 255.0
test_images = test_images / 255.0

# Show the first 25 images in the training dataset.
#show_sample(train_images,
            #['Label: %s' % label for label in train_labels])

conv_net = Sequential()

conv_net.add(Conv2D(32, (3, 3), activation='relu', input_shape=(67,60,3))) #127, 134
# fully connected
conv_net.add(MaxPooling2D(pool_size=(3, 3)))
conv_net.add(Conv2D(64, (3, 3), activation='relu'))
conv_net.add(Flatten())
conv_net.add(Dense(32, activation='relu', use_bias=True))  
conv_net.add(Dense(16, activation='relu', use_bias=True)) 
conv_net.add(Dense(4, activation='softmax', use_bias=True))
#conv_net.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model = conv_net

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

train_images = np.array(train_images)
train_images = train_images.reshape((train_images.shape[0],train_images.shape[1],train_images.shape[2],3))
model.fit(train_images, train_labels, epochs=50)

test_images = np.array(test_images)
test_images = test_images.reshape((test_images.shape[0],test_images.shape[1],test_images.shape[2],3))
test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

# Predict the labels of digit images in our test dataset.
predictions = model.predict(test_images)

# Convert Keras model to TF Lite format.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TF Lite model as file
f = open('../models/shendu2.tflite', "wb")
f.write(tflite_model)
f.close()

print('finished')

