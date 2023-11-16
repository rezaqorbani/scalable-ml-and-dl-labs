import gradio as gr
import numpy as np
from PIL import Image
import requests
import pandas as pd
import hopsworks
import joblib

project = hopsworks.login()
fs = project.get_feature_store()


mr = project.get_model_registry()
model = mr.get_model("wine_model", version=1)
model_dir = model.download()
model = joblib.load(model_dir + "/wine_model.pkl")


def wine(type, volatile_acidity, chlorides, density, alcohol):
    print("Calling function")
    if type=='White':
        type=1
    else:
        type=0
    df = pd.DataFrame([[type, volatile_acidity, chlorides, density, alcohol]], 
                      columns=['type', 'volatile_acidity', 'chlorides', 'density', 'alcohol'])
    print("Predicting")
    print(df)
    # 'res' is a list of predictions returned as the label.
    res = model.predict(df) 
    # We add '[0]' to the result of the transformed 'res', because 'res' is a list, and we only want 
    # the first element.
    print(res)
    #TO_DO: Add images, change to url to the directory with our images
    flower_url = "https://raw.githubusercontent.com/rezaqorbani/scalable-ml-and-dl-labs/main/lab1/wine/wine_images/" + str(res[0]) + ".png"
    img = Image.open(requests.get(flower_url, stream=True).raw)            
    return img


demo = gr.Interface(
    fn=wine,
    title="Wine Quality Predictive Analytics",
    description="Experiment with different input features to predict the wine quality.",
    allow_flagging="never",
    inputs=[
        gr.inputs.Radio(default='White', label="Wine type", choices=['White','Red']),
        gr.inputs.Slider(0,1.6,label='Volatile Acidity'),
        gr.inputs.Slider(0,0.7, label="Chlorides"),
        gr.inputs.Slider(0.98,1.04, label="Density"),
        gr.inputs.Number(default='10', label="Alcohol"),
        ],
    outputs=gr.Image(type="pil"))

demo.launch()