import requests

# test scrappera
url = "https://cddis.nasa.gov/archive/gnss/products/2419/COD0MGXFIN_20261370000_01D_01D_OSB.BIA.gz"
local_filename = url.split("/")[-1]
print("Testowanie połączenia z NASA CDDIS...")

try:
    with requests.Session() as session:
        response = session.head(url, timeout=10)
        
        print(f"Kod statusu HTTP: {response.status_code}")
        
        if response.status_code == 200:
            print("Sukces! Połączenie działa, plik jest dostępny.")
            with open(local_filename, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print("Chyba zapisane :>")
        elif response.status_code == 401:
            print("Błąd 401")
        elif response.status_code == 404:
            print("Błąd 404")
        else:
            print(f"Cos wybuchło fest: {response.status_code}")

except Exception as e:
    print(f"Błąd sieci: {e}")