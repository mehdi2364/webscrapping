import spacy

def recognize_city(phrase):
    # Load spaCy English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the input phrase
    doc = nlp(phrase)

    # Extract entities (cities) from the processed document
    cities = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    return cities
