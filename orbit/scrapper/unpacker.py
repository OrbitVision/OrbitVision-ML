import gzip
import os

source_dir = 'pobrane'
unpacked_dir = 'unpacked_data'

os.makedirs(unpacked_dir, exist_ok=True)

for file_name in os.listdir(source_dir):
  if file_name.endswith('.SP3.gz'):
    gz_path = os.path.join(source_dir, file_name)
    sp3_file_name = file_name[:-3]
    sp3_path = os.path.join(unpacked_dir, sp3_file_name)

    if not os.path.exists(sp3_path):
      print(f'Rozpakowuję {file_name}...')
      try:
        with gzip.open(gz_path, 'rb') as f_in:
          with open(sp3_path, 'wb') as f_out:
            f_out.write(f_in.read())
        print('-> Rozpakowano pomyślnie!')
      except (EOFError, OSError) as e:
        print(
            f'-> BŁĄD: Plik {file_name} jest uszkodzony lub niepełny! Komunikat:'
            f' {e}'
        )
        print('   (Wskazówka: Usuń ten plik z folderu "pobrane" i pobierz go ponownie)')
        # Jeśli chcesz, możesz odkomentować poniższą linię, żeby automatycznie usuwać uszkodzone archiwum:
        # os.remove(gz_path)
    else:
      print(f'Plik {sp3_file_name} już istnieje w {unpacked_dir}, pomijam.')

print('\nZakończono proces rozpakowywania!')