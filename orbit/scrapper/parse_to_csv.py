import os
import glob
import pandas as pd

def parse_sp3_file(filepath):
    records = []
    current_epoch = None
    
    with open(filepath, 'r') as f:
        for line in f:
            # Wychwytujemy nagłówek epoki zaczynający się od '*'
            if line.startswith('*'):
                parts = line.split()
                if len(parts) >= 6:
                    current_epoch = f"{parts[1]}-{parts[2].zfill(2)}-{parts[3].zfill(2)} {parts[4].zfill(2)}:{parts[5].zfill(2)}:{parts[6].zfill(2)}"
            
            # Wychwytujemy linie pozycji (zaczynają się od 'P' lub 'PG', 'PR', itp.)
            elif line.startswith('P') and current_epoch:
                parts = line.split()
                if len(parts) >= 4:
                    sat_id = parts[0][1:]  # Wycina literę systemu, np. 'G01' z 'PG01' lub zostawia sam identyfikator
                    try:
                    # X, Y, Z to zazwyczaj kolejne elementy po nazwie satelity
                        x = float(parts[1])
                        y = float(parts[2])
                        z = float(parts[3])
                        
                        # Opcjonalnie czwarty element to zegar (clock), jeśli chcesz go zachować
                        c = float(parts[4]) if len(parts) > 4 else 0.0
                        
                        records.append({
                            'epoch': current_epoch,
                            'sat_id': sat_id,
                            'x': x,
                            'y': y,
                            'z': z,
                            'clock': c
                        })
                    except ValueError:
                        continue
                        
    return records

def main():
    # Szuka plików w podfolderze unpacked_data, będąc w folderze scrapper
    search_path = 'unpacked_data/*.SP3'
    sp3_files = glob.glob(search_path)
    
    print(f"Znaleziono {len(sp3_files)} plików SP3 w ścieżce: {search_path}")
    
    if len(sp3_files) == 0:
        print("Brak plików! Upewnij się, że folder unpacked_data znajduje się w tym samym miejscu, z którego uruchamiasz skrypt.")
        return

    all_data = []
    for filepath in sp3_files:
        print(f"Przetwarzam: {os.path.basename(filepath)}")
        records = parse_sp3_file(filepath)
        all_data.extend(records)
        
    df = pd.DataFrame(all_data)
    
    # Zapis do CSV w bieżącym folderze scrapper
    output_path = 'orbits_2025_processed.csv'
    df.to_csv(output_path, index=False)
    print(f"Sukces! Zapisano wszystkie dane do {output_path} (łącznie wierszy: {len(df)})")

if __name__ == '__main__':
    main()