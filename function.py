data = {}

def read():
    if data.items():
        print("╔═══════════════════════════════════════════════════════════════════════════════════════════╗")
        print("╠═══════════════════════════════════════ DAFTAR NILAI ══════════════════════════════════════╣")
        print("╠══════╦══════════════════════╦═══════════════╦══════════╦═════════╦═════════╦══════════════╣")
        print("║  No  ║         NAMA         ║      NIM      ║   TUGAS  ║   UTS   ║   UAS   ║ NILAI AKHIR  ║")
        print("╠══════║══════════════════════║═══════════════║══════════║═════════║═════════║══════════════╣")
        i = 0
        for x in data.items():
            i += 1
            print("║ {6:4} ║ {0:20s} ║ {1:13} ║ {2:8d} ║  {3:6d} ║ {4:7d} ║ {5:12.2f} ║ " 
                    .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("╚══════╩══════════════════════╩═══════════════╩══════════╩═════════╩═════════╩══════════════╝")
    else:
        print("╔═══════════════════════════════════════════════════════════════════════════════════════════╗")
        print("╠═══════════════════════════════════════ DAFTAR NILAI ══════════════════════════════════════╣")
        print("╠══════╦══════════════════════╦═══════════════╦══════════╦═════════╦═════════╦══════════════╣")
        print("║  No  ║         NAMA         ║      NIM      ║   TUGAS  ║   UTS   ║   UAS   ║ NILAI AKHIR  ║")
        print("╠══════╩══════════════════════╩═══════════════╩══════════╩═════════╩═════════╩══════════════╣")
        print("║                                     Tidak Ada Daftar Nilai                                ║")
        print("╚═══════════════════════════════════════════════════════════════════════════════════════════╝")
    pass

def add():
    print("Tambah Data")
    nim = int(input("NIM            : "))
    nama = input("Nama           : ")
    uts = int(input("Nilai UTS      : "))
    uas = int(input("Nilai UAS      : "))
    tugas = int(input("NIlai Tugas    : "))
    nilai_akhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
    data[nama] = nim, tugas, uts, uas, nilai_akhir
    pass

def edit():
    print("Edit Data Nilai Mahasiswa")
    nama = input("Masukan Nama               : ")
    if nama in data.keys():
        nim = input("Masukan nim     : ")
        tugas = int(input("Nilai Tugas Baru  : "))
        uts = int(input("Nilai UTS Baru    : "))
        uas = int(input("Nilai UAS Baru    : "))
        nilai_akhir = ((tugas) * 30 / 100 + (uts) * 35 / 100 + (uas) * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilai_akhir
        read()
    else:
        print("Data nilai {0} tidak ada ".format(nama))
    pass

def delete():
    print("Hapus Data Nilai Mahasiswa")
    nama = input(" Masukan Nama : ")
    if nama in data.keys():
        del data[nama]
        print("Berhasil Hapus Data Nilai Mahasiswa")
        read()
    else:
        print("Data {0} tidak ada".format(nama))
    pass