import json
import numpy as np
import tensorflow
import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense, Embedding
from keras.layers import TextVectorization
from keras.preprocessing.sequence import pad_sequences
import pickle

with open("data/intent.json") as f:
    data = json.load(f)

sentences = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        sentences.append(pattern)
        labels.append(intent["tag"])

tokenizer = TextVectorization()
tokenizer.adapt(sentences)

sequences = tokenizer(sentences)
max_len = 10
padded = pad_sequences(sequences, maxlen=max_len)

label_dict = {label: i for i, label in enumerate(set(labels))}
y = np.array([label_dict[label] for label in labels])

model = Sequential([
    Embedding(1000, 64, input_length=max_len),
    LSTM(64),
    Dense(32, activation='relu'),
    Dense(len(label_dict), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(padded, y, epochs=200)

model.save("models/intent_model.h5")

with open("models/tokenizer.pkl", "wb") as f:
    pickle.dump((tokenizer, label_dict, max_len), f)