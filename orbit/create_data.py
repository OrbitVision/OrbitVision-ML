# mapping = {
#     'PG01': '62339',
#     'PE03': '41860',
#     'PR06': '63130',
#     'PC06': '44204',
#     'PC25': '43603',
#     'PJ02': '42738'
# }

# import pandas as pd
# import glob
# import os

#
# selected_sv = ['PG01', 'PE03', 'PR06', 'PC06', 'PC25', 'PJ02']

# def parse_sp3_file(file_path):
#     data_rows = []
#     with open(file_path, 'r') as f:
#         current_time = None
#         for line in f:
#             # Wyłapujemy linię z czasem (zaczyna się od '*')
#             if line.startswith('*'):
#                 parts = line.split()
#                 # Budujemy datę/czas: 2026 5 29 0 0 0.0 -> 2026-05-29 00:00:00
#                 current_time = f"{parts[1]}-{parts[2].zfill(2)}-{parts[3].zfill(2)} {parts[4].zfill(2)}:{parts[5].zfill(2)}:00"
            
#             
#             elif any(line.startswith(sv) for sv in selected_sv):
#                 parts = line.split()
#                 sv_code = parts[0]
#                 # Pozycje X, Y, Z
#                 x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                
#                 data_rows.append({
#                     'timestamp': current_time,
#                     'sv_code': sv_code,
#                     'x': x, 'y': y, 'z': z
#                 })
#     return pd.DataFrame(data_rows)

# 
# all_files = glob.glob('orbit_raw/raw_sp3_data/*.SP3') # Upewnij się co do ścieżki
# master_sp3 = pd.concat([parse_sp3_file(f) for f in all_files])

# mapping = {
#     'PG01': '62339', 'PE03': '41860', 'PR06': '63130', 
#     'PC06': '44204', 'PC25': '43603', 'PJ02': '42738'
# }
# master_sp3['norad_id'] = master_sp3['sv_code'].map(mapping)

# master_sp3.to_csv('master_sp3_data.csv', index=False)



# import pandas as pd
# import glob
# import json
# import os

# input_folder = 'orbit_raw/raw_sgp4_tle'
# output_file = 'combined_tle.csv'

# all_tle = []

# # Przetwarzanie plików
# print("Wczytywanie plików JSON...")
# for file in glob.glob(os.path.join(input_folder, '*.json')):
#     with open(file, 'r') as f:
#         try:
#             data = json.load(f)
#             # Jeśli dane to lista, dodajemy wszystkie, jeśli słownik - jeden
#             if isinstance(data, list):
#                 all_tle.extend(data)
#             else:
#                 all_tle.append(data)
#         except Exception as e:
#             print(f"Błąd przy czytaniu {file}: {e}")

# # Tworzenie DataFrame
# df_tle = pd.DataFrame(all_tle)

# # Standaryzacja kluczowych kolumn
# if 'NORAD_CAT_ID' in df_tle.columns:
#     df_tle['norad_id'] = df_tle['NORAD_CAT_ID'].astype(str).str.strip()
# if 'EPOCH' in df_tle.columns:
#     df_tle['EPOCH'] = pd.to_datetime(df_tle['EPOCH'], utc=True)


# df_tle = df_tle.drop_duplicates(subset=['norad_id', 'EPOCH'])

# # Zapis do CSV
# df_tle.to_csv(output_file, index=False)


