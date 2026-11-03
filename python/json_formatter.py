import json

path = "../generated/bncc_computacao_rest_api.json"
original_data = {}
with open(path, "r", encoding="utf-8") as f:
    original_data = json.load(f)

new_data = {"ultima_atualizacao": "28/06/2026", "dados": []}


def ensino_infantil(new_data, data):
    is_EI = data["OBJETIVO DE APRENDIZAGEM"]
    if is_EI != None:
        new_data["dados"].append(
            {
                "codigo": f"{data["OBJETIVO DE APRENDIZAGEM"][1:9]}",
                "etapa": f"{data["OBJETIVO DE APRENDIZAGEM"][1:3]}",
                "ano": f"{int(data["OBJETIVO DE APRENDIZAGEM"][3:5])}",
                "componente": f"Computação",
                "eixo": f"{data["EIXO"]}",
                "objeto_conhecimento": f"{data["OBJETO DE CONHECIMENTO"] if not type(None) else ""}",
                "subtema": "",
                "competencia": "",
                "habilidade": f"{data["OBJETIVO DE APRENDIZAGEM"][11:]}",
                "explicacao": "",
                "exemplos": f"{data["EXEMPLOS"]}",
            }
        )


def ensino_fund_inicial(new_data, data):
    if data["HABILIDADE"] == (None):
        return
    if "EF" not in data["HABILIDADE"][:5]:
        return
    # if is_EI != None:
    if int(data["HABILIDADE"][4:5]) <= 5:
        new_data["dados"].append(
            {
                "codigo": f"{data["HABILIDADE"][1:9]}",
                "etapa": f"{data["HABILIDADE"][1:3]}",
                "ano": f"{int(data["HABILIDADE"][3:5])}",
                "componente": f"Computação",
                "eixo": f"{data["EIXO"]}",
                "objeto_conhecimento": f"{data["OBJETO DE CONHECIMENTO"] if not type(None) else ""}",
                "subtema": "",
                "competencia": "",
                "habilidade": f"{data["HABILIDADE"][11:]}",
                "explicacao": "",
                "exemplos": f"{data["EXEMPLOS"]}",
            }
        )


def ensino_fund_final(new_data, data):
    if data["HABILIDADE_2"] == (None):
        return
    if "EF" not in data["HABILIDADE_2"][:5]:
        return
    # if is_EI != None:
    if int(data["HABILIDADE_2"][4:5]) > 5:
        new_data["dados"].append(
            {
                "codigo": f"{data["HABILIDADE_2"][1:9]}",
                "etapa": f"{data["HABILIDADE_2"][1:3]}",
                "ano": f"{int(data["HABILIDADE_2"][3:5])}",
                "componente": f"Computação",
                "eixo": f"{data["EIXO"]}",
                "objeto_conhecimento": f"{data["OBJETO DE CONHECIMENTO"] if data["OBJETO DE CONHECIMENTO"] != None else ""}",
                "subtema": f"{data["OBJETO DE CONHECIMENTO DESDOBRAMENTO"]}",
                "competencia": f"{data["HABILIDADE"]}",
                "habilidade": f"{data["HABILIDADE_2"][11:]}",
                "explicacao": f"{data["EXPLICAÇÃO DA HABILIDADE EXEMPLOS"] if data["EXPLICAÇÃO DA HABILIDADE EXEMPLOS"] != None else data["EXPLICAÇÃO DA HABILIDADE"] }",
                "exemplos": f"{data["EXEMPLOS"]}",
            }
        )


def ensino_medio(new_data, data):
    if data["HABILIDADE"] == (None):
        return
    if "EM" not in data["HABILIDADE"][:5]:
        return
        # if is_EI != None:
    new_data["dados"].append(
        {
            "codigo": f"{data["HABILIDADE"][1:9]}",
            "etapa": f"{data["HABILIDADE"][1:3]}",
            "ano": f"{int(data["HABILIDADE"][3:5])}",
            "componente": f"Computação",
            "eixo": "",
            "objeto_conhecimento": "",
            "subtema": "",
            "competencia": f"{data["COMPETÊNCIA ESPECÍFICA"]}",
            "habilidade": f"{data["HABILIDADE"][11:]}",
            "explicacao": f"{data["EXPLICAÇÃO DA HABILIDADE"]}",
            "exemplos": f"{data["EXEMPLOS"]}",
        }
    )


for data in original_data:
    ensino_infantil(new_data, data)
    ensino_fund_inicial(new_data, data)
    ensino_fund_final(new_data, data)
    ensino_medio(new_data, data)

example = []
for d in new_data["dados"]:
    example.append(d)

with open("../generated/bncc_computacao_rest_api.json", "w", encoding="utf-8") as j:
    j.writelines(json.dumps(example, indent=4, ensure_ascii=False))
