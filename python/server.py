import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
path = "../generated/bncc_computacao_rest_api.json"

origins = [
    "http://localhost:8000",  # React local development
    "http://127.0.0.1:3000",
    "https://yourfrontend.com",  # Production domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"msg": "root"}


@app.get("/habilidades")
def find_all_habilidades():
    bncc_habilidades = []

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for d in data:
            bncc_habilidades.append(
                {"codigo": d["codigo"], "habilidade": d["habilidade"]}
            )
    return bncc_habilidades


@app.get("/habilidades/{codigo}")
def find_habilidade(codigo: str):
    print(codigo)
    habilidade = {}
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for d in data:
            if d["codigo"] == codigo:
                print(d["codigo"])
                habilidade = d

    if habilidade == "":
        raise HTTPException(status_code=404, detail="habilidade não encontrada")
    return habilidade


@app.get("/habilidades/explicacao/")
def find_by_word_habilidades(q: str):
    explicacao = []
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for d in data:
            if q == "":
                return
            if q in d["explicacao"].lower():
                explicacao.append(d)
                # explicacao.append(
                #     {
                #         "codigo": d["codigo"],
                #         "etapa": d["etapa"],
                #         "explicacao": d["explicacao"],
                #     }
                # )

    if len(explicacao) < 1:
        raise HTTPException(status_code=404, detail="explicacao não encontrada")
    return explicacao


@app.get("/eixo")
def find_all_eixo():
    bncc_eixo = []

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        for d in data:
            if d["eixo"] != "":
                bncc_eixo.append(d["eixo"])
    return list(dict.fromkeys(bncc_eixo))


# with open("bncc_computacao.json", "r", encoding="utf-8") as data:
#     json_data = json.load(data)
#     for d in json_data:
#         print(d["EIXO"])
