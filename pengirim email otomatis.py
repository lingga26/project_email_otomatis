import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.message import EmailMessage

def kirim_email():
    # Membuat objek EmailMessage
    msg = EmailMessage()

    # Mengambil nilai dari input pengguna
    pengirim = pengirim_entry.get()
    penerima = penerima_entry.get()
    subjek = subjek_entry.get()
    isi_email = isi_email_text.get("1.0", tk.END)

    # Memeriksa apakah semua input telah diisi
    if not pengirim or not penerima or not subjek or not isi_email:
        messagebox.showerror("Error", "Mohon lengkapi semua kolom.")
        return

    # Menentukan subjek email
    msg['Subject'] = subjek

    # Menentukan pengirim email
    msg['From'] = pengirim

    # Menentukan penerima email
    msg['To'] = penerima

    # Menentukan isi email
    msg.set_content(isi_email)

    try:
        # Membuat objek SMTP dengan server Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # Mengaktifkan mode Transport Layer Security (TLS)
        server.starttls()

        # Login ke akun Gmail dengan email dan password
        server.login('lingganugraha26@gmail.com', 'apak vdnh vhsi ycya')

        # Mengirim email dengan objek EmailMessage
        server.send_message(msg)

        # Menutup koneksi dengan server
        server.quit()

        # Menampilkan pesan bahwa email telah terkirim
        messagebox.showinfo("Info", "Email telah terkirim")
    except Exception as e:
        # Menampilkan pesan error jika terjadi kesalahan
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Pengiriman Email")

# Membuat label dan entry untuk pengirim
label_pengirim = ttk.Label(root, text="Pengirim:")
label_pengirim.grid(row=0, column=0, padx=10, pady=5)
pengirim_entry = ttk.Entry(root)
pengirim_entry.grid(row=0, column=1, padx=10, pady=5)

# Membuat label dan entry untuk penerima
label_penerima = ttk.Label(root, text="Penerima:")
label_penerima.grid(row=1, column=0, padx=10, pady=5)
penerima_entry = ttk.Entry(root)
penerima_entry.grid(row=1, column=1, padx=10, pady=5)

# Membuat label dan entry untuk subjek
label_subjek = ttk.Label(root, text="Subjek:")
label_subjek.grid(row=2, column=0, padx=10, pady=5)
subjek_entry = ttk.Entry(root)
subjek_entry.grid(row=2, column=1, padx=10, pady=5)

# Membuat label dan teks area untuk isi email
label_isi_email = ttk.Label(root, text="Isi Email:")
label_isi_email.grid(row=3, column=0, padx=10, pady=5)
isi_email_text = tk.Text(root, height=5, width=40)
isi_email_text.grid(row=3, column=1, padx=10, pady=5)

# Membuat tombol untuk mengirim email
tombol_kirim = ttk.Button(root, text="Kirim Email", command=kirim_email)
tombol_kirim.grid(row=4, column=0, columnspan=2, pady=10)

# Menjalankan loop utama aplikasi
root.mainloop()
