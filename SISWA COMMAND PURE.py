import json
import os
from datetime import datetime

json_file = "keluhan.json"


# ===========================
#  LOAD & SAVE JSON
# ===========================
def load_json():
    if not os.path.exists(json_file):
        return []

    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except:
        return []


def save_json(data):
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)


# ===========================
#  MENU SISWA (INPUT LAPORAN)
# ===========================
def menu_siswa():
    print("\n    \033[34m === LAPOR KETUA!! ===\033[0m"
          "\n\033[34m=== Laporkan masalahmu disini ===\033[0m")
    fasilitas = input("Masukkan Fasilitas: ")
    tempat = input("Masukkan Tempat: ")
    keterangan = input("Masukkan Keterangan: ")
    tanggal = datetime.now().strftime("%d-%m-%Y")

    record = {
        "Fasilitas": fasilitas,
        "Tempat": tempat,
        "Keterangan": keterangan,
        "Tanggal": tanggal,
        "Laporan": "Belum"
    }

    data = load_json()
    data.append(record)
    save_json(data)

    print("\n✔ Terimakasih telah melaporkan!\n")

    input("Tekan Enter untuk kembali ke menu...")


# ===========================
#  MENU ADMIN
# ===========================
def tampilkan_data():
    data = load_json()

    if not data:
        print("\n( Kosong )\n")
        return

    print("\n=== DATA LAPORAN ===")

    for i, item in enumerate(data, start=1):
        print(f"\n[{i}]")
        print(f"Fasilitas   : {item['Fasilitas']}")
        print(f"Tempat      : {item['Tempat']}")
        print(f"Keterangan  : {item['Keterangan']}")
        print(f"Tanggal     : {item['Tanggal']}")
        print(f"Laporan     : {item['Laporan']}")
    print()


def ubah_status():
    data = load_json()

    if not data:
        print("\nTidak ada laporan untuk diubah!\n")
        return

    tampilkan_data()

    try:
        index = int(input("Pilih nomor laporan yang ingin diubah: ")) - 1
        if index < 0 or index >= len(data):
            print("Nomor tidak valid!")
            return
    except:
        print("Input harus angka!")
        return

    print("""
=== Pilih Status Baru ===
1. Pending
2. Diproses
3. Selesai
""")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        data[index]["Laporan"] = "Pending"
    elif pilihan == "2":
        data[index]["Laporan"] = "Diproses"
    elif pilihan == "3":
        data[index]["Laporan"] = "Selesai"
    else:
        print("Pilihan tidak valid!")
        return

    save_json(data)
    print("\n✔ Status laporan berhasil diperbarui!\n")

def hapus_laporan():
    data = load_json()
    tampilkan_data()

    try:
        idx = int(input("Pilih nomor laporan yang ingin dihapus: ")) - 1
        if idx < 0 or idx >= len(data):
            print("Nomor tidak valid!")
            return
    except:
        print("Input harus angka!")
        return

    del data[idx]
    save_json(data)

    print("\n✔ Laporan telah dihapus!\n")


def hapus_semua():
    confirm = input("Yakin hapus semua data? (y/n): ")
    if confirm.lower() == "y":
        save_json([])
        print("\n✔ Semua laporan dihapus!\n")

#MENU ADMIN
def menu_admin():
    while True:
        def box(text, color="\033[34m"):  # default ungu
            reset = "\033[0m"
            length = len(text) + 4
            print(color + "+" + "-" * length + "+" + reset)
            print(color + "|  " + text + "  |" + reset)
            print(color + "+" + "-" * length + "+" + reset)

        box("MENU ADMIN", "\033[34m")



        print("1. Lihat Semua Laporan")
        print("2. Ubah Status Laporan")
        print("3. Hapus Laporan")
        print("4. Hapus Semua Laporan")
        print("5. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampilkan_data()
        elif pilih == "2":
            ubah_status()
        elif pilih == "3":
            hapus_laporan()
        elif pilih == "4":
            hapus_semua()
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid!")


# ===========================
#  MENU UTAMA
# ===========================
def main_menu():


    while True:
        print("\033[34m"+"================================================================================================")
        ascii_banner = """
        ██╗      █████╗ ██████╗  ██████╗ ██████╗      ██╗  ██╗███████╗████████╗██╗   ██╗ █████╗ 
        ██║     ██╔══██╗██╔══██╗██╔═══██ ██╔══██╗     ██║ ██╔╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
        ██║     ███████║██████╔╝██║   ██ ██████╔╝     █████╔╝ █████╗     ██║   ██║   ██║███████║
        ██║     ██╔══██║██╔══   ██║   ██ ██╔══██╗     ██╔═██╗ ██╔══╝     ██║   ██║   ██║██╔══██║
        ███████╗██║  ██║██║     ██████╝  ██║  ██║     ██║  ██╗███████╗   ██║   ╚██████╔╝██║  ██║
        ╚══════╝╚═╝  ╚═╝╚═╝      ╚═══╝   ╚═╝  ╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
        """
        print("\033[34m" + ascii_banner + "\033[0m")
        print("\033[34m" + "================================================================================================ " + "\033[0m")
        print("1. Siswa - Laporkan Masalah")
        print("2. Admin - Lapor Ketua")
        print("3. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            menu_siswa()
        elif pilih == "2":
            menu_admin()
        elif pilih == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

    input("\nTekan Enter untuk keluar...")


# Jalankan program
main_menu()
