import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk import ne_chunk
from nltk.corpus import movie_reviews
from nltk import FreqDist
from nltk import NaiveBayesClassifier, classify
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk import ngrams
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import CFG
from nltk.corpus import wordnet
from nltk.corpus import wordnet



input_text = input("enter question: ")

def tokenize_input(input_text): # this function breaks down individual words and converts them to lowercase
    return word_tokenize(input_text.lower())

def remove_stopwords(tokens): # function for removing common stopwords
    stop_words = set(stopwords.words('english'))
    return [input_text for input_text in input_text if input_text not in stop_words]

def stem_words(token): # a function that stems words for faster processing
    stemmer = PorterStemmer()
    return [stemmer.stem(input_text) for input_text in token]

def lemmatize_words(token): # a function that lemmatizing words for better accuracy 
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(input_text) for input_text in token]

def bag_of_words(tokenized_input, vocabulary):
    bag = np.zeros(len(vocabulary))
    for word in tokenized_input:
        if word in vocabulary:
            index = vocabulary.index(word)
            bag[index] += 1
    return bag

#def classify(input_text, known_intents):
    #for intent, keywords in known_intent
