import tkinter as tk

# Fungsi untuk menghasilkan prediksi
def hasil_prediksi():
    hasil_label.config(text="Hasil Prediksi: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x600")
root.resizable(False, False)

# Frame utama untuk meletakkan semua widget
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()

# Membuat judul aplikasi
judul_label = tk.Label(main_frame, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
judul_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Membuat input untuk nilai mata pelajaran
entries = []
for i in range(10):
    label = tk.Label(main_frame, text=f"Nilai Mata Pelajaran {i+1}:")
    label.grid(row=i+1, column=0, sticky="e", padx=5, pady=5)
    
    entry = tk.Entry(main_frame, width=10)
    entry.grid(row=i+1, column=1, pady=5)
    entries.append(entry)

# Tombol untuk memprediksi prodi
prediksi_button = tk.Button(main_frame, text="Hasil Prediksi", command=hasil_prediksi, bg="lightblue", font=("Arial", 10, "bold"))
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(main_frame, text="Hasil Prediksi: ", font=("Arial", 12, "italic"))
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()
