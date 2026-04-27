# rmk-internship-2026
metsaraie-toenaosused
# RMK Andmetiimi Praktika 2026: Tõenäosuste Skaala

See repositoorium sisaldab minu lahendust RMK andmetiimi praktikandi proovitööle. Ülesande eesmärgiks oli leida andmeid, arvutada sündmuste tõenäosused ja esitada need intuitiivsel graafilisel skaalal.

## 💡 Idee ja metoodika
Otsustasin analüüsida **Eesti metsanduse andmeid**, kuna see haakub otseselt RMK tegevusvaldkonnaga. Kasutasin Statistikaameti avaandmeid, et leida vastus küsimusele: 
*Kui Eesti metsas tehakse raiet, siis milline on tõenäosus, et tegemist on lageraiega või hooldusraiega?*

Kasutasin tingimusliku tõenäosuse (Bayesi järeldamise) loogikat:
$P(\text{Lageraie} \mid \text{Koguraie}) = \frac{\text{Lageraie pindala}}{\text{Koguraie pindala}}$

Skaalale lisasin võrdlusmomendina ka mündiviske (0.50), et lugejal tekiks parem intuitiivne arusaam tõenäosuste suurusjärkudest. See aitab statistikat paremini tajuda.

## 📊 Andmeallikas
Andmed on pärit Statistikaameti API-st (tabel MM03: "Metsaraie riikliku metsainventeerimise (SMI) hinnangul"). Andmed on programmiliselt päritud aastate 1999–2023 kohta. API kaudu päringu tegemine tagab skripti reprodutseeritavuse.

## 🛠️ Kuidas koodi käivitada
Skript on kirjutatud Pythonis. See tõmbab andmed dünaamiliselt API-st, teeb andmepuhastuse ja arvutused ning joonistab `matplotlib` abil graafiku.

1. Klooni repositoorium:
   `git clone https://github.com/K24101855KristoMihkelson/rmk-internship-2026.git`
2. Installeeri vajalikud teegid:
   `pip install pandas requests matplotlib`
3. Käivita skript:
   `python main.py`

## 📝 Litsents
Selle projekti kood on vaba kasutamiseks ja õppimiseks (MIT litsents).
