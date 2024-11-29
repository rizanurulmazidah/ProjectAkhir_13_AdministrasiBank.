akun = {}
admin = {"username": "admin", "password": "admin123"}

def tambah_akun():
    print("\n=== Tambah Akun Baru ===")
    while True:
        nama = input("Masukkan nama nasabah: ")
        if all(char.isalpha() or char.isspace() for char in nama) and nama.strip():
            break
        else:
            print("Nama hanya boleh berisi huruf dan spasi. Silakan coba lagi.")

    while True:
        no_rekening = input("Masukkan nomor rekening: ")
        if no_rekening.isdigit():
            if no_rekening not in akun:
                break
            else:
                print("Nomor rekening sudah terdaftar! Silakan masukkan nomor rekening lain.")
        else:
            print("Nomor rekening hanya boleh berupa angka dan tidak boleh kosong.")

    pin = input("Masukkan PIN (4 digit): ")
    while len(pin) != 4 or not pin.isdigit():
        print("PIN harus terdiri dari 4 digit angka.")
        pin = input("Masukkan PIN (4 digit): ")

    saldo = int(input("Masukkan saldo awal: Rp. "))
    while saldo < 0:
        print("Saldo awal tidak boleh negatif!")
        saldo = int(input("Masukkan saldo awal: Rp. "))

    akun[no_rekening] = {"nama": nama, "pin": pin, "saldo": saldo}
    print(f"\nAkun berhasil ditambahkan untuk {nama} dengan nomor rekening {no_rekening}!\n")

def lihat_semua_akun():
    if not akun:
        print("\nTidak ada akun terdaftar.")
    else:
        print("\n=== Daftar Akun Nasabah ===")
        for no_rekening, data in akun.items():
            print(f"Nomor Rekening: {no_rekening}, PIN: {data['pin']}, Nama: {data['nama']}, Saldo: Rp. {data['saldo']:,}")
    input("\nTekan enter untuk kembali ke menu utama...")

def hapus_akun():
    while True:
        no_rekening = input("Masukkan nomor rekening yang ingin dihapus: ")
        if no_rekening.isdigit():
            break
        else:
            print("Nomor rekening hanya boleh berupa angka dan tidak boleh kosong.")
    
    if no_rekening in akun:
        del akun[no_rekening]
        print(f"Akun dengan nomor rekening {no_rekening} berhasil dihapus.")
    else:
        print("Nomor rekening tidak ditemukan.")
    input("\nTekan enter untuk kembali ke menu utama...")

def ubah_data_akun():
    no_rekening = input("Masukkan nomor rekening yang datanya ingin diubah: ")
    if no_rekening in akun:
        print(f"1. Ubah Nama (saat ini: {akun[no_rekening]['nama']})")
        print(f"2. Ubah PIN (saat ini: {akun[no_rekening]['pin']})")
        print(f"3. Ubah Saldo (saat ini: Rp. {akun[no_rekening]['saldo']:,})")
        pilihan = input("Pilih data yang ingin diubah: ")
        if pilihan == "1":
            akun[no_rekening]["nama"] = input("Masukkan nama baru: ")
            print("Nama berhasil diubah.")
        elif pilihan == "2":
            pin_baru = input("Masukkan PIN baru (4 digit): ")
            while len(pin_baru) != 4 or not pin_baru.isdigit():
                print("PIN harus terdiri dari 4 digit angka.")
                pin_baru = input("Masukkan PIN baru (4 digit): ")
            akun[no_rekening]["pin"] = pin_baru
            print("PIN berhasil diubah.")
        elif pilihan == "3":
            saldo_baru = int(input("Masukkan saldo baru: Rp. "))
            while saldo_baru < 0:
                print("Saldo tidak boleh negatif.")
                saldo_baru = int(input("Masukkan saldo baru: Rp. "))
            akun[no_rekening]["saldo"] = saldo_baru
            print("Saldo berhasil diubah.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Nomor rekening tidak ditemukan.")
    input("\nTekan enter untuk kembali ke menu utama...")

def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Lihat Semua Akun")
        print("2. Tambah Akun Baru")
        print("3. Hapus Akun")
        print("4. Ubah Data Akun")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            lihat_semua_akun()
        elif pilihan == "2":
            tambah_akun()
        elif pilihan == "3":
            hapus_akun()
        elif pilihan == "4":
            ubah_data_akun()
        elif pilihan == "5":
            print("\nKeluar dari menu admin.")
            break
        else:
            print("\nPilihan tidak valid.")

def login_admin():
    print("\n=== Login Admin ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username == admin["username"] and password == admin["password"]:
        print("\nLogin admin berhasil!")
        menu_admin()
    else:
        print("\nUsername atau password salah.")

def login_nasabah():
    print("\n=== Login Nasabah ===")
    pin = input("Masukkan PIN: ")
    for no_rekening, data in akun.items():
        if data["pin"] == pin:
            print("\nLogin berhasil!")
            return no_rekening
    print("PIN tidak ditemukan.")
    return None

def cek_saldo(no_rekening):
    saldo = akun[no_rekening]["saldo"]
    print(f"\n=== Cek saldo ===\nNama: {akun[no_rekening]['nama']}")
    print(f"Saldo anda saat ini: Rp.{saldo:,}")
    input("\nTekan enter untuk kembali ke menu utama...")

def setor_tunai(no_rekening):
    print("\n=== Setor Tunai ===")
    jumlah = int(input("Masukkan jumlah uang yang ingin disetor: Rp. "))
    if jumlah > 0:
        akun[no_rekening]["saldo"] += jumlah
        print(f"\nAnda berhasil menyetor: Rp. {jumlah:,}")
        cek_saldo(no_rekening)
    else:
        print("\nJumlah tidak valid!")

def tarik_tunai(no_rekening):
    print("\n=== Tarik Tunai ===")
    print("1. Rp. 50,000")
    print("2. Rp. 100,000")
    print("3. Rp. 200,000")
    print("4. Rp. 500,000")

    while True:
        pilihan = input("Pilih nominal: ")
        if pilihan.isdigit():
            nominal = {
                "1": 50000,
                "2": 100000,
                "3": 200000,
                "4": 500000
            }.get(pilihan)

            if nominal:
                if nominal <= akun[no_rekening]["saldo"]:
                    akun[no_rekening]["saldo"] -= nominal
                    print(f"\nBerhasil menarik Rp. {nominal:-}")
                    cek_saldo(no_rekening)
                else:
                    print("\nSaldo tidak mencukupi.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1-4.")
        else:
            print("Input harus berupa angka. Silakan coba lagi.")


def transfer_tunai(no_rekening_pengirim):
    print("\n=== Transfer Tunai ===")
    if len(akun) < 2:
        print("Transfer tidak dapat dilakukan karena belum ada akun tujuan lain.")
        input("\nTekan enter untuk kembali ke menu utama...")
        return
    
    while True:
        no_rekening_tujuan = input("Masukkan nomor rekening tujuan: ")
        if no_rekening_tujuan.isdigit():
            break
        else:
            print("Nomor rekening hanya boleh berupa angka dan tidak boleh kosong.")

    if no_rekening_tujuan not in akun:
        print("Nomor rekening tujuan tidak ditemukan.")
        input("\nTekan enter untuk kembali ke menu utama...")
        return
    
    if no_rekening_tujuan == no_rekening_pengirim:
        print("Anda tidak dapat mentransfer ke rekening sendiri.")
        input("\nTekan enter untuk kembali ke menu utama...")
        return

    jumlah = int(input("Masukkan jumlah uang yang ingin ditransfer: Rp. "))
    if jumlah <= 0:
        print("Jumlah transfer tidak valid.")
    elif jumlah > akun[no_rekening_pengirim]["saldo"]:
        print("Saldo tidak mencukupi untuk melakukan transfer.")
    else:
        akun[no_rekening_pengirim]["saldo"] -= jumlah
        akun[no_rekening_tujuan]["saldo"] += jumlah
        print(f"\nBerhasil mentransfer Rp. {jumlah:,} ke rekening {no_rekening_tujuan}.")
        print(f"Sisa saldo Anda: Rp. {akun[no_rekening_pengirim]['saldo']:,}")
    
    input("\nTekan enter untuk kembali ke menu utama...")

def menu_utama(no_rekening):
    while True:
        print("\n=== Menu Utama Nasabah ===")
        print(f"Selamat datang")
        print(f"Nama: {akun[no_rekening]['nama']}, Nomor Rekening: {no_rekening}")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Transfer Tunai")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            cek_saldo(no_rekening)
        elif pilihan == "2":
            setor_tunai(no_rekening)
        elif pilihan == "3":
            tarik_tunai(no_rekening)
        elif pilihan == "4":
            transfer_tunai(no_rekening)
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan layanan kami!")
            break
        else:
            print("\nPilihan tidak valid.")


def main():
    while True:
        print("\n\t=== ATM ===")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Nasabah")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            login_admin()
        elif pilihan == "2":
            no_rekening = login_nasabah()
            if no_rekening:
                menu_utama(no_rekening)
        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan layanan kami!")
            break
        else:
            print("\nPilihan tidak valid.")

main()