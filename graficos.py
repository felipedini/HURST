import matplotlib.pyplot as plt
import MetaTrader5 as mt5
import pandas as pd
from hurst import compute_Hc

# Conecta-se ao MetaTrader 5
if not mt5.initialize():
    print("Falha na inicialização do MetaTrader 5")
    exit(1)


def obter_dados_preco(symbol, timeframe, n_bars):
    try:
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n_bars)
        if rates is None:
            print(f"Não foi possível obter os dados de {symbol}")
            return None
        prices = [rate[4] for rate in rates]  
        return prices
    except Exception as e:
        print(f"Erro ao obter dados de {symbol}: {e}")
        return None

# coloque os Ativos desejados 
assets = ["VALE3", "ITUB4", "PETR4", "PETR3", "BBDC4", "B3SA3", "ELET3", "BBAS3", "ABEV3", "RENT3", "ITSA4", "WEGE3", "BPAC11", "RDOR3", "EQTL3", "RADL3", "SUZB3", "PRIO3", "GGBR4", "RAIL3", "BBDC3", "CSAN3", "BBSE3", "UGPA3", "VBBR3", "JBSS3", "ENEV3", "SBSP3", "LREN3", "HAPV3", "CMIG4", "HYPE3", "VIVT3", "ASAI3", "TOTS3", "KLBN11", "NTCO3", "CCRO3", "EMBR3", "ALSO3", "CPLE6", "ENGI11", "ELET6", "TIMS3", "EGIE3", "SANB11", "MGLU3", "BRFS3", "TAEE11", "GOAU4", "BRKM5", "MULT3", "AZUL4", "CSNA3", "RRRP3", "FLRY3", "CPFE3", "CRFB3", "COGN3", "SOMA3", "YDUQ3", "ENBR3", "BRAP4", "CYRE3", "RAIZ4", "CIEL3", "SMTO3", "IGTI11", "ARZZ3", "CMIN3", "SLCE3", "LWSA3", "USIM5", "IRBR3", "MRVE3", "VIIA3", "PCAR3", "GOLL4", "BEEF3", "DXCO3", "PETZ3", "MRFG3", "ALPA4", "EZTC3", "CVCB3", "CASH3"]


fig, axs = plt.subplots(nrows=5, ncols=5, figsize=(12, 12))


for i, asset in enumerate(assets):
    n_bars = 101  # Defina o número de barras desejado para calcular o expoente de Hurst
    prices = obter_dados_preco(asset, mt5.TIMEFRAME_D1, n_bars)

    if prices is not None:
        try:
            # Calcula o expoente de Hurst dos dados
            H, c, data = compute_Hc(prices)

            
            axs[i // 6, i % 6].plot(range(len(prices)), prices)
            axs[i // 6, i % 6].set_title(f"{asset}\nTimeframe: {mt5.TIMEFRAME_D1}\nHurst: {H:.2f}")

            
            axs[i // 6, i % 6].autoscale(enable=True, axis='both', tight=True)
        except Exception as e:
            print(f"Erro ao calcular expoente de Hurst para {asset}: {e}")


fig.tight_layout()


plt.show()


mt5.shutdown()
