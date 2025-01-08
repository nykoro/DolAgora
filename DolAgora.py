import requests
import tkinter as tk
from PIL import Image, ImageTk
import ctypes 

#COTAÇÃO - inicio
def atualizarCotacao():
    link = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='01-08-2025'&$top=1&$format=json&$select=cotacaoVenda"
    requisicao = requests.get(link)
    dolar = requisicao.json()
    cotacao = dolar["value"][0]["cotacaoVenda"]
    cotacaoFormatada = f"{cotacao:.2f}" #formatação da cotação 
    titulo.config(text="Dólar agora: "f"R${cotacaoFormatada}")
    janela.after(60000, atualizarCotacao) #Taxa de atualização da cotação em ms.

#COTAÇÃO - fim


#JANELA - inicio

janela = tk.Tk()
janela.title("DolAgora")
janela.geometry("220x50")
janela.resizable(False, False)
titulo = tk.Label(janela, text="" , font=("Arial", 16))
titulo.pack(pady=10)

iconPath = "C:../Icons/DolAgoraIcon.png" #formato PNG
iconImage = Image.open(iconPath)
iconPhoto = ImageTk.PhotoImage(iconImage)
janela.iconphoto(True, iconPhoto)
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("DolAgoraApp")  
janela.iconbitmap("C:../Icons/DolAgoraIcon.ico")  #formato ico 

atualizarCotacao() #função que vai manter a cotação atualizada
janela.mainloop()

#JANELA - fim