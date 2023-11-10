from tkinter import *
import socket

def nslookup():
    domain = domain_entry.get()
    try:
        ip_address = socket.gethostbyname(domain)
        result_label.config(text=f"Nama domain: {domain}\nAlamat IP: {ip_address}")
    except socket.gaierror:
        result_label.config(text=f"Tidak dapat menemukan alamat IP untuk {domain}")

main = Tk()
main.title("NSLookup Alif Fathur")

main.geometry("400x160")

# Label
domain_label = Label(main, text="Masukan domain:")
domain_label.pack(pady=10)
domain_entry = Entry(main)
domain_entry.pack()

look_btn = Button(main, text="NSLookup", command=nslookup)
look_btn.pack(pady=10)

result_label = Label(main, text="", wraplength=300)
result_label.pack()

main.mainloop()
