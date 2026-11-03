import pymupdf
import pandas as pd

dfs = []


def merge_tables(min, max):
    doc = pymupdf.open("../source/bncc.pdf")

    WIDTH = 842 * 2
    HEIGHT = 595

    new_pdf = pymupdf.open()
    page = new_pdf.new_page(width=842, height=HEIGHT)

    for i in range(min, max, 2):
        page.show_pdf_page(pymupdf.Rect(-1263, 0, WIDTH, HEIGHT), doc, i)
        page.show_pdf_page(pymupdf.Rect(-421, 0, WIDTH, HEIGHT), doc, i + 1)

    new_pdf.save("../generated/pdf_merged.pdf")
    doc = pymupdf.open("../generated/pdf_merged.pdf")
    page = doc[0]
    table = page.find_tables()
    if len(table.tables) <= 0:  # type: ignore
        return
    dfs.append(table.tables[0].to_pandas())  # type: ignore


initial_page = 5
last_page = 74
for i in range(initial_page, last_page, 2):
    merge_tables(i, i + 1)

df = pd.concat(dfs, ignore_index=True)

df = df.replace(r"\n", " ", regex=True)
df["EIXO"] = df["EIXO"].ffill()
df["OBJETO DE CONHECIMENTO"] = df["OBJETO DE CONHECIMENTO"].ffill()
df["HABILIDADE"] = df["HABILIDADE"].ffill()
df["EXEMPLOS"] = df["EXEMPLOS"].ffill()
df["COMPETÊNCIA ESPECÍFICA"] = df["COMPETÊNCIA ESPECÍFICA"].ffill()
df["EXPLICAÇÃO DA HABILIDADE"] = df["EXPLICAÇÃO DA HABILIDADE"].ffill()
df["EXPLICAÇÃO DA HABILIDADE EXEMPLOS"] = df[
    "EXPLICAÇÃO DA HABILIDADE EXEMPLOS"
].ffill()

df = df.rename(columns={"Col2": "OBJETO DE CONHECIMENTO DESDOBRAMENTO"})
df = df.rename(columns={"Col4": "HABILIDADE_2"})
df["OBJETO DE CONHECIMENTO DESDOBRAMENTO"] = df[
    "OBJETO DE CONHECIMENTO DESDOBRAMENTO"
].ffill()


df = df.drop(columns="Col5")
df = df.drop(columns="Col3")


df.to_json("../generated/output.json", force_ascii=False, orient="records", indent=4)
