import stanza
from stanza.models.common.doc import Document
stanza.download("zh-hant")
nlp = stanza.Pipeline("zh-hant", processors="depparse", depparse_pretagged=True)

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
        if len(cols) >= 6:  # 至少要有 FORM, LEMMA, UPOS, XPOS, FEATS
            token_dict = {
                "id": int(cols[0]),
                "text": cols[1],  # FORM
                "lemma": cols[2],  # LEMMA
                "upos": cols[3],  # UPOS
                "xpos": cols[4],  # XPOS
                "feats": "_"
            }
            sent.append(token_dict)


print(sentences[0])


with open("../data/pred3.conllu", "w", encoding="utf-8") as f:
    for i, sent in enumerate(sentences, start=1):
        doc = nlp(Document([sent]))
        f.write(f'# sent_id = {i}\n')
        f.write(f"# text = {''.join(tok['text'] for tok in sent)}\n")
        conllu = "{:c}".format(doc)
        f.write(conllu + "\n")
        f.write("\n")