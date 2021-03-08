from spellchecker import SpellChecker

import string

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize as tokenize 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



def loadCorpora():# this function will load corpora and return 2 lists

    question=[]
    answer=[]
    with open('Corpora.txt')as file:
        for sent in file.readlines():
            terms=sent.split("***")
            question.append(terms[0])
            answer.append(terms[1])

    return question,answer



def cleanPunctuationAndLower(sentence):
    clean=cleanPunctuation(sentence)#clean all punctuations in the sentence

    clean=clean.lower()#convert everything to lowercase
    return clean


def cleanPunctuation(sentence):
    clean=sentence.translate(str.maketrans('','',string.punctuation))#clean all punctuations in the sentence
    return clean




def Lemmatization(inputSen):
    lemmd=[]
    lemmatizer= WordNetLemmatizer()
    token=inputSen.split()
    for x in token:
        lemmd.append(lemmatizer.lemmatize(x)) #lemmatization change all the words back to root form e.g. apples and apple
    ret=(" ").join(lemmd)
    return ret


def cleanSW(inputSen):

    tokens=tokenize(inputSen)
    clean_tokens=[x for x in tokens if not x in stopwords.words()]# clean all the words with not much meaning in the sentence like 'a', 'is'
    clean=" ".join(clean_tokens) 
    return clean


