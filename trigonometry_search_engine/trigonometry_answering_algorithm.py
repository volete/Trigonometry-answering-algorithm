import math
import customtkinter
import numpy as np
import nltk
import sqlite3
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


# objective: a trigonometry calculator.

#TODO: create sql db

############################### Database configuration ##########################################

class Trig_questions:
    def __init__(self, id, question, difficulty, answer):
        self.id = id
        self.question = question
        self.difficulty = difficulty
        self.answer = answer

    def return_array(self):
        return (self.question, self.difficulty, self.answer)
    Trig_questions = 'questions'

    def to_insert_array(self):
        return (self.question, self.difficulty, self.answer)

class Database:


        def __init__(self, db_file):
            self.db_file = db_file
            self.create_connection(self.db_file)

        def create_connection(self, db_file): #create a connection
            self.conn = sqlite3.connect('trig_questions.db') #establishing a connection to the sqlite db
            cursor = self.conn.cursor() #Creates a cursor to interact with the db
            cursor.execute("CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY, question TEXT, difficulty TEXT, answer TEXT)")
            self.conn.commit() 
            self.conn.close()     

        def insert_into_db(self, trig_questions:Trig_questions): #inserting values into db
            self.conn = sqlite3.connect(self.db_file)
            sql = '''INSERT INTO questions(question, difficulty, answer)
                        VALUES(?,?,?)'''  
            self.conn.execute(sql,trig_questions.to_insert_array())
            self.conn.commit()

        def print_text_from_db(self): #printing text from db for testing purposes
            self.conn = sqlite3.connect(self.db_file)
            cursor = self.conn.execute("select * from questions")
            for row in cursor:
                print(row)


################### natural language processing unit (NLPU) #################################################
input_text = input("enter question: ")

#def tokenize_input()

################# UI ###############################################################################


root = customtkinter.CTk()
root.mainloop()
