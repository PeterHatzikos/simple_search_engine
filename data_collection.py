# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:22:07 2024

@author: Simos
"""

import requests
from bs4 import BeautifulSoup

def collect_wikipedia_data():
    data_intake = []
    wiki_texts = {}  # Λεξικό για την αποθήκευση των δεδομένων

    # Προσθέτω συνδέσμους στη λίστα data_intake
    data_intake.append(requests.get('https://en.wikipedia.org/wiki/Watermelon'))
    data_intake.append(requests.get('https://en.wikipedia.org/wiki/Information_extraction'))
    data_intake.append(requests.get('https://en.wikipedia.org/wiki/Adam_Sandler'))
    data_intake.append(requests.get('https://en.wikipedia.org/wiki/Greek_War_of_Independence'))
    data_intake.append(requests.get('https://en.wikipedia.org/wiki/Animal_Farm'))
    

    # Επεξεργασία του HTML για την εξαγωγή του κειμένου
    for i, data in enumerate(data_intake):
        soup = BeautifulSoup(data.text, "html.parser")
        content = ""  # Αρχικοποίηση περιεχομένου
        for paragraph in soup.select('p'):
            for sup_search in paragraph.select('sup'): # οπου υπάρχει η λεζάντα " sup " 
                sup_search.decompose() # αφαίρεσε τη και μην διαβάσεις τα περιεχόμενα της
            content += paragraph.get_text()  # Εξαγωγή κειμένου

        # Αποθήκευση του περιεχομένου στο λεξικό
        wiki_texts[i] = {"title": f"Page {i + 1}", "content": content}

    return wiki_texts
