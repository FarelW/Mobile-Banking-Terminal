import os
import json
from user import *
import time
from waktu import *
# import phonenumbers as pn
# from phonenumbers import carrier


# Program
# with open("database.json", "r") as f:
#     data = json.load(f)
#     user = data["user1"]

# Function untuk Pendaftaran 
def daftar():
    print('SILAHKAN DAFTAR')
    print(60*'_')
    users['Nama Anda'] = str(input('Masukkan Nama Lengkap Anda          \t: '))
    users['No. Rek'] = str(input('Masukkan Nomor Rekening Anda     \t: '))
    users['Password'] = str(input('Buat Password (HANYA ANGKA)     \t: '))
    name = users['Nama Anda']
    no_rek = users['No. Rek']
    passw = users['Password']
    if len(name) == 3:
        users['Username'] = name + no_rek[-1] + passw[-1]
    else:
        users['Username'] = name[0:4] + no_rek[-1] + passw[-1]
    os.system('cls')
    print(60*'_')
    print('|', 'PENDAFTARAN BERHASIL'.center(56), '|'.rjust(-10))
    print(60*'=')
    print('Data Diri Anda')
    count = 0
    for i in users:
        if count < 4:
            print(f'{i}                 \t: {users[i]}')
            count += 1
    print(60*'-')
    ganti_username = str(input('Ingin mengganti username?(Y/N) : '))
    if ganti_username.lower() == 'y':
        new_username = str(input('Masukkan username baru: '))
        users['Username'] = new_username
        print('Username BERHASIL DIPERBARUI')
    else:
        print(60*'-')
    print(''' 
        ''')
    with open("database.json", "r") as f:
        data = json.load(f)
        user = data["user1"]
        user.append(users)
    with open("database.json", "w") as file:
        json.dump(data, file, indent=4)
    os.system('cls')

# Function untuk login
def login():
    global indexUser
    print(60*'=')
    print('SILAHKAN LOGIN')
    print(60*'-')
    with open("database.json", "r") as f:
        data = json.load(f)
        user = data["user1"]
    username = str(input('Masukkan username: '))
    password = str(input('Masukkan Password: '))
    ulangi = False
    for i in range(len(user)):
        if password == user[i]["Password"] and username == user[i]["Username"]:
            print('BERHASIL LOGIN')
            indexUser = i
            ulangi = False
            time.sleep(1)
            os.system('cls')
            return indexUser
        else:
            ulangi = True

    if ulangi == True:
        print('Password atau Username anda SALAH, silahkan ulangi!')
        print(60*'-')
        time.sleep(3)
        os.system('cls')
        login()
    print('''
        
        
        ''')

# Function untuk tampilan awal
def depan():
    os.system('cls')
    print(60*'=')
    print('||', 'NINE MOBILE BANKING'.center(54), '||'.rjust(-10))
    print(60*'=')
    print('HALO, SELAMAT DATANG'.center(60))
    print(60*'-')
    print('''     
        oooo   oooo ooooo oooo     oooo  ooooooo   
         8888o  88   888   8888o   888 o888   888o 
         88 888o88   888   88 888o8 88 888     888 
         88   8888   888   88  888  88 888o   o888 
        o88o    88  o888o o88o  8  o88o  88ooo88   
                                           
        ''')
    print(60*'-')
    pilih = input('Apakah anda sudah memiliki akun?(Ya/No): ')
    print(60*'-')
    os.system('cls')
    if pilih.lower() == 'no':
        daftar()
        login()
    else:
        login()

# Function untuk tampilan menu
def menu():
    os.system('cls')
    with open("database.json", "r") as f:
        data = json.load(f)
        user = data["user1"]
    print(60*'=')
    print('||', 'NIMO BANKING'.center(54), '||'.rjust(-10))
    print(60*'=')
    print(f'HALO, Selamat {waktu} {user[indexUser]["Nama Anda"]}'.center(60))
    print(60*'_')
    print('Saldo Rekening Utama'.center(55))
    print(f'Rp {user[indexUser]["Saldo"]}'.center(55))
    print(60*'-')
    print('| (1) Home            (2) Aktivitas               (3) Akun |')
    print(60*'-')
    print('Catatan Keuangan')
    print(45*'-')
    print(f'| Pemasukan       | Pengeluaran             ')
    print(45*'-')
    print(
        f'| Rp {user[indexUser]["Pemasukkan"]}   | Rp {user[indexUser]["Pengeluaran"]}     ')
    print(45*'-')
    print(f'Selisih Rp {user[indexUser]["Selisih"]}'.center(25))
print(60*'_')

# Function untuk menampilkan menu Home
def menu_home():
    global choice
    os.system('cls')
    print('Menu Home')
    print(60*'-')
    print('| (1) Tarik Tunai    (2) Transfer     (3) Dompet Digital |')
    print('|           (4) Pulsa Data     (5) Listrik               |')
    print(60*'-')
    choice = int(input('Pilih menu : '))
    if choice == 1:
        # TARIK TUNAI
        global penarikan
        with open("database.json", "r") as f:
            data = json.load(f)
            user = data["user1"]
        with open("database.json", "w") as file:
            json.dump(data, file, indent=4)
        os.system('cls')
        nominal = [100_000, 200_000, 300_000, 400_000, 500_000,
                   600_000, 700_000, 800_000, 900_000, 1_000_000]
        print(' ')
        print('Sumber Dana')
        print(15*"-")
        print(user[indexUser]["No. Rek"])
        print(f'Rp {user[indexUser]["Saldo"]}')
        print(15*"-")
        print('Nominal')
        x = 0
        for i in range(0, 5):
            print(41*"-")
            print(
                f'| Rp {nominal[x]} ({x+1})  | | Rp {nominal[x+1]} ({x+2})\t|')
            x += 2
        print(41*"-")
        print('')
        choice_nominal = int(input('Pilih : '))
        penarikan = nominal[choice_nominal-1]
        aktivitas_recorder(choice)
        print(41*"_")
        print('Detail')
        print(f'Nominal Penarikan     \t Rp {nominal[choice_nominal-1]} ')
        print(f'Biaya Admin           \t Rp 0 ')
        print(41*'_')
        print(f'Total                 \t Rp {nominal[choice_nominal-1]} ')
        print('Konfirmasi')
        t = True
        while t:
            konfirmasi = str(input('Masukkan PIN: '))
            if konfirmasi == user[indexUser]["Password"]:
                import random
                with open("database.json", "r") as f:
                    data = json.load(f)
                    user = data["user1"]
                    user[indexUser]["Saldo"] -= nominal[choice_nominal-1]
                    user[indexUser]["Pengeluaran"] += nominal[choice_nominal-1]
                    user[indexUser]["Selisih"] = user[indexUser]["Pemasukkan"] - \
                        user[indexUser]["Pengeluaran"]
                with open("database.json", "w") as file:
                    json.dump(data, file, indent=4)
                print('PIN TARIK TUNAI')
                for i in range(6):
                    print(random.randint(0, 9), end='')
                t = False
            else:
                print('PIN ANDA SALAH')
        print(30*'_', )
        pilih = str(input('Lanjut ke menu utama?(Y/N): '))
        print(' ')
        if pilih.lower() == 'y':
            menu()
            menu_choice()
        else:
            print('Terima Kasih, telah menggunakan aplikasi Nine Banking')
    elif choice == 2:
        # TRANSFER
        global tf, penerima, rekening, n_bank
        with open("database.json", "r") as f:
            data = json.load(f)
            user = data["user1"]
        os.system('cls')
        print(' ')
        print('Transfer')
        print(15*"_")
        print('Bank Tujuan')
        bank = ['BANK BRI    ', 'MANDIRI     ', 'BANK BNI    ', 'BANK BTN    ', 'BANK BCA    ',
                'CIMB NIAGA  ',  'BANK PERMATA', 'MAYBANK     ', 'BANK DANAMON', 'BANK CAPITAL']
        x = 0
        for i in range(0, 5):
            print(49*"-")
            print(
                f'| {bank[x]} ({x+1})      | | {bank[x+1]} ({x+2})\t|')
            x += 2
        print(49*"-")
        print('')
        choice_nominal = int(input('Pilih Bank: '))
        n_bank = bank[choice_nominal-1]
        penerima = str(input('Nama Penerima: '))
        rekening = str(input(f'Nomor Rekening {bank[choice_nominal-1]}: '))
        print(49*'_')
        print('Nominal Transfer')
        tf = int(input('Rp '))
        aktivitas_recorder(choice)
        print(49*'_')
        print('''
                  ''')
        os.system('cls')
        print('Konfirmasi')
        print(49*'_')
        print('Sumber dana')
        print(user[indexUser]['Nama Anda'])
        print('NINE BANK -', user[indexUser]['No. Rek'])
        print(30*'-')
        print('Nomor Tujuan')
        print(penerima)
        print(f'{bank[choice_nominal-1]}')
        print(f'{rekening}')
        print(49*'_')
        print('Detail')
        print(f'Nominal                  Rp {tf}')
        print(f'Biaya Admin              Rp 6.500')
        print(49*'-')
        print(f'Total                    Rp {tf + 6500}')
        with open("database.json", "r") as f:
            data = json.load(f)
            user = data["user1"]
            user[indexUser]["Saldo"] -= tf + 6500
            user[indexUser]["Pengeluaran"] += tf + 6500
            user[indexUser]["Selisih"] = user[indexUser]["Pemasukkan"] - \
                user[indexUser]["Pengeluaran"]
        with open("database.json", "w") as file:
            json.dump(data, file, indent=4)
        t = True
        while t:
            konfirmasi = (input('Masukkan PIN: '))
            if konfirmasi == user[indexUser]['Password']:
                print('Transfer BERHASIL')
                t = False
            else:
                print('PIN ANDA SALAH')
        print(30*'_', )
        pilih = str(input('Lanjut ke menu utama?(Y/N): '))
        print(' ')
        if pilih.lower() == 'y':
            menu()
            menu_choice()
        else:
            print('Terima Kasih, telah menggunakan aplikasi Nine Banking')
            utama = False
    elif choice == 3:
        # Dompet Digital
        global dg, choice1, tf1, nomor_hp
        with open("database.json", "r") as f:
            data = json.load(f)
            user = data["user1"]
        os.system('cls')
        print(' ')
        print('Dompet Digital')
        print(15*"_")
        dg = ['GoPay ', 'LinkAja  ', 'OVO   ',
              'ShopeePay', 'DANA  ',  'i.saku  ']
        x = 0
        for i in range(0, 3):
            print(41*"-")
            print(f'| {dg[x]} ({x+1})      | | {dg[x+1]} ({x+2})\t|')
            x += 2
        print(41*"-")
        print('')
        choice1 = int(input('Pilih Dompet Digital: '))
        # NOMOR HP
        nomor = True
        while nomor:
            nomor_hp = str(input(f'Nomor Handphone:  '))
            if 9 < len(nomor_hp) < 13:
                nomor = False
            else:
                print('Nomor tidak ditemukan!')
        print('''
                  ''')
        print(49*'_')
        print('Konfirmasi')
        print(49*'_')
        print('Nomor Tujuan')
        print(f'{dg[choice1 - 1]} - {nomor_hp}')
        print(30*'-')
        print('Nominal Transfer')
        tf1 = int(input('Rp '))
        aktivitas_recorder(choice)
        print(49*'_')
        with open("database.json", "r") as f:
            data = json.load(f)
            user = data["user1"]
            user[indexUser]["Saldo"] -= tf1
            user[indexUser]["Pengeluaran"] += tf1
            user[indexUser]["Selisih"] = user[indexUser]["Pemasukkan"] - \
                user[indexUser]["Pengeluaran"]
        with open("database.json", "w") as file:
            json.dump(data, file, indent=4)
        t = True
        while t:
            konfirmasi = (input('Masukkan PIN: '))
            if konfirmasi == user[indexUser]['Password']:
                print('Top Up BERHASIL')
                t = False
            else:
                print('PIN ANDA SALAH')
        print(30*'_', )
        pilih = str(input('Lanjut ke menu utama?(Y/N): '))
        print(' ')
        if pilih.lower() == 'y':
            menu()
            menu_choice()
        else:
            print('Terima Kasih, telah menggunakan aplikasi Nine Banking')

    elif choice == 4:
        # PULSA/DATA
        global pilih1, kode, nohp, cn, angka, data1
        with open("database.json", "r") as f:
            data = json.load(f)
            user = data["user1"]
        os.system('cls')
        print(' ')
        print('Beli Pulsa/Data')
        print(15*"_")
        #  DATA DAM PULSA
        data1 = {
            'hari': [['500 MB', 3000], ['1 GB', 5000], ['5 GB', 20000], ['10GB', 30000], ['30GB', 50000]],
            'minggu': [['1.5 GB', 20000], ['4.5 GB', 35000], ['10 GB', 60000], ['18GB', 85000], ['30GB', 105000]],
            'bulan': [['3.5 GB', 28000], ['7.5 GB', 50000], ['15 GB', 75000], ['30GB', 120000], ['50GB', 145000]]
        }
        pulsa = [10_000, 15_000, 20_000, 25_000, 30_000,
                 40_000, 50_000, 75_000, 100_000, 150_000, 200_000, 300_000, 500_000, 1_000_000]
        print(49*'_')
        # Nomor Hp
        nomor = True
        nohp = '+62'
        while nomor:
            nomor_hp = str(input(f'Nomor Handphone:  '))
            nohp += nomor_hp.replace(nomor_hp[0], '')
            no = pn.parse(nohp)
            valid = pn.is_valid_number(no)
            if valid == True:
                nomor = False
            else:
                print('Nomor tidak ditemukan!')
        print('')
        # Melacak Provider
        provider_no = pn.parse(nohp, 'RO')
        print(carrier.name_for_number(provider_no, 'en'), '-', nomor_hp)
        p = True

        while p:
            pilih1 = str(input('Pulsa(P) / Data(D)? P/D: '))
            if pilih1 == 'P':
                os.system('cls')
                x = 0
                for i in range(0, int(len(pulsa)/2)):
                    print(41*"-")
                    print(
                        f'| Rp {pulsa[x]} ({x+1})      | | {pulsa[x+1]} ({x+2})\t|')
                    x += 2
                print(41*"-")
                print('')
                choice_nominal = int(input('Pilih : '))
                cn = pulsa[choice_nominal-1]
                aktivitas_recorder(choice)
                print(41*"_")
                print('Detail')
                print(
                    f'Nominal               \t Rp {pulsa[choice_nominal-1]} ')
                print(f'Biaya Admin           \t Rp 1.500 ')
                print(41*'_')
                print(
                    f'Total                 \t Rp {pulsa[choice_nominal-1] + 1500} ')
                print('Konfirmasi')
                t = True
                while t:
                    konfirmasi = (input('Masukkan PIN: '))
                    if konfirmasi == user[indexUser]['Password']:
                        with open("database.json", "r") as f:
                            data = json.load(f)
                            user = data["user1"]
                            user[indexUser]["Saldo"] -= (
                                pulsa[choice_nominal-1] + 1500)
                            user[indexUser]["Pengeluaran"] += (
                                pulsa[choice_nominal-1] + 1500)
                            user[indexUser]["Selisih"] = user[indexUser]["Pemasukkan"] - \
                                user[indexUser]["Pengeluaran"]
                        with open("database.json", "w") as file:
                            json.dump(data, file, indent=4)
                        print('Transaksi BERHASIL')
                        t = False
                    else:
                        print('PIN ANDA SALAH')
                print(30*'_', )
                pilih = str(input('Lanjut ke menu utama?(Y/N): '))
                print(' ')
                if pilih.lower() == 'y':
                    menu()
                    menu_choice()
                else:
                    print('Terima Kasih, telah menggunakan aplikasi Nine Banking')
                p = False
            elif pilih1 == 'D':
                os.system('cls')
                print('Paket Harian')
                x = 0
                for i in range(0, 5):
                    print(33*"-")
                    print(
                        f"| {data1['hari'][i][0]}      Rp {data1['hari'][i][1]}  (H{x+1})\t|")
                    x += 1
                print('')
                print('Paket Mingguan')
                y = 0
                for i in range(0, 5):
                    print(33*"-")
                    print(
                        f"| {data1['minggu'][i][0]}       Rp {data1['minggu'][i][1]}  (M{y+1})\t|")
                    y += 1
                print('')
                print('Paket Bulanan')
                z = 0
                for i in range(0, 5):
                    print(33*"-")
                    print(
                        f"| {data1['bulan'][i][0]}       Rp {data1['bulan'][i][1]}  (B{z+1})\t|")
                    z += 1
                # Pilih Paket
                paket = str(input('Pilih Paket (CONTOH: H5) : '))
                kode = paket.replace(paket[1], '')
                angka = int(paket.replace(paket[0], ''))

                # PAKET HARIAN
                if kode == 'H':
                    aktivitas_recorder(choice)
                    os.system('cls')
                    print(
                        f"Paket yang anda pilih: {data['hari'][angka-1][0]} 1 Hari")
                    print('Detail')
                    print(
                        f"Nominal               \t Rp {data1['hari'][angka-1][1]} ")
                    print(f'Biaya Admin           \t Rp 0 ')
                    print(41*'_')
                    print(
                        f'Total                 \t Rp {data1["hari"][angka-1][1]} ')
                    print('Konfirmasi')
                    p = False
                    t = True
                    while t:
                        konfirmasi = (input('Masukkan PIN: '))
                        if konfirmasi == user[indexUser]['Password']:
                            with open("database.json", "r") as f:
                                data = json.load(f)
                                user = data["user1"]
                                user[indexUser]["Saldo"] -= (
                                    data1['hari'][angka-1][1])
                                user[indexUser]["Pengeluaran"] += (
                                    data1['hari'][angka-1][1])
                                user[indexUser]["Selisih"] = user[indexUser]["Pemasukkan"] - \
                                    user[indexUser]["Pengeluaran"]
                            with open("database.json", "w") as file:
                                json.dump(data, file, indent=4)
                            print('Transaksi BERHASIL')
                            t = False
                        else:
                            print('PIN ANDA SALAH')

                # PAKET MINGGUAN
                elif kode == 'M':
                    aktivitas_recorder(choice)
                    os.system('cls')
                    print(
                        f"Paket yang anda pilih: {data1['minggu'][angka-1][0]} 7 Hari")
                    print('Detail')
                    print(
                        f"Nominal               \t Rp {data1['minggu'][angka-1][1]} ")
                    print(f'Biaya Admin           \t Rp 0 ')
                    print(41*'_')
                    print(
                        f'Total                 \t Rp {data1["minggu"][angka-1][1]} ')
                    print('Konfirmasi')
                    p = False
                    t = True
                    while t:
                        konfirmasi = (input('Masukkan PIN: '))
                        if konfirmasi == user[indexUser]['Password']:
                            with open("database.json", "r") as f:
                                data = json.load(f)
                                user = data["user1"]
                                user[indexUser]["Saldo"] -= data1['minggu'][angka-1][1]
                                user[indexUser]["Pengeluaran"] += data1['minggu'][angka-1][1]
                                user[indexUser]["Selisih"] = user[indexUser]["Pemasukkan"] - \
                                    user[indexUser]["Pengeluaran"]
                            with open("database.json", "w") as file:
                                json.dump(data, file, indent=4)
                            print('Transaksi BERHASIL')
                            t = False
                        else:
                            print('PIN ANDA SALAH')

                # PAKET BULANAN
                elif kode == 'B':
                    aktivitas_recorder(choice)
                    os.system('cls')
                    print(
                        f"Paket yang anda pilih: {data1['bulan'][angka-1][0]} 30 Hari ")
                    print('Detail')
                    print(
                        f"Nominal               \t Rp {data1['bulan'][angka-1][1]} ")
                    print(f'Biaya Admin           \t Rp 0 ')
                    print(41*'_')
                    print(
                        f'Total                 \t Rp {data1["bulan"][angka-1][1]} ')
                    print('Konfirmasi')
                    p = False
                    t = True
                    while t:
                        konfirmasi = (input('Masukkan PIN: '))
                        if konfirmasi == user[indexUser]['Password']:
                            os.system('cls')
                            with open("database.json", "r") as f:
                                data = json.load(f)
                                user = data["user1"]
                                user[indexUser]["Saldo"] -= data1["bulan"][angka-1][1]
                                user[indexUser]["Pengeluaran"] += data1["bulan"][angka-1][1]
                                user[indexUser]["Selisih"] = user[indexUser]["Pemasukkan"] - \
                                    user[indexUser]["Pengeluaran"]
                            with open("database.json", "w") as file:
                                json.dump(data, file, indent=4)
                            print('Transaksi BERHASIL')
                            t = False
                        else:
                            print('PIN ANDA SALAH')
                
                else:
                    os.system('cls')
                    print('ERROR')
                print(30*'_', )
                pilih = str(input('Lanjut ke menu utama?(Y/N): '))
                print(''' 
                              ''')
                if pilih.lower() == 'y':
                    os.system('cls')
                    menu()
                    menu_choice()
                else:
                    print('Terima Kasih, telah menggunakan aplikasi Nine Banking')
            else:
                print('Error')

   # LISTRIK
    elif choice == 5:
        global nometer, nm
        with open("database.json", "r") as f:
            data = json.load(f)
            user = data["user1"]
        os.system('cls')
        nominal = [20_000, 50_000, 100_000, 200_000,
                   500_000, 1_000_000, 5_000_000, 10_000_000]
        print('Beli Listrik')
        print(15*"_")
        m = True
        while m:
            nometer = input('Masukkan Nomor Meter: ')
            if len(nometer) == 11 or len(nometer) == 12:
                print(' ')
                print('Nomor Tujuan')
                print(15*"-")
                print(nometer, '- R1M / 900 VA')
                print('Sumber Dana')
                print(f'Rp {user[indexUser]["Saldo"]}')
                print(15*"-")
                print('Nominal')
                x = 0
                for i in range(0, 4):
                    print(41*"-")
                    print(
                        f'| Rp {nominal[x]} ({x+1})  | | Rp {nominal[x+1]} ({x+2})\t|')
                    x += 2
                print(41*"-")
                print('')
                choice_nominal = int(input('Pilih : '))
                nm = nominal[choice_nominal-1]
                aktivitas_recorder(choice)
                print(41*"_")
                print('Detail')
                print(
                    f'Nominal               \t Rp {nominal[choice_nominal-1]} ')
                print(f'Biaya Admin           \t Rp 0 ')
                print(41*'_')
                print(
                    f'Total                 \t Rp {nominal[choice_nominal-1]} ')
                print('Konfirmasi')
                t = True
                while t:
                    konfirmasi = (input('Masukkan PIN: '))
                    if konfirmasi == user[indexUser]['Password']:
                        import random
                        with open("database.json", "r") as f:
                            data = json.load(f)
                            user = data["user1"]
                            user[indexUser]["Saldo"] -= nominal[choice_nominal-1]
                            user[indexUser]["Pengeluaran"] += nominal[choice_nominal-1]
                            user[indexUser]["Selisih"] = user[indexUser]["Pemasukkan"] - \
                                user[indexUser]["Pengeluaran"]
                        with open("database.json", "w") as file:
                            json.dump(data, file, indent=4)
                        print('Token PLN Prabayar Anda')
                        for i in range(5):
                            for i in range(4):
                                print(random.randint(0, 9), end='')
                            print(' ', end='')
                        t = False
                    else:
                        print('PIN ANDA SALAH')
                print(' ')
                print(30*'_', )
                pilih = str(input('Lanjut ke menu utama?(Y/N): '))
                print(' ')
                if pilih .lower() == 'y':
                    menu()
                    menu_choice()
                    print('''
                          
                            ''')
                else:
                    print('Terima Kasih, telah menggunakan aplikasi Nine Banking')

            else:
                os.system('cls')
                print('No Meter yang Anda Masukkan SALAH, MOHON DITELITI LAGI')
                time.sleep(2)
                

# Function untuk menu Aktivitas dan menyimpan data ke file aktivitas.json
def aktivitas_recorder(aktivitas_counter):
    os.system('cls')
    if (aktivitas_counter == 1):
        with open("aktivitas.json", "r") as f:
            actv = json.load(f)
            temp = actv[f"act{str(indexUser + 1)}"]
            history_tarik = f"Penarikkan sebesar Rp {penarikan} berhasil..."
            temp.append(history_tarik)
        with open("aktivitas.json", "w") as file:
            json.dump(actv, file, indent=4)
        return history_tarik
    
    elif (aktivitas_counter == 2):
        with open("aktivitas.json", "r") as f:
            actv = json.load(f)
            temp = actv[f"act{str(indexUser + 1)}"]
            history_tarik = f"Transfer sebesar Rp {tf} ke {penerima} dengan NOMOR REKENING: {rekening}-{n_bank} berhasil..."
            temp.append(history_tarik)
        with open("aktivitas.json", "w") as file:
            json.dump(actv, file, indent=4)
        return history_tarik
    
    elif (aktivitas_counter == 3):
        with open("aktivitas.json", "r") as f:
            actv = json.load(f)
            temp = actv[f"act{str(indexUser + 1)}"]
            history_tarik = f"Top up {dg[choice1 - 1]} sebesar Rp {tf1} ke {nomor_hp} berhasil..."
            temp.append(history_tarik)
        with open("aktivitas.json", "w") as file:
            json.dump(actv, file, indent=4)
            
    elif (aktivitas_counter == 4):
        with open("aktivitas.json", "r") as f:
            actv = json.load(f)
            temp = actv[f"act{str(indexUser + 1)}"]
            if pilih1 == 'P':
                    history_tarik = f"Top up pulsa Rp {cn} ke {nohp} berhasil..."
                    temp.append(history_tarik)
            else:
                if kode == 'H':
                        history_tarik = f"Top up data harian Rp {data1['hari'][angka-1][1]} ke {nohp} berhasil..."
                        temp.append(history_tarik)
                elif kode == 'M':
                        history_tarik = f"Top up data mingguan Rp {data1['hari'][angka-1][1]} ke {nohp} berhasil..."
                        temp.append(history_tarik)
                elif kode == 'B':
                        history_tarik = f"Top up data bulanan Rp {data1['hari'][angka-1][1]} ke {nohp} berhasil..."
                        temp.append(history_tarik)
        with open("aktivitas.json", "w") as file:
             json.dump(actv, file, indent=4)
    else:
        with open("aktivitas.json", "r") as f:
            actv = json.load(f)
            temp = actv[f"act{str(indexUser + 1)}"]
            history_tarik = f"Pembelian listrik sebesar Rp {nm} ke {nometer}- R1M / 900 VA berhasil"
            temp.append(history_tarik)
        with open("aktivitas.json", "w") as file:
            json.dump(actv, file, indent=4)
        return history_tarik   
             
def akun():
        os.system('cls')
        with open("database.json", "r") as f:
            data = json.load(f)
            user = data["user1"]

        print(60*'_')
        print('AKUN'.center(60))
        print(60*'-')
        print(f'Nama                  :  {user[indexUser]["Nama Anda"]} ')
        print(f'No Rekening           :  {user[indexUser]["No. Rek"]}')
        print(f'Username              :  {user[indexUser]["Username"]}')
        print(f'Password              :  {user[indexUser]["Password"]}')
        print(60*'-')
        print('')
        print('Anda ingin log Out(L) atau Kembali ke Menu Utama (M)?: ')
        lm = input('pilih (L/M) : ')     
        if lm.lower() == 'l':
            depan()
            menu()
            menu_choice()
        else:
            menu()
            menu_choice()
                        

# Function pilih menu
def menu_choice():
    menu_choices = int(input('Pilih Menu : '))
    if menu_choices == 1:
        menu_home()
        menu()
    elif menu_choices == 2:
        with open("aktivitas.json", "r") as f:
            actv = json.load(f)
            test = 0
            temp = actv[f"act{str(indexUser + 1)}"]
            if len(temp) != 0:
                test += 1
            if test == 0:
                print(60*('_'))
                print('MENU AKTIVITAS')
                print(60*('_'))
                print('Tidak ada aktivitas')
                kembali = input('Klik K untuk kembali ke menu: ')
                print(60*('_'))
                if kembali.lower() == 'k':
                    os.system('cls')
                    menu()
                    menu_choice()
            else:
                print(60*('_'))
                print('MENU AKTIVITAS')
                print(60*('_'))
                temp = actv[f"act{str(indexUser + 1)}"]
                for j in temp:
                    print(j)
                kembali = input('Klik K untuk kembali ke menu: ')
                print(60*('_'))
                if kembali.lower() == 'k':
                    os.system('cls')
                    menu()
                    menu_choice()

        with open("aktivitas.json", "w") as file:
            json.dump(actv, file, indent=4)
    elif menu_choices == 3:
        akun()
# Menjalankan program
depan()
menu()
menu_choice()



