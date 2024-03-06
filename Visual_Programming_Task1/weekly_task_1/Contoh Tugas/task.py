class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def display_info(self):
        print("=== Informasi Mahasiswa ===")
        print(f"Nama         : {self.nama}")
        print(f"Kelas        : {self.kelas}")
        print(f"Prodi        : {self.prodi}")
        print(f"Fakultas     : {self.fakultas}")
        print(f"Tempat Tinggal: {self.tempat_tinggal}")
        print(f"Asal         : {self.asal}")

# Contoh penggunaan:
if __name__ == "__main__":
    # Membuat objek Mahasiswa
    mahasiswa1 = Mahasiswa("Aditya Nugraha Novianto", "2021 B", "Pendidikan Komputer", "FKIP", "Samarinda", "Kutai Barat")

    # Menampilkan informasi mahasiswa
    mahasiswa1.display_info()
