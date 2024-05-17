import math

# Parametry hory
h = 3000  # výška hory v metrech
pata_spicka = 5000  # délka cesty od paty ke špičce v metrech
vzdalenost_mezi_snehulaky = 100  # vzdálenost mezi sněhuláky v metrech
cas_na_stavbu_snehulaka = 30  # čas na stavbu jednoho sněhuláka v minutách
cas_na_pauzu = 60  # čas na pauzu po každé vrstvě v minutách

# Proměnné pro celkový počet sněhuláků a celkový čas
celkovy_pocet_snehulaku = 0
celkovy_cas = 0

# Výpočet vrcholového úhlu
fi = math.acos(h / pata_spicka)

# Iterace přes každou vrstvu
for actual_h in range(0, h, vzdalenost_mezi_snehulaky):
    # Výpočet poloměru na vrstevnici
    r = math.tan(fi) * (h - actual_h)
    # Výpočet obvodu vrstevnice
    obvod = 2 * math.pi * r
    # Výpočet počtu sněhuláků na vrstevnici
    pocet_snehulaku_na_vrstevnici = int(obvod // vzdalenost_mezi_snehulaky)
    # Přičtení počtu sněhuláků k celkovému počtu
    celkovy_pocet_snehulaku += pocet_snehulaku_na_vrstevnici
    # Přičtení času na stavbu sněhuláků a pauzu
    celkovy_cas += pocet_snehulaku_na_vrstevnici * cas_na_stavbu_snehulaka + cas_na_pauzu

# Přidání sněhuláka na vrcholu hory
celkovy_pocet_snehulaku += 1
celkovy_cas += cas_na_stavbu_snehulaka

# Výpočet celkového času ve dnech a hodinách
celkovy_cas_hodiny = celkovy_cas // 60
celkovy_cas_minuty = celkovy_cas % 60
celkovy_cas_dny = celkovy_cas_hodiny // 24
celkovy_cas_hodiny = celkovy_cas_hodiny % 24

# Výpis výsledků
print(f"Celkový počet sněhuláků: {celkovy_pocet_snehulaku}")
print(f"Celkový čas: {celkovy_cas_dny} dnů, {celkovy_cas_hodiny} hodin a {celkovy_cas_minuty} minut")
