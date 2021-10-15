# Meng-import module tkinter
from tkinter import *


#Entry=Entry(root)

# import xmlrpc bagian client saja
import xmlrpc.client 

# buat stub (proxy) untuk client
proxy = xmlrpc.client.ServerProxy("http://192.168.137.1:8000/RPC2")

# Membuat Object Tkinter
TkObject = Tk()

# Membuat widget label header
Header = Label(TkObject, text="Masukkan Nama Kandidat")

# Memasukan label header kedalam Grid
Header.grid(columnspan=2)

# Membuat widget button
button = Button(TkObject, text="Submit",command=proxy.vote_candidate('Nama'))

# Membuat widget label serta entry untuk nama kandidat
label1 = Label(TkObject, text="Nama")
Entry1 = Entry (TkObject, text="Nama")
#Entry.insert =(1,'Nama')

# Memasukan widget label dan entry dari Nama kandiddat ke dalam grid
label1.grid(row=2, column=0, sticky=E)
Entry1.grid(row=2, column=1)

# Memasukan widget button ke dalam grid
button.grid(row=5, columnspan=2)

# Menjalankan program
#print('Voting berhasil')

# lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
#proxy.querry_result()


