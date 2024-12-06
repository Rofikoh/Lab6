def tambah_data(data_mahasiswa):
  nama = input("Masukkan nama: ")
  nim = input("Masukkan NIM: ")
  uts = int(input("Masukkan nilai UTS: "))
  uas = int(input("Masukkan nilai UAS: "))
  tugas = int(input("Masukkan nilai tugas: "))
  mahasiswa_baru = {'nama': nama, 'nim': nim, 'uts': uts, 'uas': uas, 'tugas': tugas}
  data_mahasiswa.append(mahasiswa_baru)
  print("Data mahasiswa berhasil ditambahkan!")

def tampilkan_data(data_mahasiswa):
  print("\nData Mahasiswa:")
  print("======================================================")
  print("| No | Nama       | NIM   | UTS | UAS | Tugas |")
  print("======================================================")
  no = 1
  for mahasiswa in data_mahasiswa:
    print(f"| {no:2d} | {mahasiswa['nama']:<10} | {mahasiswa['nim']:<8} | {mahasiswa['uts']:3d} | {mahasiswa['uas']:3d} | {mahasiswa['tugas']:4d} |")
    no += 1

def hapus_data(data_mahasiswa):
  nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
  for i in range(len(data_mahasiswa)-1, -1, -1):
    if data_mahasiswa[i]['nama'] == nama:
      del data_mahasiswa[i]
      print("Data mahasiswa berhasil dihapus!")
      return
  print("Data mahasiswa tidak ditemukan!")

def ubah_data(data_mahasiswa):
  nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
  for mahasiswa in data_mahasiswa:
    if mahasiswa['nama'] == nama:
      print("Data mahasiswa saat ini:")
      print(mahasiswa)
      mahasiswa['nim'] = input("Masukkan NIM baru (kosongkan jika tidak ingin mengubah): ") or mahasiswa['nim']
      mahasiswa['uts'] = int(input("Masukkan nilai UTS baru (kosongkan jika tidak ingin mengubah): ")) or mahasiswa['uts']
      mahasiswa['uas'] = int(input("Masukkan nilai UAS baru (kosongkan jika tidak ingin mengubah): ")) or mahasiswa['uas']
      mahasiswa['tugas'] = int(input("Masukkan nilai tugas baru (kosongkan jika tidak ingin mengubah): ")) or mahasiswa['tugas']
      print("Data mahasiswa berhasil diubah!")
      return
  print("Data mahasiswa tidak ditemukan!")

# Inisialisasi data mahasiswa
data_mahasiswa = []

while True:
  print("\nMenu:")
  print("1. Tambah data")
  print("2. Tampilkan data")
  print("3. Hapus data")
  print("4. Ubah data")
  print("5. Keluar")
  pilihan = input("Pilih menu: ")

  if pilihan == '1':
    tambah_data(data_mahasiswa)
  elif pilihan == '2':
    tampilkan_data(data_mahasiswa)
  elif pilihan == '3':
    hapus_data(data_mahasiswa)
  elif pilihan == '4':
    ubah_data(data_mahasiswa)
  elif pilihan == '5':
    break
  else:
    print("Pilihan tidak valid!")
