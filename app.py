import streamlit as st
import torch
import numpy as np
from utils import output_processing
from transformers import pipeline

@st.cache_resource
def get_model():
    # tokenizer = AutoTokenizer.from_pretrained("Yash907/db-finetuned-NER")
    # model = AutoModelForSequenceClassification.from_pretrained("Yash907/db-finetuned-NER")
    pipe = pipeline("token-classification", model="Yash907/db-finetuned-NER")
    return pipe

model = get_model()

st.title(':rainbow[Fine-Tuned Named Entity Recognition]')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

st.markdown("""This webapp can detect entities in your input sentence. The model used
here is fine-tuned on custom dataset [link](https://huggingface.co/datasets/conll2003) for detecting entities.""", 
unsafe_allow_html=True)

input_text = st.text_area(label = ' ', placeholder = 'Enter your text here', max_chars = 512, 
                     label_visibility = "collapsed")
button = st.button('Analyze')


if input_text and button:
    # try :    
    #     output = model(input_text)
    # except Exception as e:
    #     pass
    # else: 
    final_output = output_processing(output)
    for key, value in final_output.items():
        st.success(f"**{key}** : {value}")    