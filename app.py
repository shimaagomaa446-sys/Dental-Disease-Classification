import gradio as gr
import tensorflow as tf
import numpy as np

model=tf.keras.models.load_model("D:\Data Science\Training\sprint 2\OralDiseas\efficentNetB4_best_weight.keras")

classes = [
    'Calculus',
    'Caries',
    'Gingivitis',
    'Ulcers',
    'Tooth Dicoloration',
    'Hypodontia'
]
def predict_image(image):
    image=image.resize((256,256))
    image=np.array(image)
    image=image.astype('float32')
    image=np.expand_dims(image,axis=0)
    predictions=model.predict(image,verbose=0)
    results={
        classes[i]:float(predictions[0][i])
        for i in range(len(classes))
    }
    return results
demo = gr.Interface(
    fn=predict_image,

    inputs=gr.Image(
        type="pil",
        label="Upload Dental Image"
    ),

    outputs=gr.Label(
        num_top_classes=6,
        label="Prediction Results"
    ),

    title="Dental Disease Classification",

    description="Upload a dental image to predict its class."
)
demo.launch(share=True)