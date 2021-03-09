Download following libraries before running the code

pip install nltk
pip install -U spacy
python -m spacy download en_core_web_lg



How to run the code: run main.py

Data flow: Preprocessing.py => generate.py => main.py


some features:
1. the system can clean all punctuations in the sentence and convert sentence to lower case

2. the system can remove suffixes (e.g.playing and play) and 
convert all the words back to root form (e.g. apples and apple)

3. the system can clean all the words with not much meaning in the sentence (e.g. 'a', 'is') 


Therefore, you don't have to ask exactly the same questions as in the corpus,
but just the same meaning and keywords. 

examples:
Input:what is chemistry??  
the science of mixing chemicals.

Input:tell me about chemistry  
the science of mixing chemicals.


more examples in demo.png
