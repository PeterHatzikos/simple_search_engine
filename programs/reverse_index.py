# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:16:56 2024

@author: Petros
"""

def create_inverted_index_stemmed(processed_texts):
    """
    Δημιουργεί αντεστραμμένο ευρετήριο από τα επεξεργασμένα δεδομένα,
    εξασφαλίζοντας ότι κάθε doc_id εμφανίζεται μόνο μία φορά.
    """
    inverted_index = {}  # Λεξικό για αποθήκευση του ανεστραμμένου ευρετηρίου

    for doc_id, data in processed_texts.items():
        # Παίρνουμε τα stem tokens από τα επεξεργασμένα δεδομένα
        tokens = data.get("stemmed_tokens", [])

        for token in tokens:
            if token not in inverted_index:
                inverted_index[token] = set()  # Χρησιμοποιούμε σύνολο για μοναδικότητα
            inverted_index[token].add(doc_id)  # Προσθέτουμε το doc_id στο σύνολο του token

    # Μετατροπή των συνόλων σε λίστες για αποθήκευση σε JSON
    inverted_index = {token: list(doc_ids) for token, doc_ids in inverted_index.items()}

    return inverted_index


