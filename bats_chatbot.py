import random
import string
import requests
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) 
nltk.download('punkt')   #comment out after first use
nltk.download('wordnet') #comment out after first use

#Get data for chatbot
def get_file(url):
   fname = input("Enter file name you want ")
   response = requests.get(url)
   if response.status_code == 200:
      print("File downloaded successfully")
      with open(fname, "wb") as file:
         file.write(response.content)
   else: 
      print("Could not download file: ", response.status_code)
      fname = "-1"
   return fname

#Absolute keywords
#greeting
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# hospitality
HOSPITALITY_INPUTS = ("how are you", "how you doing", "whats up", "how are you doing")
HOSPITALITY_RESPONSES = ("Im doing fine", "Im great!", "Im good!")

def hospitality(sentence):
    for word in sentence.split():
        if word.lower() in HOSPITALITY_INPUTS:
            return random.choice(HOSPITALITY_RESPONSES)

# thanks
THANK_INPUTS = ("thanks", "thank you", "that's helpful", "thanks a lot!", "thank you so much")
THANK_RESPONSES = ["You are welcome", "No problem", "My pleasure"]

def thanks(sentence):
    for word in sentence.split():
        if word.lower() in THANK_INPUTS:
            return random.choice(THANK_RESPONSES)

#Processing        
lemmer = WordNetLemmatizer()
def LemTokens(word_tokens):
    return [lemmer.lemmatize(token) for token in word_tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def response(user_response):
    bot_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        bot_response=bot_response + "I am sorry! I don't understand you"
        return bot_response
    else:
        bot_response = bot_response + sent_tokens[idx]
        return bot_response

print("Chatbot online")
file_change = input("Use new data? ") #Only enter 'yes'
if file_change.lower() == 'yes':
    url = input("Enter url: ")
    fname = get_file(url)
else: 
    fname = input("Enter data file name: ")
with open(fname, 'r', encoding = 'UTF-8') as fh:
    raw = fh.read().lower() #reads the text file and converts it to lower case
activate = input("Activate bats? ").lower() #Only enter 'yes'
if activate == "yes":
    print("Activating bats")
    sent_tokens = nltk.sent_tokenize(raw) 
    word_tokens = nltk.word_tokenize(raw)
    flag=True
    print("Bats: Hello, I am Bats and I will answer your queries. If you wish to exit, type Bye!")
    while flag==True:
        user_response = input()
        user_response=user_response.lower()
        if user_response != 'bye':
            if greeting(user_response) != None:
                    print("Bats: "+greeting(user_response))
            elif hospitality(user_response) != None:
                    print("Bats: "+hospitality(user_response))
            elif thanks(user_response) != None:
                    print("Bats: "+thanks(user_response))
            else:
                print("Bats: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
        else:
            flag=False
            print("Bats: Bye")
            print("Deactivating Bats")
else: 
    print("Bats not activated")
