import spacy

nlp=spacy.load("./pipeline/ukgeo")

doc = nlp("Richard Burton visited Stack of the Riffars in 2002")
print([(ent.text, ent.label_) for ent in doc.ents])
