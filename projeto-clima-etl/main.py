import os
import time
from etl import extract, transform, alert

def executar_pipeline():
    print("🚀 Iniciando Pipeline de Engenharia de Dados (Clima)...")
    
    # PASSO 1: EXTRAÇÃO (Extract)
    # Vai na API e traz o JSON para a pasta data/raw
    dados_brutos = extract.extrair_dados_clima()
    
    if not dados_brutos:
        print("⛔ Pipeline abortado por falha na extração.")
        return

    # PASSO 2: ALERTA (Monitoramento)
    # Verifica se precisa gritar "Fogo!" (ou "Gelo!")
    alert.verificar_alerta(dados_brutos)

    # PASSO 3: TRANSFORMAÇÃO (Transform & Load)
    # Transforma o JSON em uma linha de CSV e anexa no histórico
    sucesso_transformacao = transform.transformar_dados(dados_brutos)

    # PASSO 4: PERSISTÊNCIA (Git Automation)
    # Se tudo deu certo, salva o CSV no GitHub para não perder quando o Codespace fechar
    if sucesso_transformacao:
        sincronizar_git()
    
    print("🏁 Pipeline finalizado com sucesso.")

def sincronizar_git():
    """
    Função que age como um robô operando o terminal git.
    Ela adiciona o arquivo CSV modificado e envia para a nuvem.
    """
    print("☁️ Iniciando sincronização com o GitHub...")
    
    try:
        # Configurações básicas (caso o codespace tenha esquecido quem é você)
        # Substitua pelo seu e-mail se quiser, ou deixe genérico
        os.system('git config --global user.email "Informar o e-mail"')
        os.system('git config --global user.name "Bot Clima Codespace"')

        # Adiciona apenas o arquivo de histórico (a pasta raw ignoramos pois é pesada/suja)
        os.system('git add data/gold/historico_clima.csv')
        
        # Faz o commit com data e hora automática
        mensagem = f"Update: Dados climaticos {time.strftime('%Y-%m-%d %H:%M')}"
        os.system(f'git commit -m "{mensagem}"')
        
        # Envia para o repositório remoto
        resultado = os.system('git push')
        
        if resultado == 0:
            print("✅ Git Push realizado! Seus dados estão salvos no repositório.")
        else:
            print("⚠️ Aviso: O Git Push falhou (talvez não haja mudanças novas ou erro de permissão).")
            
    except Exception as e:
        print(f"❌ Erro no Git Sync: {e}")

if __name__ == "__main__":
    executar_pipeline()