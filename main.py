import datetime

def ola():
    """
    Retorna uma saudação baseada na hora atual do dia.
    """
    now = datetime.datetime.now()
    hour = now.hour
    if 6 <= hour < 12:
        return "Bom dia"
    elif 12 <= hour < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

# Exemplo de uso (opcional, mas útil para teste)
if __name__ == "__main__":
    print(ola())

