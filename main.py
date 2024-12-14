import os
from data_collection import collect_wikipedia_data
from text_processing import stem_process , NoStopWords ,lemmatization_process
from reverse_index import create_inverted_index_stemmed
import json

def main():
    # Δημιουργία του φακέλου "data" αν δεν υπάρχει
    if not os.path.exists("data"):
        os.makedirs("data")

    # Συλλογή δεδομένων
    wiki_texts = collect_wikipedia_data()
   

    # Αποθήκευση σε JSON
    with open("data/wikipedia_data_source.json", "w", encoding="utf-8") as json_file:
        json.dump(wiki_texts, json_file, ensure_ascii=False, indent=4)
        
    print("Τα δεδομένα αποθηκεύτηκαν στο αρχείο 'wikipedia_data_source.json'")
    
    # Προεπεξεργασία δεδομένων με stemming 
    stemmed_texts = stem_process(wiki_texts)
    
    with open("data/stemmed_texts.json", "w", encoding="utf-8") as json_file:
       json.dump(stemmed_texts, json_file, ensure_ascii=False, indent=2)
        

    print("Τα δεδομένα αποθηκεύτηκαν στο αρχείο 'stemmed_texts.json'")
    
    # Προεπεξεργασία δεδομένων χωρίς stemming / lemmatization 
    smple_texts = NoStopWords(wiki_texts)
    
    with open("data/NoStopWord_texts.json", "w", encoding="utf-8") as json_file:
        json.dump(smple_texts, json_file, ensure_ascii=False, indent=2)

    print("Τα δεδομένα αποθηκεύτηκαν στο αρχείο 'NoStopWord_texts.json'")

    # Προεπεξεργασία δεδομένων με lemmatization
    lemm_texts = lemmatization_process(wiki_texts)

    with open("data/Lemmatized_texts.json", "w", encoding="utf-8") as json_file:
        json.dump(lemm_texts, json_file, ensure_ascii=False, indent=2)

    print("Τα δεδομένα αποθηκεύτηκαν στο αρχείο 'Lemmatized_texts.json'")

    # δημιουργία ευρετηρίου 
    i_index = create_inverted_index_stemmed(stemmed_texts)
    
    with open("data/inverted_index.json", "w", encoding="utf-8") as json_file:
        json.dump(i_index, json_file, ensure_ascii=False, indent=2)

    print("Τα δεδομένα αποθηκεύτηκαν στο αρχείο 'inverted_index.json'")

if __name__ == "__main__":
    main()
