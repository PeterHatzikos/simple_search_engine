import re
import nltk
from nltk.tokenize import * 
from nltk.stem import PorterStemmer, WordNetLemmatizer

# initializing the nltk library (downloading resources)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# list with stop words
stop_words = set(nltk.corpus.stopwords.words('english'))

def stem_process(wiki_texts):
    stem_process={}
    for key, value in wiki_texts.items():
        content = value["content"]

        # removal of special characters (we keep letters , numbers and gaps/spaces)
        content = re.sub('-',' ',content)
        content = re.sub('[^a-zA-Z0-9\s]', '', content)
        content = re.sub('\n',' ',content)
        # Tokenization
        words = word_tokenize(content)
        sentences = sent_tokenize(content)

        
        # Stemming
        stemmed_words = [stemmer.stem(word.lower()) for word in words]
    
        if key not in stem_process: # initializing dictionaries per key
            stem_process[key]={}
            
        try:
        # updating dictionary with processed data
            stem_process[key]["tokens"] = words 
            stem_process[key]["stemmed_tokens"] = stemmed_words
            stem_process[key]["sentences"] = sentences
        except KeyError:
            print("couldnt find a match for the key: ",key )

    return stem_process

def NoStopWords(wiki_texts):
    smpl_process={}
    for key, value in wiki_texts.items():
        content = value["content"]

        # removal of special characters (we keep letters , numbers and gaps/spaces)
        content = re.sub('-',' ',content)
        content = re.sub('[^a-zA-Z0-9\s]', '', content)
        content = re.sub('\n',' ',content)
        
       
        # Tokenization
        words = word_tokenize(content)
        sentences = sent_tokenize(content)

        # removal of stop words
        filtered_words = [word for word in words if word.lower() not in stop_words]
        
        if key not in smpl_process: # initializing dictionaries per key
            smpl_process[key]={}
       
        try:
        # updating dictionary with processed data
            smpl_process[key]["tokens"] = words 
            smpl_process[key]["No-Stop-Words"] = filtered_words  
            smpl_process[key]["sentences"] = sentences
        except KeyError:
            print("couldnt find a match for the key: ",key )

    return smpl_process


def lemmatization_process(wiki_texts):
    lem_process={}
    for key, value in wiki_texts.items():
        content = value["content"]
     
        # removal of special characters (we keep letters , numbers and gaps/spaces)
        content = re.sub('-',' ',content)
        content = re.sub('\n',' ',content)
        content = re.sub('[^a-zA-Z0-9\s]', '', content)

        # Tokenization
        words = word_tokenize(content)
        sentences = sent_tokenize(content)

     

        # Lemmatization
        lemmatized_words = [lemmatizer.lemmatize(word.lower()) for word in words]
        
        if key not in lem_process: # initializing dictionaries per key
            lem_process[key]={}
            
        try:    
        # updating dictionary with processed data
            lem_process[key]["tokens"] = words  # Τα tokens χωρίς ειδικούς χαρακτήρες
            lem_process[key]["lemmatized_tokens"] = lemmatized_words
            lem_process[key]["sentences"] = sentences
        except KeyError:
            print("couldnt find a match for the key: ",key )
            
    return lem_process

