data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200, 
            'jagung': 880, 
            'kedelai': 500}
    },

    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500, 
            'jagung': 900, 
            'kedelai': 450}
    },

    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100, 
            'jagung': 750, 
            'kedelai': 600}
    },

    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300, 
            'jagung': 850, 
            'kedelai': 550}
    },

    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400, 
            'jagung': 950, 
            'kedelai': 480}
    }
}


# # 1. Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing.
# for lokasi, nama_dan_panen  in data_panen.items():
#     print(f"{lokasi}: {nama_dan_panen}")

# # 2. Tampilkan jumlah hasil panen jagung dari lokasi2.
# print(f"Hasil panen jagung dari lokasi2: {data_panen['lokasi2']['hasil_panen']['jagung']}")

# # 3. Tampilkan nama lokasi dari lokasi3.
# print(f"Nama lokasi3: {data_panen['lokasi3']['nama_lokasi']}")

# # 4 Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda:
# padi_lokasi1 = data_panen['lokasi1']['hasil_panen']['padi']
# kedelai_lokasi1 = data_panen['lokasi1']['hasil_panen']['kedelai']

# padi_lokasi2 = data_panen['lokasi2']['hasil_panen']['padi']
# kedelai_lokasi2 = data_panen['lokasi2']['hasil_panen']['kedelai']

# padi_lokasi3 = data_panen['lokasi3']['hasil_panen']['padi']
# kedelai_lokasi3 = data_panen['lokasi3']['hasil_panen']['kedelai']

# padi_lokasi4 = data_panen['lokasi4']['hasil_panen']['padi']
# kedelai_lokasi4 = data_panen['lokasi4']['hasil_panen']['kedelai']

# padi_lokasi5 = data_panen['lokasi5']['hasil_panen']['padi']
# kedelai_lokasi5 = data_panen['lokasi5']['hasil_panen']['kedelai']

# # 5. Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi.
# hasil_padi = [
#     padi_lokasi1,
#     padi_lokasi2,
#     padi_lokasi3,
#     padi_lokasi4,
#     padi_lokasi5
# ]

# hasil_kedelai = [
#     kedelai_lokasi1,
#     kedelai_lokasi2,
#     kedelai_lokasi3,
#     kedelai_lokasi4,
#     kedelai_lokasi5
# ]

# print("Jumlah padi lokasi 1,2,3,4,5:", hasil_padi)
# print("Jumlah kedelai lokasi 1,2,3,4,5:", hasil_kedelai)


6. Buat Percabangan
Jika jumlah hasil panen padi lebih dari 1300 atau jagung lebih dari 800 di suatu lokasi, maka lokasi tersebut memerlukan perhatian khusus.
Jika tidak, maka lokasi tersebut dalam kondisi baik.

for lokasi, nama_dan_panen in data_panen.items():
    nama = nama_dan_panen['nama_lokasi']
    padi = nama_dan_panen['hasil_panen']['padi']
    jagung = nama_dan_panen['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        status = "memerlukan perhatian khusus."
    else:
        status = "dalam kondisi baik."
    
    print(f"{nama} {status}")