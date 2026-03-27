import pickle
import numpy as np
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

model = load_model("models/intent_model.h5")

with open("models/tokenizer.pkl", "rb") as f:
    tokenizer, label_dict, max_len = pickle.load(f)

inv_labels = {v: k for k, v in label_dict.items()}

def get_intent(text):
    seq = tokenizer([text])
    padded = pad_sequences(seq, maxlen=max_len)

    pred = np.argmax(model.predict(padded))
    return inv_labels[pred]