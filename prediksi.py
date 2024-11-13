import tkinter as tk #Import: tkinter dan messagebox digunakan untuk membuat antarmuka GUI dan menampilkan pesan.
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try: 
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")
#Fungsi hasil_prediksi: Memvalidasi input pengguna dan menampilkan hasil prediksi:
#Perulangan for: Mengecek semua nilai yang diambil dari entries (masing-masing entry berisi nilai mata pelajaran).
#Konversi ke int: Mencoba mengubah nilai input menjadi integer.
#Validasi Nilai: Memastikan nilai berada di antara 0 dan 100. Jika tidak, fungsi akan mengeluarkan ValueError.
#Hasil Prediksi: Jika semua input valid, label hasil_label akan diperbarui dengan teks "Prediksi Prodi: Teknologi Informasi".
#Pesan Kesalahan: Jika terjadi kesalahan, messagebox akan menampilkan pesan bahwa input harus berupa angka antara 0 dan 100.

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#f0f0f0")
#Inisialisasi root: Menciptakan jendela utama aplikasi.
#Pengaturan Jendela: Menambahkan judul, ukuran (500x600 piksel), dan latar belakang dengan warna abu-abu terang (#f0f0f0).

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#FFADAD")
judul_label.pack(pady=20)
#Membuat label judul di bagian atas dengan teks "Aplikasi Prediksi Prodi Pilihan", menggunakan font Arial ukuran 18 yang tebal, dan latar belakang merah muda (#FFADAD).
#pack(pady=20) memberikan jarak vertikal sebesar 20 piksel di sekitar label.

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#FFADAD")
frame_input.pack(pady=10)


entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#FFADAD")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)
#Looping untuk Input: Membuat 10 label dan entry untuk nilai mata pelajaran.
#Setiap label menunjukkan "Nilai Mata Pelajaran X" (X dari 1 hingga 10).
#Masing-masing entri diberi lebar 10 dan font Arial ukuran 12.
#Setiap entry ditambahkan ke list entries untuk memudahkan akses dalam fungsi hasil_prediksi.


prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="orange")
prediksi_button.pack(pady=30)
#Tombol Prediksi: Membuat tombol dengan teks "Hasil Prediksi".
#Tombol ini memanggil fungsi hasil_prediksi saat ditekan.
#Font Arial ukuran 12 yang tebal, dengan latar hijau (#4CAF50) dan teks berwarna oranye

hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="red", bg="#FFADAD")
hasil_label.pack(pady=20)

root.mainloop()