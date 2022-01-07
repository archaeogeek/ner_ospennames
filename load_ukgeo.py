import spacy

nlp=spacy.load('en_core_web_sm')
print('loaded model')


with nlp.select_pipes(enable='ner'):
    ruler=nlp.add_pipe("entity_ruler", "osopennames", before="ner").from_disk("mergednameonly.jsonl")
print("finished loading pipeline")
nlp.to_disk("./pipeline/ukgeo")
print("saved model")

