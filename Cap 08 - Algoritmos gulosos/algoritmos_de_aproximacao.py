# Usamos set para termos valores únicos dentro do array

estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # Estados que desejamos ter cobertura

estacoes = {} 
estacoes["kone"] = set(["id", "nv", "ut"])
estacoes["ktwo"] = set(["wa", "id", "mt"])
estacoes["kthree"] = set(["or", "nv", "ca"])
estacoes["kfour"] = set(["nv", "ut"])
estacoes["kfive"] = set(["ca", "az"])

final_estacoes = set() # Onde vamos armazenar o conjunto final de estações

def conjunto_cobertura(estados_abranger, estacoes):
    final_estacoes = set()
    while estados_abranger:
        melhor_estacao = None
        estados_cobertos = set()
        for estacao, estados_por_estacao in estacoes.items():
            cobertos = estados_abranger & estados_por_estacao # intersecção 
            if len(cobertos) > len(estados_cobertos) and estacao not in final_estacoes:
                melhor_estacao = estacao
                estados_cobertos = cobertos
        if melhor_estacao is not None:
            estados_abranger -= estados_cobertos
            final_estacoes.add(melhor_estacao)
            estacoes.pop(melhor_estacao)
        else:
            return None
    return final_estacoes

print(conjunto_cobertura(estados_abranger, estacoes))