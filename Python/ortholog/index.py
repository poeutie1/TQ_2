import re
import networkx as nx
import matplotlib.pyplot as plt

#要変更
path = '/Users/satorio/Desktop/TQ/Python/ortholog/tail.fasta36'

# フィルタリング対象の文字列リスト
filter_keywords = ['ys40', 'ytma', 'ymn1', 'y345', 'y377', 'yh03']

# 正規表現パターンの作成
pattern = re.compile(r'|'.join(filter_keywords), re.IGNORECASE)

#置換パターンの定義
replace_dict={"TthHB5002_00010": "5002","TthAA37_00010": "a307", "TthAA229_00010":"a229", "TT_C1608": "tth7",  "TthAA220_00010": "a220", "TthAA22_00010": "a202","TTHN1_01918": "nar1", "TthAA11_00010": "a101","TthHB5008_00010": "5008","Ththe16_0001": "tts6", "Ththe16_0001": "ak01", "TthHB5018_00010": "5018", "TthSNM66_00010": "sn66", "TthSNM17_00010": "sn17",  "TTHA1973": "ttj8" , "K7H19_00005": "n1x8", "TthSNM76_00010": "sn76","JCM10941_00010": "ls81", "TthSNM33_00010": "sn33", "TthSNM11_00010": "sn11"}

# ファイルの読み込み
with open(path, 'r') as f:
    content = f.read()




if content:
    # 正規表現パターンの定義
    best_scores_pattern = re.compile(r"The best scores are:(.*?)(?:\n>>|\n\n|\Z)", re.DOTALL)
    matches = best_scores_pattern.findall(content)

    if matches:
        # 結果の表示
        for i, match in enumerate(matches):
            # 各行の処理
            filtered_lines = []
            for line in match.splitlines():
                # 'opt bits' で始まる行を除外
                if line.strip().startswith('opt bits'):
                    continue
                # 括弧内の数値部分を削除
                line = re.sub(r'\(\s*\d+\s*\)', '', line)
                
                # フィルタリング対象の文字列を含む行を除外
                if pattern.search(line):
                    continue
                # 不要なスペースを削除して整形（ここいるの？）

                line = ' '.join(line.split())
                filtered_lines.append(line)

                #三つ目の部位データを削除の過程

                #真ん中の文字列を菌株codeに変換する過程
                line = ["TthHB5002_00010" if "TthHB5002_00010"=="TthHB5002_00010" else i for i in line ]
                #内部の数字データ二つを削除する過程

            # フィルタリングされた行を結合
            filtered_match = "\n".join(filtered_lines)
            print(f"{filtered_match}\n")
    else:
        print("No matches found.")
else:
    print("No content to process.")

    #Evalueだけにフィルタリングができていない

#有向グラフオブジェクトの生成(無向グラフでOK)
class GraphD:
    def __init__(self) -> None:
        self.G = nx.DiGraph()
graphD = GraphD()
graphD.G.add_nodes_from([i+1 for i in range(22)])
#ここってラベル番号が表示されてるっぽい
graphD.G.add_edges_from([(i,j) for i in range(1,22) for j in range(22, 0, -1) if i !=j ])
#重みに応じて色を変更する(ここなんか動かないのでコメントアウトとして保存しておく)
#weights = nx.get_edge_attributes(graphD.G, 'weight').values()
#nx.draw_networkx(graphD.G, edge_color = weights)

#グラフ可視化
nx.draw(graphD.G, with_labels = True)
plt.show()
