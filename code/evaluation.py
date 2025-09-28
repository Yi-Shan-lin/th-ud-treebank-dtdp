from collections import Counter, defaultdict

def load_conllu(filename):
    """讀取 conllu 檔案，回傳句子 list，每句是一個 (id, head, deprel) 的 list"""
    sentences = []
    sent = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                if sent:
                    sentences.append(sent)
                    sent = []
                continue
            cols = line.split("\t")
            if len(cols) < 8:
                continue
            try:
                idx = int(cols[0])
                head = int(cols[6])
                deprel = cols[7]
                sent.append((idx, head, deprel))
            except ValueError:
                continue
    if sent:
        sentences.append(sent)
    return sentences

def evaluate_deprel(gold_file, pred_file):
    gold_sents = load_conllu(gold_file)
    pred_sents = load_conllu(pred_file)

    assert len(gold_sents) == len(pred_sents), "句子數量不一致！"

    counts = defaultdict(lambda: Counter())

    for gold, pred in zip(gold_sents, pred_sents):
        assert len(gold) == len(pred), "token 數量不一致"
        for (g_idx, g_head, g_rel), (p_idx, p_head, p_rel) in zip(gold, pred):
            assert g_idx == p_idx
            # 如果 head 也正確，則 deprel 才算完全正確
            if g_head == p_head and g_rel == p_rel:
                counts[g_rel]["tp"] += 1
            else:
                counts[p_rel]["fp"] += 1
                counts[g_rel]["fn"] += 1

    print(f"{'Deprel':10s} | {'Precision':>9} | {'Recall':>9} | {'F1':>9} | {'Support':>7}")
    print("-"*50)
    for rel, c in counts.items():
        tp, fp, fn = c["tp"], c["fp"], c["fn"]
        prec = tp / (tp + fp) if tp + fp > 0 else 0.0
        rec = tp / (tp + fn) if tp + fn > 0 else 0.0
        f1 = 2*prec*rec/(prec+rec) if prec+rec > 0 else 0.0
        support = tp + fn
        print(f"{rel:10s} | {prec:9.2f} | {rec:9.2f} | {f1:9.2f} | {support:7d}")

# 用法
evaluate_deprel("../data/th_ud.conllu", "data/pred3.conllu")