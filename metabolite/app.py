import pandas as pd
import json
import sys

def process_excel_file():
    df = pd.read_excel(
        '/Users/satorio/Downloads/ThermusQ-MTQ-Metabolite-Standard-240904-18YB.xlsx',
        #↑アドレス後で変更
        skiprows=[1, 227],  
        usecols=[1, 2, 3, 4, 5, 7, 11, 13, 15, 19, 20, 21, 22, 23, 24]
    )
    df = df.dropna(subset=['MTQID']) 

    nested_data = {}
    for _, row in df.iterrows():
        category = row.get("Category", "Unknown")
        subcategory = row.get("LV2-Category", "Unknown")
        molecule_info = {
            "MTQID": str(row.get("MTQID", "")),
            "Metabolite Name": str(row.get("Metabolite Name", "")),
            "PubChem(CID)": str(row.get("PubChem(CID)", "")),
            "Abbr.": str(row.get("Abbr.", "")),
            "Fomula": str(row.get("Fomula", "")),
            "Charge": str(row.get("Charge", "")),
            "Monoisotopic Mass": str(row.get("Monoisotopic Mass", "")),
            "ParentID": str(row.get("ParentID", "")),
            "T": str(row.get("T", "")),
            "Rep": str(row.get("Rep", "")),
            "General": str(row.get("General", "")),
            "ChEBI": str(row.get("ChEBI", "")),
            "alt-Category (C-D, 複数可)": str(row.get("alt-Category", ""))
        }

        if category not in nested_data:
            nested_data[category] = {}
        if subcategory not in nested_data[category]:
            nested_data[category][subcategory] = []
        nested_data[category][subcategory].append(molecule_info)

    print(json.dumps(nested_data, ensure_ascii=False, indent=4))
    #JSONファイルに変更、これをphpで呼んでる

if __name__ == "__main__":
    process_excel_file()

