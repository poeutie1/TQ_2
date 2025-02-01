import re

path = '/Users/satorio/Desktop/TQ/Python/ortholog/tail.fasta36'

library_pattern = re.compile(r"Library:")

with open(path, 'r') as f:
    content = f.read()
for i in range(len(lines) - 1):  # 最後の行は次の行が存在しないため除外
    current_line = lines[i]
    next_line = lines[i + 1]

    # 現在の行が "3>>>" のような形式か確認
    prefix_match = prefix_pattern.search(current_line)
    identifier_match = identifier_pattern.search(current_line)

    if prefix_match and identifier_match:
        # 数値部分を取得して昇順チェック
        current_prefix = int(prefix_match.group(1))
        if current_prefix > previous_prefix and library_pattern.search(next_line):
            # 条件を満たす場合のみ抽出
            gene_id = identifier_match.group(1)  # 識別子1 (例: TthHB5002_00030)
            protein_name = identifier_match.group(2)  # 識別子2 (例: eno)
            extracted_results.append(f"Extracted ID: {gene_id}, Extracted Name: {protein_name}")
            previous_prefix = current_prefix  # 前の数値部分を更新

# 抽出結果の表示
for result in extracted_results:
    print(result)