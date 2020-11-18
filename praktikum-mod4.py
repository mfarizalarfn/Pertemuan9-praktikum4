print("===================================================================")
print("Nama : Mohamad Farizal Arifin")
print("NIM : 312010231")
print("Kelas : TI.20.B1")
print("Mata Kuliah : Bahasa Pemrograman")
print("===================================================================")
print("Tugas Praktikum module 4")

# Buat program sederhana untuk menambahkan data kedalam sebuah list dengan rincian sebagai berikut:
# • Progam meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
# • Tampilkan pertanyaan untuk menambah data (y/t?), apabila jawaban t (Tidak), maka program akan menampilkan daftar datanya.
# • Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)
# • Buat flowchart dan penjelasan programnya pada README.md.
# • Commit dan push repository ke github.

baris = []
stop = False

# masukan nilai
while (not stop):
    nama = input("Masukan Nama : ")
    nim = input("Masukan NIM : ")
    tugas = input("Masukan Nilai Tugas : ")
    uts = input("Masukan Nilai UTS : ")
    uas = input("Masukan Nilai UAS : ")
    nilai_akhir = 0.3 * float(tugas) + 0.35 * float(uts) + 0.35 * float(uas)
    baris.extend([nama, nim, tugas, uts, uas, nilai_akhir])

    tanya = input("Tambah data? (y/n) : ")
    if(tanya == "n"):
        stop = True

# cetak nilai
print("===================================================================")

from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["N0","Nama","Nim","Tugas","UTS","UAS","Nilai Akhir"]
x.add_row(["no",baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]])
print(x)