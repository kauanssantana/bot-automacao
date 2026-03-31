🤖 AutoCadastro RPA

![Capa do Projeto](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

📖 Sobre o Projeto

O AutoCadastro RPA é um robô de automação de processos desenvolvido em Python para otimizar a entrada de dados em sistemas ERP/Web. Em vez de preencher manualmente centenas de produtos, este bot assume o controle do mouse e do teclado, lê uma base de dados externa e realiza todo o trabalho pesado de forma autônoma.

O projeto demonstra conceitos fundamentais de RPA (Robotic Process Automation), como manipulação de interface gráfica (GUI), controle de fluxo por tempo e tratamento de dados estruturados.


✨ Principais Funcionalidades

🔐 Login Automatizado: Acesso inteligente ao sistema com preenchimento automático de credenciais.

📊 Integração com Base de Dados: Leitura e processamento de arquivos .csv utilizando a biblioteca Pandas.

⌨️ Preenchimento de Formulários: Input dinâmico de múltiplos campos (Código, Marca, Tipo, Categoria, Preços e Observações).

🧠 Lógica de Tratamento de Dados: Filtro inteligente que identifica campos vazios (NaN) na planilha e decide se deve ou não realizar a escrita, evitando erros no sistema.

📍 Ferramenta de Calibragem: Script auxiliar incluso para mapear coordenadas de tela (x, y) em qualquer monitor.


💻 Tecnologias Utilizadas
O bot foi construído com foco em simplicidade e eficiência:

Python 3: Linguagem base do projeto.

Pandas: Utilizado para a manipulação e análise da base de dados produtos.csv.

PyAutoGUI: Responsável pela automação da interface gráfica (cliques, escrita e comandos de teclado).

Time: Controle de delays para garantir a sincronia entre o código e o tempo de carregamento do navegador.


🚀 Como Executar o Projeto
Faça o clone deste repositório:

Bash
git clone https://github.com/seu-usuario/autocadastro-rpa.git
Instale as dependências necessárias:

Bash
pip install pyautogui pandas
Calibragem (Obrigatório):
Execute o arquivo auxiliar.py para descobrir as coordenadas de clique do seu monitor e atualize as variáveis no codigo.py.

Rode a automação:

Bash
python codigo.py
