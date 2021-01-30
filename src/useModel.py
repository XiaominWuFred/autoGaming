# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image

# Load the TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path='shendu.tflite')
interpreter.allocate_tensors()
# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


wrongCount = 0
for i in range(1000):
    print(i)
    
    image = Image.open('../train/zuo/'+str(i)+'.png')
    npImg = np.array(image)
    input_image = npImg / 255
    input_image = np.array(input_image, dtype=np.float32)
    input_image = np.array(input_image)
    input_image = input_image.reshape((1,67,60,3))
    
    interpreter.set_tensor(input_details[0]["index"], input_image)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    result = np.argmax(output_data[0])
    
    print(result)
    
    if result != 2:
        wrongCount+=1
       
print(str(wrongCount)+ ' are wrong')