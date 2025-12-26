import pandas as pd # A ferramenta padrão da indústria para dados
import os
import json
import glob # Biblioteca para encontrar arquivos em pastas

def transformar_dados(dados_json):
    """
    Recebe o dicionário JSON (da memória), extrai as métricas importantes,
    transforma em tabela e salva na camada Gold (CSV).
    """
    try:
        # 1. Navegação (Drill-down)
        # O JSON da Tomorrow.io geralmente tem a estrutura: data -> values
        # Se der erro aqui, é porque a estrutura do JSON mudou ou é diferente
        valores = dados_json['data']['values']
        momento = dados_json['data']['time']
        
        # 2. Achatamento (Flattening)
        # Escolhemos a dedo o que queremos monitorar. O resto é lixo.
        dados_tratados = {
            'data_hora_coleta': momento,
            'temperatura': valores.get('temperature'),
            'sensacao_termica': valores.get('temperatureApparent'),
            'umidade': valores.get('humidity'),
            'velocidade_vento': valores.get('windSpeed'),
            'probabilidade_chuva': valores.get('precipitationProbability'),
            'codigo_clima': valores.get('weatherCode')
        }

        # 3. Criação do DataFrame (A Tabela de 1 linha)
        df_novo = pd.DataFrame([dados_tratados])

        # 4. Salvamento Incremental (Append)
        arquivo_saida = "data/gold/historico_clima.csv"
        
        # Verificamos se o arquivo já existe para saber se precisamos escrever o cabeçalho
        existe_arquivo = os.path.isfile(arquivo_saida)
        
        # mode='a' significa APPEND (adicionar ao final), não sobrescrever
        # header=not existe_arquivo significa: só escreva o nome das colunas se o arquivo for novo
        df_novo.to_csv(arquivo_saida, mode='a', index=False, header=not existe_arquivo)
        
        print(f"✅ Sucesso! Dados transformados e adicionados em: {arquivo_saida}")
        return True

    except KeyError as e:
        print(f"❌ Erro de Schema: Não encontrei a chave {e} no JSON. Verifique a estrutura.")
        return False
    except Exception as e:
        print(f"❌ Erro na Transformação: {e}")
        return False

# Bloco de teste local
if __name__ == "__main__":
    # Truque para testar: Pega o arquivo mais recente da pasta Raw
    lista_arquivos = glob.glob('data/raw/*.json')
    if lista_arquivos:
        ultimo_arquivo = max(lista_arquivos, key=os.path.getctime)
        print(f"🧪 Testando transformação com o arquivo: {ultimo_arquivo}")
        
        with open(ultimo_arquivo, 'r') as f:
            dados_teste = json.load(f)
            transformar_dados(dados_teste)
    else:
        print("⚠️ Nenhum arquivo encontrado em data/raw/ para testar.")