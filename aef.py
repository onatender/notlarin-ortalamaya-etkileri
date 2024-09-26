ders_akts = 1
toplam_akts = 240

dersten_alınabilecek_max_ort_katkısı = 4 * (ders_akts / toplam_akts)

harfler = {
    "CC": 2.0,
    "CB": 2.5,
    "BB": 3.0,
    "BA": 3.5,
    "AA": 4.0
}

for harf, not_degeri in harfler.items():
    print(f"{harf} harfinin ortalamaya pozitif etkisi: {dersten_alınabilecek_max_ort_katkısı * (not_degeri / 4.0):.4f}")



