## Python Behave Playwright
Este projeto implementa uma suíte de testes automatizados utilizando a abordagem BDD (Behavior Driven Development) com Python e Behave, com foco em garantir a qualidade de APIs, interfaces de usuário (UI) e integração com a base de dados.

O objetivo principal é fornecer uma framework estruturada e escalável para validar funcionalidades críticas de aplicações, promovendo testes claros, legíveis e de fácil manutenção. A suíte combina:

Testes de API utilizando Playwright permitindo simular requisições, validar respostas e garantir a consistência das integrações.

Testes de UI para validar fluxos da aplicação do ponto de vista do usuário final.

Validações de base de dados para assegurar que operações críticas persistam os dados corretamente e atendam às regras de negócio.

BDD com Behave, fornecendo uma camada de documentação viva onde cenários de teste são escritos em linguagem natural (Gherkin), facilitando o entendimento entre equipes de QA, desenvolvimento e stakeholders.


## Instalação e Pré-requisitos

Python 3.12.0 (https://www.python.org/downloads/)
Verifique a instalação com:
python --version

Node.js v20.17.0 (https://nodejs.org/pt/blog/release/v20.17.0)
Necessário para executar testes de API e UI com Playwright.
Verifique a versão instalada:
node --version


## Estrutura do Projeto

O projeto segue a estrutura padrão BDD com Python e Behave, organizada para suportar testes de API, UI e validações de base de dados, de forma modular e escalável.

```
project-root
│
├── src/
│   ├── features/                  # Contém os arquivos .feature do Behave
│   │   ├── steps/                 # Contém os step definitions correspondentes às features
│   │   └── *.feature              # Arquivos de cenários escritos em Gherkin
│   │
│   ├── pages/                     # Implementação dos métodos das páginas / funcionalidades
│   │   └── *.py
│   │
│   ├── elementpages/              # Variáveis e elementos reutilizáveis das páginas
│   │   └── *.py
│   │
│   └── files/                     # Arquivos auxiliares como imagens, Excel, dados de teste, etc.
│       └── *
│
├── behave.ini                     # Configuração do Behave
├── requirements.txt               # Lista de dependências do Python

```

Configuração do behave.ini

O Behave precisa conhecer a estrutura do projeto para localizar corretamente os arquivos de teste e steps. O arquivo behave.ini contém a seguinte configuração:
```
[behave]
paths = src/features
steps_dir = src/features/steps
logging_level = INFO
show_skipped = false
show_timings = true
```

Dependências do Projeto

O arquivo requirements.txt contém todas as bibliotecas necessárias para executar a suíte:

```
behave
playwright
allure-behave 
behave-html-formatter
allure-python-commons
openpyxl 
mysql-connector-python
browser-use 
```
pip install -r requirements.txt

A seguir executar o comando faz o download dos browsers necessários para os testes.

playwright install


## Extensões VS Code Recomendadas(plugins)

Para melhorar a produtividade e facilitar o desenvolvimento e execução dos testes, recomenda-se instalar as seguintes extensões no Visual Studio Code.

Como instalar
Abrir o VS Code
No menu lateral esquerdo, clicar em Extensions (Ctrl + Shift + X)
Pesquisar pelo ID da extensão ou pelo nome.
Clicar em Install
```
Lista de extensões
BDD / Cucumber / Behave
alexkrechik.cucumberautocomplete
Autocomplete, snippets e suporte para arquivos .feature. (escolher em settings do plugin pre-release)

Playwright
ms-playwright.playwright
Integração oficial do Playwright com VS Code.

sakamoto66.vscode-playwright-test-runner
Permite executar testes Playwright diretamente no editor.

Python
ms-python.python
Suporte completo para desenvolvimento em Python.

ms-python.debugpy
Ferramenta de debugging para Python no VS Code.

Relatórios de Teste
qameta.allure-vscode
Visualização de relatórios Allure diretamente no VS Code.

Produtividade
github.copilot-chat
Assistente de IA para ajudar na escrita de código e testes.

esbenp.prettier-vscode
Formatação automática de código.

Interface
dracula-theme.theme-dracula
Tema visual Dracula para o editor.

Utilidades
sleistner.vscode-fileutils
Facilita criação e manipulação de arquivos no projeto.
```

## Executar Testes (sem relatório Allure)
Para executar todos os testes a partir da suite de testes localizada na pasta src, utilize o comando:

behave --no-capture --no-skipped --color --format pretty

Explicação das opções

--no-capture → mostra os logs diretamente no terminal

--no-skipped → oculta cenários ignorados

--color → ativa cores no output do terminal

--format pretty → output formatado para melhor leitura

## Executar Testes com Relatório Allure
Para executar uma feature específica e gerar os resultados do Allure, utilize:

behave --no-capture features/nome_da_feature.feature -f allure_behave.formatter:AllureFormatter -o allure-results

Após executar os testes e gerar os resultados, crie o relatório com:

allure generate allure-results -o allure-report --clean
```
allure-results → contém os resultados dos testes

allure-report → pasta onde o relatório HTML será gerado

--clean → remove relatórios antigos antes de gerar o novo
```
Para abrir o relatório no navegador:
Navegue até à pasta onde o relatório foi gerado
Execute o comando:

Allure open .

ou gera e abre o relatório automaticamente, sem precisar executar generate e open separadamente.

allure serve allure-results