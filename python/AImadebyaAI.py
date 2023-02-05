import tensorflow as tf
from tensorflow.keras.layers import Dense, Embedding, Dropout, LSTM
from tensorflow.keras.models import Sequential

    # load the text data
with open('data.txt') as f:
    text = f.read()

    # create tokenizer
tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~ ')
tokenizer.fit_on_texts([text])
tokens = tokenizer.texts_to_sequences([text])[0]

    # create the model
model = Sequential()
model.add(Embedding(len(tokenizer.word_index)+1, 64))
model.add(LSTM(64, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(64))
model.add(Dropout(0.2))
model.add(Dense(len(tokenizer.word_index)+1, activation='softmax'))
    
# compile and fit the model
model.compile(loss='c')
    
   