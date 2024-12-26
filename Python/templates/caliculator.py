import re 
data = """" Statistics:  Expectation_n fit: rho(ln(x))= 5.8427+/-0.000734; mu= 6.3285+/- 0.039
 mean_var=40.3353+/- 9.115, 0's: 0 Z-trim(107.6): 3  B-trim: 3 in 1/38
 Lambda= 0.201944
 statistics sampled from 7114 (7117) to 7114 sequences
Algorithm: FASTA (3.8 Nov 2011) [optimized]
Parameters: BL50 matrix (15:-5), open/ext: -10/-2
 ktup: 2, E-join: 1 (0.768), E-opt: 0.2 (0.402), width:  16
 Scan time:  0.440

The best scores are:                                      opt bits E(67887)
ys40|YS40_170|no_data hypothetical protein         (  87)  568 171.1 1.6e-43
ytma|TMA_168|no_data hypothetical protein          (  87)  568 171.1 1.6e-43
y40i|PGDDIFCJ_00177|no_data hypothetical protein   (  87)  562 169.3 5.5e-43

>>ys40|YS40_170|no_data hypothetical protein              (87 aa)
 initn: 568 init1: 568 opt: 568  Z-score: 900.4  bits: 171.1 E(67887): 1.6e-43
Smith-Waterman score: 568; 100.0% identity (100.0% similar) in 87 aa overlap (1-87:1-87)
"""
pattern = r"(The best scores are:.*?)(?:\n{2,})"
match = re.search(pattern, data, re.DOTALL)


if match:
    result = match.group(1)
    print(result)
else:
    print("該当するデータが見つかりませんでした。")
