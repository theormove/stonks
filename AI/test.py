import tensorflow as td 
from tensorflow import keras
import numpy as np
import os
import codecs



def text_encode(text, encoded):
	for word in text: 
		if word.lower() in word_index and word_index[word.lower()] < 100000:
			encoded.append(word_index[word.lower()])
		else:
			encoded.append(2)
	return encoded		


def txt_to_data(url="test.txt"):
	encoded = [1]
	with codecs.open(url,'r', encoding = 'utf-8', errors = 'ignore') as f:
		for line in f.readlines():
			nline = line.replace(",","").replace("(","").replace("(","").replace(":","").replace("\"","").replace("*","").strip().split(" ")
			text_encode(nline, encoded)
		return encoded

def create_train_data(directories, main, k = 0.9):
	lenghts = []
	for directory in directories:
		lenghts.append(len(os.listdir(directory)))
	print(min(lenghts))	
	for i in range(int(min(lenghts)*k)):
		for directory in directories:
			train_data.append(txt_to_data(directory + '/' + os.listdir(directory)[i]))
			if directory in main:
				train_labels.append(1)
			else:
				train_labels.append(0)	
	for i in range(int(min(lenghts)*k),min(lenghts)):
		for directory in directories:
			test_data.append(txt_to_data(directory + '/' + os.listdir(directory)[i]))
			if directory == main:
				test_labels.append(1)
			else:
				test_labels.append(0)			

def decode_text(text):
	reverse_word_index = dict([(value,key) for (key,value) in word_index.items()])
	return " ".join([reverse_word_index.get(i,"?") for i in text])



data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = ([],[]),([],[])

word_index = data.get_word_index()

word_index = {k:(v+3) for k, v in word_index.items()}

word_index["<PAD>"] = 0 
word_index["<START>"] = 1
word_index["<UNK>"] = 2 
word_index["<UNUSED>"] = 3
'''
create_train_data(['metals','energy', 'reuters_metals','agriland','energymarket'],['agriland'])		
print(decode_text(train_data[1]))
print(train_labels[1])

train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post", maxlen=5000)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding="post", maxlen=5000)




model = keras.Sequential()
model.add(keras.layers.Embedding(100000,8))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

model.summary()

model.compile(optimizer="adam", loss = "binary_crossentropy", metrics=["accuracy"])

x_val = train_data[:100]
x_train = train_data[100:] 

y_val = train_labels[:100]
y_train = train_labels[100:]

print(len(test_data))
print(len(test_labels))
print(len(x_val))
print(len(y_val))
print(len(x_train))
print(len(y_train))

fitModel = model.fit(x_train, y_train, epochs = 3, batch_size = 1, validation_data=(x_val,y_val), verbose=1) 

results = model.evaluate(test_data, test_labels)

model.save("model.h5")	
'''
model = keras.models.load_model("model.h5")
if __name__ == "__main__":
	encoded = txt_to_data()
	encoded = keras.preprocessing.sequence.pad_sequences([encoded], value=word_index["<PAD>"], padding="post", maxlen=5000)
	predict = model.predict(encoded)
	print(encoded)
	print(predict[0])				