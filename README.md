# Script KRS IPB
script untuk mengambil krs di IPB secara otomatis

`created by dafaath with python`

## Penggunaan
1. Clone repo ini `git clone https://github.com/dafaath/script-KRS-IPB.git`
2. Install python 3 dan pip, [tutorial disini](https://phoenixnap.com/kb/how-to-install-python-3-windows)
3. Setelah install buka terminal (cmd/powershell) di direktori file ini
4. Gunakan command `pip3 -r requirements.txt`, tunggu sampai proses selesai
5. Pastikan sudah install chrome di komputer anda
6. Buat file dengan nama config.json (nama harus persis) di direktori ini, sehingga setara dengan scriptkrs.py
7. masukan text ini di config.json
```
{
  "username": "",
  "password": "",
  "jadwal": [{
        "matkul": "",
        "kuliah": "",
        "praktikum": ""
    }]
}
```
8. `username` isi dengan username akun IPB, `password` juga isi dengan passwordnya, untuk `matkul` bisa diisi kode dari matkul tersebut (ex:KOM300) `kuliah` adalah pararel kuliah yang ingin diambil, dan `praktikum` adalah pararel praktikum yang ingin diambil. Jika tidak ada praktikum bisa dikosongkan saja 
9. Contoh pengisiian config.json
```
{
  "username": "namadanusernameasal",
  "password": "passwordyangtidakkuat",
  "jadwal": [{
        "matkul": "KOM300",
        "kuliah": "1",
        "praktikum": "1"
    },
        {
        "matkul": "KOM311",
        "kuliah": "2",
        "praktikum": "1"
    },
        {
        "matkul": "KOM321",
        "kuliah": "2",
        "praktikum": "1"
    },
        {
        "matkul": "KOM325",
        "kuliah": "1",
        "praktikum": "1"
    },
        {
        "matkul": "KOM333",
        "kuliah": "2",
        "praktikum": "2"
    },
        {
        "matkul": "KOM335",
        "kuliah": "2",
        "praktikum": "1"
    }]
}
```
10. Setelah config.json dibuat dan diisi dengan data yang benar kita bisa menjalankan scriptnya
```
python3 scriptkrs.py
```
