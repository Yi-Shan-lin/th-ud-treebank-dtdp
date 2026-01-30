# Taiwanese Hokkien UD Treebank

This repository contains a small-scale Universal Dependencies (UD) treebank
for Taiwanese Hokkien (Southern Min).

## Overview
- Language: Taiwanese Hokkien
- Annotation framework: Universal Dependencies
- Number of sentences: ~200
- Annotation level: POS + dependency relations
- Annotation method: manual annotation

## Motivation
Taiwanese Hokkien is a low-resource language.
This project explores whether cross-lingual dependency parsing models
trained on Mandarin Chinese can be transferred to Hokkien.

## Data
Annotated data is provided in CoNLL-U format `data/th_ud.conllu`.

## Experiments
We evaluate cross-lingual parsing transfer using the Stanford NLP library (Stanza),
with Mandarin UD models applied to Taiwanese Hokkien data, the result is provided in CoNLL-U format `data/pred`.

## Tools
- UD annotation
- Stanza
- Python

## Disclaimer
This dataset is created for academic and educational purposes only.