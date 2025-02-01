import re
import networkx as nx
import matplotlib.pyplot as plt

# 要変更
path = '/Users/satorio/Desktop/TQ/Python/ortholog/tail.fasta36'

# phagesリスト
filter_keywords = ['ys40', 'ytma', 'ymn1', 'y345', 'y377', 'yh03', 'yplo', 'ypma', 'y40i', 'y426', 'ypfa', 'yg20', 'yn93', 'ypko', 'yh16']

# 正規表現パターンの作成
pattern = re.compile(r'|'.join(filter_keywords), re.IGNORECASE)
identifier_pattern = re.compile(r"\|([A-Za-z0-9_]+)\|([a-zA-Z0-9_]+)")
library_pattern = re.compile(r"Library:")
prefix_pattern = re.compile(r"(\d+)>>>")  # 昇順チェック用

# ファイルの読み込み
with open(path, 'r') as f:
    content = f.read()

if content:
    # 正規表現パターンの定義
    best_scores_pattern = re.compile(r"The best scores are:(.*?)(?:\n>>|\n\n|\Z)", re.DOTALL)
    matches = best_scores_pattern.findall(content)

    if matches:
        previous_prefix = 0  # 昇順チェック用
        for match in matches:
            # 各行の処理
            lines = match.splitlines()
            filtered_lines = []
            extracted_results = []

            for i, line in enumerate(lines):
                # 'opt bits' で始まる行を除外
                if line.strip().startswith('opt bits'):
                    continue

                # 括弧内の数値部分を削除
                line = re.sub(r'\(\s*\d+\s*\)', '', line)

                # フィルタリング対象の文字列を含む行を除外
                if pattern.search(line):
                    continue

                # 不要なスペースを削除して整形
                line = ' '.join(line.split())
                filtered_lines.append(line)

                # 昇順チェックと識別子の抽出
                prefix_match = prefix_pattern.search(line)
                identifier_match = identifier_pattern.search(line)

                if prefix_match and identifier_match:
                    current_prefix = int(prefix_match.group(1))  # 数値部分を取得
                    # 昇順確認と次の行にLibrary:があるかを確認
                    if current_prefix > previous_prefix and i + 1 < len(lines) and library_pattern.search(lines[i + 1]):
                        gene_id = identifier_match.group(1)
                        protein_name = identifier_match.group(2)
                        extracted_results.append(f"Extracted ID: {gene_id}, Extracted Name: {protein_name}")
                        previous_prefix = current_prefix  # 昇順の値を更新

            # フィルタリングされた行を結合
            filtered_match = "\n".join(filtered_lines)

            # 出力
            if extracted_results:
                print("\n".join(extracted_results))
            print(filtered_match)
            print("-" * 40)  # 区切り線
    else:
        print("No matches found.")
else:
    print("No content to process.")

# 有向グラフオブジェクトの生成(無向グラフでOK)
class GraphD:
    def __init__(self) -> None:
        self.G = nx.DiGraph()
graphD = GraphD()
graphD.G.add_nodes_from([i + 1 for i in range(22)])
# エッジを追加
graphD.G.add_edges_from([(i, j) for i in range(1, 22) for j in range(22, 0, -1) if i != j])

# グラフ可視化
nx.draw(graphD.G, with_labels=True)
plt.show()
