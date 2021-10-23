print("Selamat Datang di Program Konversi Mata Uang Sederhana!")
print("======================================================")
def program_konversi_sederhana():
    print("Berikut Adalah Daftar Menu Mata Uang Yang Dapat Kami Konversi: ")
    daftar_konversi = ["1. IDR-USD   Kurs Jual: 0,000071", "2. IDR-SGD   Kurs Jual: 0,000095", "3. IDR-EUR   Kurs Jual: 0,000061", "4. IDR-JPY   Kurs Jual: 0,0081"]
    for i in daftar_konversi:
        print(i)
    def konversi():
        x = int(input("Silahkan Pilih Menu Nomor Berapa Yang Anda Inginkan: "))
        y = float(input("Silahkan Masukkan Jumlah IDR Yang Ingin Anda Konversi: "))
        print("==================================================================")
        USD = 0.000071 * y
        SGD = 0.000095 * y
        EUR = 0.000061 * y
        JPY = 0.0081 * y
        if x == 1:
            print("Hasil Konversi Adalah: %f" %USD)
        elif x == 2:
            print("Hasil Konversi Adalah: %f" %SGD)
        elif x == 3:
            print("Hasil Konversi Adalah: %f" %EUR)
        elif x == 4:
            print("Hasil Konversi Adalah: %f" %JPY)
        else:
            print("Hasil Tidak Dapat Kami Proses, Silahkan Input Menu Dari Nomor 1-4!")
            konversi()
    konversi()
    print("Apakah Anda Ingin Mengkonversi Lagi? ")
    z = int(input("Ketik '1' Untuk Memulai Program Kembali dan Ketik Angka Lainnya Jika Tidak: "))
    if z == 1:
        program_konversi_sederhana()
    else:
        print("Terimakasih Telah Menggunakan Program Kami!")
program_konversi_sederhana()
