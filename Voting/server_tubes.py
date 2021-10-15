# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler

import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2')

# Buat server
with SimpleXMLRPCServer(('192.168.137.1', 8000)) as server:
	server.register_introspection_functions()

    # buat data struktur dictionary untuk menampung nama_kandidat dan hasil voting
	nama_kandidat = {'nama':["Buala","Christian","Basado","Furqon"], 'vote':[0,0,0,0]}

    # kode setelah ini adalah critical section, menambahkan vote tidak boeh terjadi race condition
    # siapkan lock
	lock = threading.Lock()
    

    #  buat fungsi bernama vote_candidate()
	def vote_candidate(x):
        # critical section dimulai harus dilock
		lock.acquire()
        # jika nama_kandidat ada dalam dictionary maka tambahkan  nilai votenya
		if x in nama_kandidat['nama']:
			idx = nama_kandidat['nama'].index(x)
			nama_kandidat['vote'][idx]+=1
		print(nama_kandidat['vote'])
		
        # critical section berakhir, harus diunlock
		lock.release()
		return 'AHSYIAAAP'
	
    # register fungsi vote_candidate() sebagai vote
	server.register_function(vote_candidate)
	
    # buat fungsi bernama querry_result
	def querry_result():

        # critical section dimulai
		lock.acquire()

        # hitung total vote yang ada
		total_vote = sum(nama_kandidat['vote'])

        # hitung hasil persentase masing-masing nama_kandidat
		for i in range(len(nama_kandidat['nama'])):
			persentase = (nama_kandidat['vote'][i]/total_vote)*100
			print("Nama : ", nama_kandidat['nama'][i])
			print("Persentase : ", persentase, "%")
				
		# critical section berakhir
		lock.release()
		return 'AHSYIAAAP'
		
	# register querry_result sebagai querry
	server.register_function(querry_result, 'querry_result')
	
	print ('Server voting berjalan...')
    # Jalankan server
	server.serve_forever()
