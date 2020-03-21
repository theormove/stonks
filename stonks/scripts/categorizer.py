from tensorflow import keras
import codecs
import json
import operator


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

def load_index():
	with open('word_index.json','r') as f:
		return json.load(f)

word_index = load_index()
	
	
metals = keras.models.load_model("metals_model.h5")
energy = keras.models.load_model("energy_model.h5")
agroculture = keras.models.load_model("agroculture_model.h5")
models = {'metals':metals, 'energy': energy,'agroculture': agroculture}


def categorizer(text):
	predictions = {}
	encoded = keras.preprocessing.sequence.pad_sequences([text_encode(text,[1])], value=word_index["<PAD>"], padding="post", maxlen=5000)
	for model in models:
		predictions[model] = models[model].predict(encoded)[0]
	result = []	
	for key in predictions:
		if predictions[key] > 0.5:
			result.append(key)
	if len(result) == 0:
		result.append('glob')		
	return result