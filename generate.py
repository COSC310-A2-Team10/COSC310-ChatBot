import preprocessing as prep
import en_core_web_lg
import spacy




def preprocess(sentence): # preprocess the sentence using preprocessing model
    clean=prep.cleanPunctuationAndLower(sentence)
    lemma=prep.Lemmatization(clean)
    spell=prep.cleanSW(lemma)
    return spell




def wordEmbedding(question): #change all questions in the corpora to vectors and store in a list
    embeddingList=[]
    nlp = en_core_web_lg.load()

    for x in range(len(question)):
        doc=nlp(preprocess(question[x]))
        embeddingList.append(doc)
    return embeddingList



def generate(intputSen,doc2,answer):
    Bestsimilarity=0
    index=0
    nlp = en_core_web_lg.load()
    doc1=nlp(preprocess(intputSen))
    similarity=0

    for x in range(len(doc2)):
        if doc2[x].vector_norm and doc1.vector_norm:
            similarity=doc1.similarity(doc2[x]) #compare the input sentence and questions stored in the list

        if similarity>Bestsimilarity: #store best similarity and the index in the answer list
            Bestsimilarity=similarity
            index=x
    if Bestsimilarity> 0.60: 
        # this is the threshold, so if this value is too high, then your input must
        #have a higher degree of similarity to the questions in the corpora
        print(answer[index])
    else:
        print("Sorry your question is not included in my database")


