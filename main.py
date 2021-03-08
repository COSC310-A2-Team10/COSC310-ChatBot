import random
import generate as gen
import preprocessing as prep

question,answer=prep.loadCorpora()

print("preparing system.....")
embeddingList=gen.wordEmbedding(question)
print("The chatbbot is ready, Enter 'bye' to exit the system")
print("Hi I'm your chatbot let's chat!!")

while (True):
    userinput=input("Input:").lower()
    if userinput =="bye":
        listBye = ['see you','bye','bye-bye','good bye']
        replyBye = random.choice(listBye)
        print(replyBye)
        break
    elif userinput=="hi" or userinput=="hello":
        listHi = ['Hi!!','Hello!!','good to see you!','Hi there!']
        replyHi = random.choice(listHi)
        print(replyHi)
    else:
        gen.generate(userinput,embeddingList,answer)

