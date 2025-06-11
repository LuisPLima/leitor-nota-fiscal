from fastapi import FastAPI, UploadFile
from leitura_qrcode import ler_qrcode
from robo_consulta import buscar_dados_fiscais
from exportador_excel import gerar_excel

app = FastAPI()

@app.post("/leitor/qrcode/")
async def leitor_qrcode(file: UploadFile):
    codigo = ler_qrcode(await file.read())
    return {"codigo": codigo}

@app.get("/consulta/")
async def consulta_documento(codigo: str):
    dados = buscar_dados_fiscais(codigo)
    return dados

@app.post("/exportar/")
async def exportar_excel(dados: dict):
    caminho = gerar_excel(dados)
    return {"arquivo": caminho}
