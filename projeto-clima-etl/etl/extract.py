import os
import json
import requests  # Solicita os dados a API
from datetime import datetime
from dotenv import load_dotenv  # Segurança para carregar senhas

# Carrega as variáveis que estão no arquivo .env para a memória do script
load_dotenv()

def extrair_dados_clima():
    """
    Função responsável por conectar na API, baixar os dados e salvar no disco.
    Retorna: O dicionário de dados se sucesso, ou None se falha.
    """
    
    # 1. Configuração (Pega as credenciais do "Cofre")
    api_key = os.getenv("TOMORROW_API_KEY")
    location = os.getenv("LOCATION")
    
    if not api_key or not location:
        print("ERRO: Variáveis de ambiente (API KEY ou LOCATION) não encontradas no .env")
        return None

    # 2. Solicita os dados em Realtime
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={api_key}"
    headers = {"accept": "application/json"}

    try:
        print(f"🔄 Conectando a API Tomorrow.io para a localização: {location}...")
        
        # 3. Requisição
        response = requests.get(url, headers=headers)

        # 4. Validação (O HTTP 200 é sucesso. 401 é senha errada. 429 é limite estourado)
        response.raise_for_status() 

        # 5. Parsing (Transforma o texto que veio da internet em Dicionário Python)
        dados = response.json()

        # 6. Persistência na Raw (Salvando o "Snapshot" do momento)
        # Cria um nome de arquivo único baseado no horário atual: ex: clima_20231027_153000.json
        timestamp_atual = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho_arquivo = f"data/raw/clima_{timestamp_atual}.json"

        # Abre o arquivo em modo de escrita ('w') e salva o JSON
        with open(caminho_arquivo, 'w') as f:
            json.dump(dados, f, indent=4)

        print(f"✅ Sucesso! Dados brutos salvos em: {caminho_arquivo}")
        return dados

    except requests.exceptions.HTTPError as err:
        print(f"❌ Erro de HTTP (A API recusou): {err}")
    except Exception as e:
        print(f"❌ Erro Genérico: {e}")
    
    return None
"""
# Este bloco 'if' permite testar este arquivo isoladamente
if __name__ == "__main__":
    extrair_dados_clima()
"""    