import tkinter as tk
import webbrowser
import os
from tkinter import messagebox

def abrir_link(url):
    webbrowser.open(url)

def abrir_programa(caminho, download_url):
    try:
        os.startfile(caminho)
    except FileNotFoundError:
        resposta = messagebox.askyesno("Programa não encontrado", f"O programa {caminho} não foi encontrado. Deseja baixar?")
        if resposta:
            webbrowser.open(download_url)
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o programa. Erro: {e}")

# Criando a interface
tela = tk.Tk()
tela.title("Finance Hub")
tela.geometry("500x700")
tela.configure(bg="#f0f0f0")

# Título
titulo = tk.Label(tela, text="Finance Hub", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#2e3f5b")
titulo.pack(pady=10)

# Seção de Links Principais
links_principais = [
    ("Portal Principal do SharePoint", "https://www.microsoft.com/pt-br/microsoft-365/sharepoint/collaboration"),
    ("Power BI - Página Principal", "https://powerbi.microsoft.com/pt-br/"),
    ("Outlook - Acesse seu e-mail", "https://outlook.live.com"),
]
for nome, url in links_principais:
    btn = tk.Button(tela, text=nome, command=lambda u=url: abrir_link(u), width=50, bg="#1e4d7d", fg="white")
    btn.pack(pady=2)

# Seção de Softwares Contábeis e Financeiros
softwares = [
    ("Excel", "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE", "https://www.microsoft.com/pt-br/microsoft-365/excel"),
    ("Word", "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE", "https://www.microsoft.com/pt-br/microsoft-365/word"),
    ("TOTVS", "C:\\TOTVS\\totvs.exe", "https://www.totvs.com"),
    ("SAP", "C:\\SAP\\sap.exe", "https://www.sap.com/brazil/index.html"),
    ("Domínio Contábil", "C:\\Dominio\\dominio.exe", "https://www.thomsonreuters.com.br/pt/dominio.html"),
    ("Alterdata", "C:\\Alterdata\\alterdata.exe", "https://www.alterdata.com.br"),
    ("Omie", "C:\\Omie\\omie.exe", "https://www.omie.com.br"),
    ("Calima", "C:\\Calima\\calima.exe", "https://www.calimaerp.com"),
]
for nome, caminho, download_url in softwares:
    btn = tk.Button(tela, text=nome, command=lambda c=caminho, d=download_url: abrir_programa(c, d), width=50, bg="#4a7abc", fg="white")
    btn.pack(pady=2)

# Seção de Sites e Portais Oficiais
sites = [
    ("e-CAC (Receita Federal)", "https://cav.receita.fazenda.gov.br/autenticacao/login"),
    ("SEFAZ (Secretaria da Fazenda)", "https://www.nfe.fazenda.gov.br/portal"),
    ("Conectividade Social (Caixa)", "https://conectividade.caixa.gov.br"),
    ("SPED (Sistema Público de Escrituração Digital)", "https://sped.rfb.gov.br"),
    ("Banco Central (BACEN)", "https://www.bcb.gov.br"),
    ("B3 - Bolsa de Valores", "https://www.b3.com.br"),
    ("Tesouro Direto", "https://www.tesourodireto.com.br"),
]
for nome, url in sites:
    btn = tk.Button(tela, text=nome, command=lambda u=url: abrir_link(u), width=50, bg="#2e3f5b", fg="white")
    btn.pack(pady=2)

# Seção de Automação e Gestão de Processos
automacao = [
    ("UiPath", "C:\\UiPath\\uipath.exe", "https://www.uipath.com/pt/"),
    ("Power Automate", "C:\\PowerAutomate\\powerautomate.exe", "https://powerautomate.microsoft.com/pt-br/"),
    ("Automação Domínio", "C:\\DominioAutomacao\\dominioauto.exe", "https://www.thomsonreuters.com.br/pt/dominio.html"),
]
for nome, caminho, download_url in automacao:
    btn = tk.Button(tela, text=nome, command=lambda c=caminho, d=download_url: abrir_programa(c, d), width=50, bg="#556b2f", fg="white")
    btn.pack(pady=2)

# Seção de Ferramentas Bancárias e Pagamentos
bancos = [
    ("Banco do Brasil", "https://www.bb.com.br"),
    ("Itaú Empresas", "https://www.itau.com.br/empresas/"),
    ("Bradesco Net Empresa", "https://banco.bradesco/html/classic/produtos-servicos/para-sua-empresa/net-empresa.shtm"),
    ("Santander Empresas", "https://www.santander.com.br/empresas"),
    ("PagSeguro", "https://pagseguro.uol.com.br"),
    ("Mercado Pago", "https://www.mercadopago.com.br"),
    ("PIX (Banco Central)", "https://www.bcb.gov.br/estabilidadefinanceira/pix"),
]
for nome, url in bancos:
    btn = tk.Button(tela, text=nome, command=lambda u=url: abrir_link(u), width=50, bg="#8b0000", fg="white")
    btn.pack(pady=2)

# Rodando a interface
tela.mainloop()