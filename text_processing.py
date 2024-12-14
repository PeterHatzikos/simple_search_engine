import re
import nltk
from nltk.tokenize import * 
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Αρχικοποίηση της βιβλιοθήκης nltk (λήψη πόρων)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Λίστα με stop words
stop_words = set(nltk.corpus.stopwords.words('english'))

def stem_process(wiki_texts):
    stem_process={}
    for key, value in wiki_texts.items():
        content = value["content"]

        # Αφαίρεση ειδικών χαρακτήρων (κρατάμε μόνο αλφαριθμητικούς χαρακτήρες και κενά)
        content = re.sub('-',' ',content)
        content = re.sub('[^a-zA-Z0-9\s]', '', content)
        content = re.sub('\n',' ',content)
        # Tokenization
        words = word_tokenize(content)
        sentences = sent_tokenize(content)

        
        # Stemming
        stemmed_words = [stemmer.stem(word.lower()) for word in words]
    
        if key not in stem_process:
            stem_process[key]={}
            
        try:
        # Ενημέρωση του λεξικού με τα επεξεργασμένα δεδομένα
            stem_process[key]["tokens"] = words  # Τα tokens χωρίς ειδικούς χαρακτήρες
            stem_process[key]["stemmed_tokens"] = stemmed_words
            stem_process[key]["sentences"] = sentences
        except KeyError:
            print("couldnt find a match for the key: ",key )

    return stem_process

def NoStopWords(wiki_texts):
    smpl_process={}
    for key, value in wiki_texts.items():
        content = value["content"]

        # Αφαίρεση ειδικών χαρακτήρων (κρατάμε μόνο αλφαριθμητικούς χαρακτήρες και κενά)
        content = re.sub('-',' ',content)
        content = re.sub('[^a-zA-Z0-9\s]', '', content)
        content = re.sub('\n',' ',content)
        
       
        # Tokenization
        words = word_tokenize(content)
        sentences = sent_tokenize(content)

        # Αφαίρεση των stop words
        filtered_words = [word for word in words if word.lower() not in stop_words]
        
        if key not in smpl_process:
            smpl_process[key]={}
       
        try:
        # Ενημέρωση του λεξικού με τα επεξεργασμένα δεδομένα
            smpl_process[key]["tokens"] = words 
            smpl_process[key]["No-Stop-Words"] = filtered_words  # Τα tokens χωρίς stop words και ειδικούς χαρακτήρες
            smpl_process[key]["sentences"] = sentences
        except KeyError:
            print("couldnt find a match for the key: ",key )

    return smpl_process


def lemmatization_process(wiki_texts):
    lem_process={}
    for key, value in wiki_texts.items():
        content = value["content"]
     
        # Αφαίρεση ειδικών χαρακτήρων (κρατάμε μόνο αλφαριθμητικούς χαρακτήρες και κενά)
        content = re.sub('-',' ',content)
        content = re.sub('\n',' ',content)
        content = re.sub('[^a-zA-Z0-9\s]', '', content)

        # Tokenization
        words = word_tokenize(content)
        sentences = sent_tokenize(content)

     

        # Lemmatization
        lemmatized_words = [lemmatizer.lemmatize(word.lower()) for word in words]
        
        if key not in lem_process:
            lem_process[key]={}
            
        try:    
        # Ενημέρωση του λεξικού με τα επεξεργασμένα δεδομένα
            lem_process[key]["tokens"] = words  # Τα tokens χωρίς ειδικούς χαρακτήρες
            lem_process[key]["lemmatized_tokens"] = lemmatized_words
            lem_process[key]["sentences"] = sentences
        except KeyError:
            print("couldnt find a match for the key: ",key )
            
    return lem_process

