# Bibliotecas
import pyautogui
import time
import pandas # Movido para o topo!

# Configurações iniciais
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

# Pausa maior para garantir que o site carregue
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=919, y=321) # ATENÇÃO: Pegue a coordenada correta do seu PC
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") 
pyautogui.write("12345678")
pyautogui.press("tab") 
pyautogui.press("enter")

# Pausa maior para o site carregar após o login
time.sleep(3)

# Clique para fechar algum pop-up ou aviso (ajuste as coordenadas)
pyautogui.click(x=1896, y=133)
time.sleep(2)

# Passo 3: Abrir a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4 e 5: Cadastrar os produtos (repetir para cada linha)
for linha in tabela.index: 
    # Clicar no primeiro campo do formulário
    pyautogui.click(x=809, y=235) # ATENÇÃO: Pegue a coordenada correta do seu PC

    # Preencher os campos
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") 
    
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab") 

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab") 

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab") 

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab") 

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab") 

    obs = str(tabela.loc[linha, "obs"])
    # Se observação não for "nan" (vazio), ele escreve
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") 

    # Enviar formulário
    pyautogui.press("enter") 

    # Rolar a página para cima para o próximo cadastro
    pyautogui.scroll(5000)