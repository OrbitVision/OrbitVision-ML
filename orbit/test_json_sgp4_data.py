import json
from datetime import datetime, date, timedelta

nazwa_pliku = "tle_data_to_verify.json"

with open(nazwa_pliku, "r", encoding="utf-8") as f:
  data = json.load(f)

znalezione_daty = set()
for item in data:
    epoch_str = item.get("EPOCH")
    if epoch_str:
        d = datetime.fromisoformat(epoch_str).date()
        znalezione_daty.add(d)

start_date = date(2025, 1, 1)
end_date = date(2025, 12, 31)

wszystkie_dni_2025 = set()
current = start_date
while current <= end_date:
    wszystkie_dni_2025.add(current)
    current += timedelta(days=1)

brakujace_dni = sorted(list(wszystkie_dni_2025 - znalezione_daty))

if not brakujace_dni:
    print("Sukces! Masz dane dla każdego dnia 2025 roku.")
else:
    print(f"Brakuje dni ({len(brakujace_dni)}):")
    for dzien in brakujace_dni:
        print(dzien)