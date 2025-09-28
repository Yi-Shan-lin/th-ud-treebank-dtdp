from stanza.utils.conll import CoNLL

import stanza
stanza.download("zh-hant")
nlp = stanza.Pipeline("zh-hant")
sentences = []



with open("../data/th_ud.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        sentences.append(line)

print(len(sentences))


with open("../data/pred.conllu", "w", encoding="utf-8") as f:
    for i, sent in enumerate(sentences, start=1):
        doc = nlp(sent)
        f.write(f'# sent_id = {i}\n')
        f.write(f'# text = {sent}\n')
        conllu = "{:c}".format(doc)
        f.write(conllu + "\n")
        f.write("\n")
