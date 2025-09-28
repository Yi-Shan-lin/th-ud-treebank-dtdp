import stanza
stanza.download("zh-hant")
nlp = stanza.Pipeline("zh-hant", processors="tokenize,pos,lemma,depparse", tokenize_pretokenized=True)

sentences = []
with open("../data/th_ud.conllu", "r") as f:
    sent = []
    for line in f:
        if len(line.strip()) == 0:
            sentences.append(sent)
            sent = []
            continue
        if line.startswith("#"):
            continue
        cols = line.strip().split("\t")
        if len(cols) >2:
            sent.append(cols[1])


with open("../data/pred2.conllu", "w", encoding="utf-8") as f:
    for i, sent in enumerate(sentences, start=1):
        doc = nlp([sent])
        f.write(f'# sent_id = {i}\n')
        f.write(f"# text = {''.join(sent)}\n")
        conllu = "{:c}".format(doc)
        f.write(conllu + "\n")
        f.write("\n")
        


doc = nlp([sentences[0]])
for i, sentence in enumerate(doc.sentences):
    print(f'====== Sentence {i+1} tokens =======')
    print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')

print("{:C}".format(doc))

for i, sentence in enumerate(doc.sentences):
    print(sentence)

print(sentences[0])