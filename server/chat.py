import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))

import pickle

with open(dir_path + '/' + 'intents.json') as file:
    data = json.load(file)

# load trained model
model = keras.models.load_model(dir_path + '/' +'chat_model')

# load tokenizer object
with open(dir_path + '/' +'tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load label encoder object
with open(dir_path + '/' +'label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

# parameters
max_len = 20


def chat(inp):
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                            truncating='post', maxlen=max_len))
    print(result)
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    print(tag)
    for i in data['intents']:
        if i['tag'] == tag:
            return np.random.choice(i['responses'])
