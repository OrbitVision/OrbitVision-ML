from datetime import datetime, timedelta
import os
import re

# Wybierz folder do sprawdzenia ('unpacked_data' lub 'pobrane')
target_dir = 'unpacked_data'

found_dates = set()

if not os.path.exists(target_dir):
  print(f'Folder "{target_dir}" nie istnieje!')
  exit()

print(f'Skanuję pliki w folderze: {target_dir}...')

for file_name in os.listdir(target_dir):
  match = re.search(r'COD0MGXFIN_(\d{4})(\d{3})', file_name)
  if match:
    year = int(match.group(1))
    doy = int(match.group(2))

    # Konwertujemy rok i dzień roku (DOY) na obiekt daty
    try:
      date_obj = datetime.strptime(f'{year} {doy}', '%Y %j').date()
      found_dates.add(date_obj)
    except ValueError:
      print(f'Ostrzeżenie: Nieprawidłowa data w pliku {file_name}')

if not found_dates:
  print('Nie znaleziono żadnych pasujących plików SP3.')
else:
  min_date = min(found_dates)
  max_date = max(found_dates)

  print(f'\n--- ZAKRES ---')
  print(f'Najstarszy plik: {min_date}')
  print(f'Najnowszy plik:  {max_date}')
  print(f'Znaleziono unikalnych dni: {len(found_dates)}')
  print(f'--------------\n')

  print('Sprawdzam brakujące pliki w tym zakresie:')
  current_date = min_date
  missing_count = 0

  while current_date <= max_date:
    if current_date not in found_dates:
      year = current_date.year
      doy = current_date.strftime('%j')
      expected_name = f'COD0MGXFIN_{year}{doy}0000_01D_05M_ORB.SP3'
      print(f'BRAK: {expected_name} (Data: {current_date})')
      missing_count += 1
    current_date += timedelta(days=1)

  print(f'\nPodsumowanie: W wybranym zakresie brakuje {missing_count} plików.')