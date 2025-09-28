from collections import Counter
import pandas as pd

conllu_file = "../data/th_ud.conllu"

deps = []

with open(conllu_file, "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("#") or not line.strip():
            continue
        cols = line.strip().split("\t")
        if len(cols) >= 8:
            deps.append(cols[7])  # 第8欄是 DEPREL

counter = Counter(deps)
total = sum(counter.values())

# 轉成 DataFrame
df = pd.DataFrame(counter.items(), columns=["Deprel", "Count"])
df["Percentage"] = df["Count"] / total * 100
df = df.sort_values(by="Count", ascending=False)

print(df)

# 如果要輸出 LaTeX 表格
print(df.to_latex(index=False, float_format="%.2f"))