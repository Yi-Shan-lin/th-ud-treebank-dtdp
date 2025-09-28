import re

def tokenize_line(sent):
    sent = re.sub(r'\s+', ' ', sent.strip())
    return list(sent)


with open('../data/th_ud.txt', 'r') as f, open('../data/th_ud.conllu', 'w') as fout:
    for i, line in enumerate(f, start=1):
        line.strip()
        if not line:
            continue
        tokens = tokenize_line(line)
        fout.write(f'# sent_id = {i}\n')
        fout.write(f'# text = {line}')
        fout.write('# Chinese_text = \n')

        for j, token in enumerate(tokens, start=1):
            fout.write("\t".join([str(j), token, token] + 7 * ["_"]) + "\n")
        fout.write('\n')