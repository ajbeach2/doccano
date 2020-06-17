import spacy

nlp = spacy.load("en_core_web_sm")


def built_in_ner(text, to_return):
    doc = nlp(text)
    
