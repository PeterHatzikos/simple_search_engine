# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:22:07 2024
"""

import requests
from bs4 import BeautifulSoup

def collect_wikipedia_data():
    data_intake = []
    wiki_texts = {}  # dictionary for storing data

    # inserting links into list named data_intake
    data_intake.append(requests.get('https://en.wikipedia.org/wiki/Watermelon'))
    data_intake.append(requests.get('https://en.wikipedia.org/wiki/Information_extraction'))
    data_intake.append(requests.get('https://en.wikipedia.org/wiki/Adam_Sandler'))
    data_intake.append(requests.get('https://en.wikipedia.org/wiki/Greek_War_of_Independence'))
    data_intake.append(requests.get('https://en.wikipedia.org/wiki/Animal_Farm'))
    

    # processing the HTML to extract the needed texts
    for i, data in enumerate(data_intake):
        soup = BeautifulSoup(data.text, "html.parser")
        content = ""  # initialisation of contents
        for paragraph in soup.select('p'): # wherever there is the caption <p>
            for sup_search in paragraph.select('sup'): # wherever there is the caption" sup " 
                sup_search.decompose() #  remove it and dont read its contents
            content += paragraph.get_text()  # extracting texts

        # saving contents into dictionary
        wiki_texts[i] = {"title": f"Page {i + 1}", "content": content}

    return wiki_texts
