# COSC310-Friend-ChatBot
![ChatbotImage](https://s3-eu-west-1.amazonaws.com/userlike-cdn-blog/do-i-need-a-chatbot/header-chat-box.png)

## About the project
This repository contains a programming project code for a chatbot that simulates a conversation between friends. 
A specific topic about soccer and some scattered topics are covered.

## Prepare stage
before we start running this code we need to download several libraries
```bash
pip install nltk
pip install -U spacy
python -m spacy download en_core_web_lg
pip install pyspellchecker
```

## How to run the code
run [main.py](https://github.com/COSC310-A2-Team10/COSC310-Friend-ChatBot/blob/main/main.py)

## Data flow
`preprocessing.py` --> `generate.py` --> `main.py`

## Some features
1. the system can clean all punctuations in the sentence and convert sentence to lower case

2. the system can remove suffixes (e.g.playing and play) and 
convert all the words back to root form (e.g. apples and apple)

3. the system can clean all the words with not much meaning in the sentence (e.g. 'a', 'is')

Therefore, you don't have to ask exactly the same questions as in the corpus,
but just the same meaning and keywords. :grinning:

## Sample output 
```bash
Input:what is chemistry??  
the science of mixing chemicals.
```
```bash
Input:tell me about chemistry  
the science of mixing chemicals.
```
```bash
...
```

### More examples:
