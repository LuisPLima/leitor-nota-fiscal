from playwright.sync_api import sync_playwright

def buscar_dados_fiscais(codigo):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.nfce.fazenda.sp.gov.br/ConsultaPublica")
        page.fill('#codigo', codigo)
        page.click('#btnConsultar')
        page.wait_for_selector('.dadosNota')
        dados = page.evaluate('() => document.querySelector(".dadosNota").innerText')
        browser.close()
        return dados
