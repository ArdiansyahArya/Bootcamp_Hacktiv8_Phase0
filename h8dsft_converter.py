# Fungsi Konversi Kelvin ke Celcius dan Celcius ke Kelvin

# Argumen jenis temperatur yang dapat di input
# 'kelvin' untuk kelvin
# 'celcius' untuk celcius

SK=0
SC=0

def konversiKC(suhu, jenis_temperatur): # Fungsi konversi kelvin ke celcius
    if jenis_temperatur == "kelvin": # Parameter yang mendeteksi bahwa input suhu adalah satuan kelvin
        C = suhu -273.15 
        print (f'Konversi dari suhu {suhu} derajat kelvin menghasilkan suhu {round(C,2)} derajat Celcius')
        SC = 1
    elif jenis_temperatur == "celcius": # Parameter yang mendeteksi bahwa intpu suhu adalah satuan celcius
        K = suhu +273.15
        print (f'Konversi dari suhu {suhu} derajat celcius menghasilkan suhu {round(K,2)} derajat Kelvin')
        SK = 1
    else : # Bila input jenis_temperatur diluar dari suhu kelvin dan celcius atau salah input
        print("Jenis temperatur tidak diketahui atau salah input")

# Fungsi konversi suhu ke fahrenheit

def konversitoF(suhu, jenis_temperatur):
    if jenis_temperatur == "kelvin": # Parameter yang mendeteksi bahwa input suhu adalah satuan kelvin
        F = (suhu * (9/5)) - 459.67
        print(f'Konversi dari suhu {suhu} derajat Kelvin menghasilkan suhu {round(F,2)} derajat Fahrenheit')
    elif jenis_temperatur == "celcius": # Parameter yang mendeteksi bahwa input suhu adalah satuan celcius
        F = ((9/5)*suhu) + 32
        print(f'Konversi dari suhu {suhu} derajat Celcius menghasilkan suhu {round(F,2)} derajat Fahrenheit')
    else: # Bila input suhu diluar dari satuan kelvin dan celcius atau salah input
        print("Jenis temperatur tidak diketahui atau salah input")

# Fungsi konversi fahrenheit dari fahrenheit.

def konversifromF(suhu, jenis_temperatur_output):
    if jenis_temperatur_output == "kelvin":
        K = (suhu + 459.67) * (5/9)
        print(f'Konversi dari suhu {suhu} derajat Fahrenheit menghasilkan suhu {round(K,2)} derajat Kelvin')
    elif jenis_temperatur_output == "celcius":
        C = (suhu - 32) * (5/9)
        print(f'Konversi dari suhu {suhu} derajat Fahrenheit menghasilkan suhu {round(C,2)} derajat Celcius')
    else: # Bila output suhu yang diinginkan diluar dari satuan kelvin dan celcius atau salah input
        print("Jenis temperatur tidak diketahui atau salah input")

konversiKC(100, "celcius")
konversitoF(100, "kelvin")
konversifromF(100, "celcius")