[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/khaagv3C)
# oslomet_oblig_2

DATA1300 – Obligatorisk oppgave 3  
## Health App
Et lite Python‑program som regner ut BMI og lagrer helsedata.  
Man kan legge til personer, se alle og få litt statistikk.
### Slik kjører du programmet
1. Åpne terminalen i prosjektmappa
   
2. Aktiver miljøet
```bash
source .venv/bin/activate
```
3. Gå til src‑mappa og start
```bash
cd src
python -m health_app.main
```
### Kjøre tester
```bash
pytest -v
```
### Innhold
- `health.py` – regner ut BMI og sånt  
- `data.py` – lagrer og henter fra JSON  
- `main.py` – meny i terminalen  
- `tests/` – testfiler  
### Laget av
Jonas Midthun  
Mai 2026
