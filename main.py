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
