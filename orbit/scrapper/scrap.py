import os
import requests
from bs4 import BeautifulSoup

#dir_url = "https://cddis.nasa.gov/archive/gnss/products/2347/"
output_dir = "pobrane_nwmSkad"

################## - tutaj istotne - 2347 do 2399 to cały rok 2025
# start_week = 2347
# end_week = 2399
##################
start_week = 2295
end_week = 2347
os.makedirs(output_dir, exist_ok=True)

print(f"Pobieram listę plików z katalogu...")

for week in range(start_week, end_week + 1):
    dir_url = f'https://cddis.nasa.gov/archive/gnss/products/{week}/'
    print(f'\n--- Scrapuje folder tygodnia: {week} ({dir_url}) ---')

    try:
      # Sesja automatycznie korzysta z pliku _netrc w tle przy przekierowaniach OAuth
      with requests.Session() as session:
        response = session.get(dir_url, timeout=15)
        print(f"Kod statusu strony katalogu: {response.status_code}")

        if response.status_code == 200:
          soup = BeautifulSoup(response.text, "html.parser")
          downloaded_count = 0

          for link in soup.find_all("a"):
            href = link.get("href")
            if href and 'COD0MGXFIN' in href and '_01D_05M_ORB.SP3.gz' in href:
              href = href.strip()
              file_url = f"{dir_url.rstrip('/')}/{href.lstrip('/')}"
              print(
                  f"DEBUG - Sklejony URL: {file_url}"
              )
              file_name = href.split("/")[-1]
              local_filename = os.path.join(output_dir, file_name)

              print(f"Pobieram: {file_name}...")
              file_response = session.get(file_url, stream=True, timeout=30)
              
              if file_response.status_code == 200:
                with open(local_filename, "wb") as f:
                  for chunk in file_response.iter_content(chunk_size=8192):
                    if chunk:
                      f.write(chunk)
                print("-> Zapisano pomyślnie.")
                downloaded_count += 1
              else:
                print(f"-> Błąd pobierania. Status: {file_response.status_code}")

          print(f"\nZakończono! Pobrano łącznie plików: {downloaded_count}")
        else:
          print(f"Błąd dostępu do katalogu. Kod: {response.status_code}")

    except Exception as e:
      print(f"Wystąpił błąd: {e}")