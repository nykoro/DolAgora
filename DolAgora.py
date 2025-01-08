import requests
import tkinter as tk
import time

#COTAÇÃO - inicio

link = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='01-08-2025'&$top=1&$format=json&$select=cotacaoVenda"
requisicao = requests.get(link)
dolar = requisicao.json()
cotacao = dolar["value"][0]["cotacaoVenda"]
cotacaoFormatada = f"{cotacao:.2f}" #formatação da cotação 
print(cotacaoFormatada)

#COTAÇÃO - fim

#criar janela - inicio

janela = tk.Tk()
janela.title("DolAgora")
janela.geometry("220x50")
janela.resizable(False, False)
titulo = tk.Label(janela, text="Dólar Agora: " f"R${cotacaoFormatada}" , font=("Arial", 16))
titulo.pack(pady=10)
janela.mainloop()


#criar janela - fim