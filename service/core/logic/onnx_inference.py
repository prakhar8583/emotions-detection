import onnxruntime as rt
import cv2
import numpy as np
import time
import service.main as s

def emotions_detector(img_array):
    time_init=time.time()
    


    # Check the actual input name
    input_name = s.m.get_inputs()[0].name
    output_name = s.m.get_outputs()[0].name  # usually your output layer

    # Preprocess the image
    img_resized = cv2.resize(img_array, (256, 256))
    im = np.float32(img_resized) / 255.0  # normalize if model expects [0,1]
    img_input = np.expand_dims(im, axis=0)  # add batch dimension
    time_elapse_preprocees = time.time() - time_init
   
    # Run inference with correct input name
    onnx_pred = s.m.run([output_name], {input_name: img_input})
    time_elapse = time.time() - time_init
 # it is just for cal culating The time here we subtract privous time and current
    emotion=""
    if np.argmax(onnx_pred[0][0])==0:
        emotion="angry"
    elif np.argmax(onnx_pred[0][0])==1:
        emotion="happy"
    elif np.argmax(onnx_pred[0][0])==2:
        emotion="Nothing"
    else:
        emotion="Sad"

    return {"emotion": emotion,
            "time_elapse":str(time_elapse),
            "time_elapse_preprocees":str(time_elapse_preprocees)}
