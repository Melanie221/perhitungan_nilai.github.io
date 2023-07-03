data1=['MTK','BI','PKN','IPS','IPA']

input("Masukkan npm anda:")
input("Masukkan nama anda:")
kode=input("Masukkan kode:")
kode in data1
if 'MTK' in kode:
    print("Matematika")
elif 'BI' in kode:
    print("Bahasa Indonesia")
elif 'PKN' in kode:
    print("Pendidikan Kewarganegaraan")
elif 'IPS' in kode:
    print("Ilmu Pengetahuan Sosial")
elif 'IPA' in kode:
    print("Ilmu Pengetahuan Alam")

print(30*"_")
nilai1=int(input("Masukkan nilai tugas1:"))
nilai2=int(input("Masukkan nilai tugas2:"))
nilai3=int(input("Masukkan nilai ulangan:"))
nilai4=int(input("Masukkan nilai UTS:"))
nilai5=int(input("Masukkan nilai UAS:"))

n1=(10/100)*(nilai1+nilai2)
n2=(20/100)*nilai3
n3=(30/100)*nilai4
n4=(40/100)*nilai5

nilai_akhir=n1+n2+n3+n4
print("nilai", kode, "anda adalah:", nilai_akhir)

x=nilai_akhir
if 85 <= x <=100:
    print("Nilai anda adalah: A")
elif 70 <= x <=84:
    print("Nilai anda adalah: B")
elif 55 <= x <=69:
    print("Nilai anda adalah: C (Tidak Lulus)")
elif 30 <= x <=54:
    print("Nilai anda adalah: D (Tidak Lulus)")
elif 0 <= x <=29:
    print("Nilai anda adalah: E (Tidak Lulus)") 
