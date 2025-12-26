import json

# Definição dos Gatilhos (Thresholds)
LIMITE_TEMPERATURA_ALTA = 30.0 
LIMITE_TEMPERATURA_BAIXA = 10.0 
LIMITE_CHUVA = 70.0 

def verificar_alerta(dados_json):
    """
    Analisa os dados brutos e decide se emite um alerta.
    Input: JSON bruto da API (igual ao extract.py)
    """
    try:
        # Selecionando os dados que quero:
        valores = dados_json['data']['values']
        
        temp_atual = valores.get('temperature')
        chuva_prob = valores.get('precipitationProbability')
        
        # Lista para acumular mensagens de alerta
        alertas = []

        # Regra 1: Calor Extremo
        if temp_atual and temp_atual >= LIMITE_TEMPERATURA_ALTA:
            msg = f"🔥 ALERTA DE CALOR: Temperatura atual de {temp_atual}°C atingiu o limite de {LIMITE_TEMPERATURA_ALTA}°C."
            alertas.append(msg)

        # Regra 2: Frio Extremo
        if temp_atual and temp_atual <= LIMITE_TEMPERATURA_BAIXA:
            msg = f"❄️ ALERTA DE FRIO: Temperatura atual de {temp_atual}°C está abaixo de {LIMITE_TEMPERATURA_BAIXA}°C."
            alertas.append(msg)

        # Regra 3: Chuva Iminente
        if chuva_prob and chuva_prob >= LIMITE_CHUVA:
            msg = f"☔ ALERTA DE CHUVA: Probabilidade de chuva é de {chuva_prob}%."
            alertas.append(msg)

        # Disparador (A saída)
        if alertas:
            print("\n" + "="*40)
            print("🚨 ATENÇÃO: SISTEMA DE EMERGÊNCIA CLIMÁTICA 🚨")
            print("="*40)
            for alerta in alertas:
                print(f" -> {alerta}")
            print("="*40 + "\n")
            
            # Aqui no futuro entraria: enviar_email(alertas) ou enviar_sms(alertas)
            return True
        else:
            print(f"✅ Condições Normais: {temp_atual}°C e {chuva_prob}% de chance de chuva.")
            return False

    except Exception as e:
        print(f"❌ Erro ao processar alertas: {e}")
        return False
"""
# Bloco de Teste Simulado
if __name__ == "__main__":
    # Vamos criar um dado FAKE para testar se o alerta dispara
    # Isso é um "Unit Test" manual
    dado_fake_perigoso = {
        "data": {
            "values": {
                "temperature": 38.5,            # Vai disparar calor
                "precipitationProbability": 80, # Vai disparar chuva
                "humidity": 40
            }
        }
    }
    
    print("🧪 Testando com dados simulados de EMERGÊNCIA:")
    verificar_alerta(dado_fake_perigoso)
    
    print("\n🧪 Testando com dados simulados NORMAIS:")
    dado_fake_normal = {"data": {"values": {"temperature": 22, "precipitationProbability": 0}}}
    verificar_alerta(dado_fake_normal)
    """