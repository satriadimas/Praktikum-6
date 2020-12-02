import function

while True:
    print("")
    g = input("L)ihat, T)ambah, U)bah, H)apus, K)eluar: ")
    # Untuk keluar dari program
    if g.lower() == "k":
        print("you exit from program")
        break
    # untuk melihat list
    elif g.lower() == "l":
        function.read()
    # Untuk menambahkan data
    elif g.lower() == "t":
        function.add()
    # Untuk mengubah data
    elif g.lower() == "u":
        function.edit()
    # Untuk menghapus data
    elif g.lower() == "h":
        function.delete()
    else:
        print("Pilih Menu Yang Tersedia")
