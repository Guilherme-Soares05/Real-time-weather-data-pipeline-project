# ⛈️ Pipeline de Engenharia de Dados: Monitoramento Climático Regional

> **Projeto inspirado no curso da Udemy: Projeto Real de Engenharia de Dados: Real Time Analytics**
---

## 📖 Sobre o Projeto

Este repositório documenta a implementação de um pipeline **ETL (Extract, Transform, Load)** completo para monitoramento de condições meteorológicas críticas em tempo real.

O objetivo central foi replicar a lógica de negócios de uma arquitetura corporativa de Big Data, porém adaptando-a para um cenário de **custo zero** e infraestrutura efêmera, demonstrando capacidade de abstração e engenharia de software.

Veja como ficou o resultado final: https://lookerstudio.google.com/reporting/5ee24cf9-af6c-4350-a7c9-bab3ef5927ed

---

## 🏗️ Arquitetura: Da Nuvem Enterprise para a Solução "Smart"

A base teórica deste projeto vem de uma arquitetura clássica de Streaming na AWS. O desafio foi substituir componentes pagos por soluções eficientes em código Python.

### 1. O Modelo Original (AWS Enterprise)
Baseado na arquitetura de referência corporativa, o fluxo original utilizava recursos com cobrança por hora/disponibilidade:
* **Ingestão:** `API Gateway` + `Lambda Producer`
* **Broker de Mensagens:** `Amazon Kinesis Data Streams` (Custo fixo alto por shard)
* **Processamento:** `Lambda Consumer` + `Glue Jobs` (Cobrança por DPU)
* **Catálogo:** `AWS Glue Data Catalog`
* **Orquestração:** `CloudWatch Events`

### 2. A Solução Implementada (Serverless)
Refatorei a arquitetura mantendo os princípios de Engenharia de Dados (Desacoplamento, Resiliência e Idempotência), mas alterando a tecnologia para custo zero:

| Função | Componente AWS (Original) | Solução "Github Codespace e Google Looker" (Atual) |
| :--- | :--- | :--- |
| **Gatilho** | CloudWatch Events | Execução Manual / Cron no Container |
| **Extração** | Lambda Producer | Script Python (`requests`) |
| **Broker** | Kinesis Data Streams | Variáveis em Memória (Python Lists) |
| **Transformação**| Glue / Lambda Consumer | Biblioteca `pandas` (Dataframes) |
| **Storage** | Amazon S3 | **Git** (Versionamento de CSV) |
| **Analytics** | Amazon Athena / QuickSight | **Google Sheets** + **Looker Studio** |

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12
* **Bibliotecas:** `pandas`, `requests`, `python-dotenv`
* **Fonte de Dados:** Tomorrow.io API
* **Orquestração:** Script Python Modular (`main.py`)
* **Visualização:** Google Sheets e Google Looker Studio

## Como Executar

### Pré-requisitos
* Conta no GitHub (Gratuita)
* API Key da Tomorrow.io (Gratuita)
* Planilha no Google Sheets (Gratuita)
* Criar relatório no Googler Looker Studio (Gratuito)


### Passo a Passo
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/](https://github.com/)[SEU_USUARIO]/[NOME_DO_REPO].git
    cd [NOME_DO_REPO]
    ```

2.  **Configure o Ambiente Virtual:**
    ```bash
    touch .env #Cria o arquivo .env na raiz do projeto
    python -m venv venv
    source venv/bin/activate #Ativa o ambiente virtual
    ```

3.  **Baixe os requirements:**
    ```bash
    cd ./projeto-clima-etl/
    pip install -r requirements.txt
    ```

4.  **Configurando API e Localização:**
    ```text
    TOMORROW_API_KEY= Gerar a api no Tomorrow https://app.tomorrow.io/home
    LOCATION=-23.5505, -46.6333 (Meu exemplo)
    ```

5. **Executando o pipeline:**
    ```bash
        python main.py
    ```

6. **Suba o CSV gerado para o Github:**
    ```bash
        git add .
        git commit -m "Sua mensagem de commit"
        git push
    ```

## 📈 Configuração do Sheets

1. **No Sheets crie uma planilha vazia (em branco)**
* **Obs: Você precisará que o .csv esteja na pasta gold do repositório do Github**
2. **Navegue até a pasta onde está o .csv e clique nele apenas para visualização**
3. **Será exibido o .csv porém no canto direito superior haverá uma opção chamada "raw" clique nela e copie o link com final csv**
4. **Na célula A1 clique duas vezes e adicione =IMPORTDATA("Colar o link do CSV")**
5. **Mude para Estados Unidos**
* **Por que? O Python gera números com ponto (25.5). O Sheets Brasil espera vírgula. Mudar para EUA corrige a leitura dos dados.**
7. **Acesse o Google Looker Studio.** <br>

## 📊 Configuração do Looker

8. **Crie um relatório vazio.**
9. **Selecione a fonte de dados Planilhas Google.**
10. **Escolha a planilha que você criou.**
11. **Pronto! Seus gráficos serão atualizados sempre que você rodar o script Python e atualizar a planilha.**

---
*Desenvolvido por: @Guilherme-Soares05 como projeto de Portfólio de Engenharia de Dados.*