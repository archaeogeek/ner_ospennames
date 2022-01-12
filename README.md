# ner_ospennames
WIP: Named Entity Recognition in SpaCy with OS Open Names data

## Prep

Prep your osopennames data using something resembling the process here: https://gist.github.com/archaeogeek/d7a3c20a12147bab38e1c0e75f56c1f1

## Setup

Download or clone this repository.Note that if you receive errors relating to Git LFS you may need to install it- see https://git-lfs.github.com/ for instructions, and then additionally run 'git lfs pull' after cloning or pulling. Then set up a virtual environment, activate it, and install the requirements.

```
python3 -m venv .
source bin/activate

pip install -r requirements.txt
```

## To run

Download the standard model:

```
python3 -m spacy download en_core_web_sm

```

Assuming you followed the linked gist to prepare your osopennames data and it's in this folder as 'mergednameonly.jsonl' load the pipeline and then test it: 

```
python3 load_ukgeo.py
python3 test_ukgeo.py
```


