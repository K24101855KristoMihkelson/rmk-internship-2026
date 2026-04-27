import requests
import pandas as pd
import io

def fetch_stat_api_data():
    """Pärib Statistikaametist metsaraiete andmed."""
    url = "https://andmed.stat.ee/api/v1/et/stat/MM03"
    
    payload = {
      "query": [
        {
          "code": "Aasta",
          "selection": {
            "filter": "item",
            "values": [str(aasta) for aasta in range(1999, 2024)]
          }
        },
        {
          "code": "Raie liik",
          "selection": {
            "filter": "item",
            "values": ["1", "2", "3", "4"]
          }
        },
        {
          "code": "Näitaja",
          "selection": {
            "filter": "item",
            "values": ["1"]
          }
        }
      ],
      "response": {
        "format": "csv"
      }
    }

    print("Saadan päringu Statistikaameti API-sse...")
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Andmed edukalt käes!")
        df = pd.read_csv(io.StringIO(response.text), encoding='utf-8-sig')
        return df
    else:
        print(f"Viga API päringul! Veakood: {response.status_code}")
        return None

if __name__ == "__main__":
    metsa_df = fetch_stat_api_data()
    if metsa_df is not None:
        import matplotlib.pyplot as plt

        # 1. ANDMETE PUHASTAMINE
        print("Puhastan andmed...")
        metsa_df.columns = ['Aasta', 'Raieliik', 'Pindala_tuhat_ha']
        metsa_df['Raieliik'] = metsa_df['Raieliik'].str.replace('..', '', regex=False).str.strip().str.capitalize()

        # 2. TÕENÄOSUSTE ARVUTAMINE
        print("Arvutan tõenäosusi...")
        summad = metsa_df.groupby('Raieliik')['Pindala_tuhat_ha'].sum()
        koguraie_summa = summad['Koguraie']
        lageraie_summa = summad['Lageraie']
        hooldusraie_summa = summad['Hooldusraie']

        p_lageraie = lageraie_summa / koguraie_summa
        p_hooldusraie = hooldusraie_summa / koguraie_summa

        # 3. GRAAFIKU JOONISTAMINE
        print("Joonistan tõenäosuste skaalat...")
        sundmused = ['Lageraie\n(kui toimub raie)', 'Mündivise\n(kull/kiri)', 'Hooldusraie\n(kui toimub raie)']
        toenaosused = [p_lageraie, 0.5, p_hooldusraie]
        varvid = ['#e63946', '#457b9d', '#2a9d8f'] 

        fig, ax = plt.subplots(figsize=(12, 4))
        ax.hlines(y=0, xmin=0, xmax=1, color='gray', alpha=0.5, linewidth=2, zorder=1)
        ax.scatter(toenaosused, [0, 0, 0], color=varvid, s=200, zorder=2, edgecolors='black')

        y_korgused = [0.05, -0.05, 0.05]
        joondused = ['bottom', 'top', 'bottom']

        for i, (txt, p) in enumerate(zip(sundmused, toenaosused)):
            ax.annotate(f"{txt}\n{p:.2f}", 
                        (p, y_korgused[i]), 
                        ha='center', 
                        va=joondused[i],    
                        fontsize=11, 
                        fontweight='bold',
                        color=varvid[i])

        ax.scatter([0, 1], [0, 0], color='black', s=50, zorder=2)
        ax.text(0, -0.15, "0.0\n(Võimatu)", ha='center', va='top', fontsize=10, color='gray')
        ax.text(1, -0.15, "1.0\n(Kindel)", ha='center', va='top', fontsize=10, color='gray')

        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(-0.3, 0.3) 
        ax.axis('off') 
        ax.set_title("Tõenäosuste skaala: Millist raiet tehakse Eesti metsas?", 
                     fontsize=16, 
                     fontweight='bold', 
                     pad=20)

        plt.show() 
