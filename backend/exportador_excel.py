import pandas as pd

def gerar_excel(dados):
    df = pd.DataFrame(dados["itens"])
    df["Categoria"] = df["Descrição"].apply(categorizar)
    arquivo = "/tmp/notas_exportadas.xlsx"
    df.to_excel(arquivo, index=False)
    return arquivo

def categorizar(descricao):
    desc = descricao.lower()
    if "cerveja" in desc or "vodka" in desc:
        return "Bebidas alcoólicas"
    if "maçã" in desc or "banana" in desc:
        return "Frutas"
    if "cenoura" in desc or "alface" in desc:
        return "Verduras"
    return "Outros"
