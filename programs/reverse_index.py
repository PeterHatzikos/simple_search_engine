# -*- coding: utf-8 -*-


def create_inverted_index_stemmed(processed_texts):
    """
    creates inverted index from the processed data , 
    guaranteeing that all do_id's are shown only once
    """
    inverted_index = {}  #  dictionary for saving the inverted index

    for doc_id, data in processed_texts.items():
        # take the stem tokens from the processed data
        tokens = data.get("stemmed_tokens", [])

        for token in tokens:
            if token not in inverted_index:
                inverted_index[token] = set()  # using sum for individuality
            inverted_index[token].add(doc_id)  # adding doc_id to the sum of token

    # changing the sums into list so that they get saved as JSON
    inverted_index = {token: list(doc_ids) for token, doc_ids in inverted_index.items()}

    return inverted_index


