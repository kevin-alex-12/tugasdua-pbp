## Link menuju aplikasi

https://tugas-pbp22.herokuapp.com/mywatchlist/ <br>
https://tugas-pbp22.herokuapp.com/mywatchlist/html/ <br>
https://tugas-pbp22.herokuapp.com/mywatchlist/json/ <br>
https://tugas-pbp22.herokuapp.com/mywatchlist/xml/

##  Jelaskan perbedaan antara JSON, XML, dan HTML!

| JSON        | XML        | HTML        |
| ----------- | ---------- | ----------- |
| Ekstensi file .json | Ekstensi file .xml | Ekstensi file .html |
| Penyimpanan data sulit untuk dilihat | Penyimpanan data lebih terstruktur dan mudah dibaca | Penyimpanan data memiliki bagian masing-masing |
| Berfokus untuk transfer data | Berfokus untuk transfer data | Berfokus untuk penyajian data |
| Data lebih efisien | Data kurang efisien | Data kurang efisien |
| Tidak perlu tag | Perl tag | Perlu tag |
| Pembacaan lebih cepat | Pembacaan lambat | Pembacaan lambat |
| Dalam format JavaScript | Tidak ada format | Tidak ada format |

Sumber: <br>
[Apa itu JSON? Simak Perbedaannya dengan XML](https://www.dicoding.com/blog/apa-itu-json/) <br>
[Apa Perbedaan JSON Dan XML?](https://www.monitorteknologi.com/perbedaan-json-dan-xml/)

##  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Dalam mengintegrasikan platform, kita perlu mentransfer data antarplatform tersebut. Oleh karena itu, kita memerlukan data delivery agar data-data tersebut dapat melintas antarplatform. Tidak semua data cocok untuk digunakan pada suatu platform sehingga terdapat banyak tipe data yang tersedia dan dapat disesuaikan dengan platform yang akan dikirimkan datanya.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama, buat terlebih dahulu aplikasi mywatchlist dengan perintah

```
python manage.py startapp mywatchlist
```

Kemudian, tambahkan pengaturan routing pada berkas urls.py di folder mywatchlist serta pada variabel urlpatterns di folder project_django. Jangan lupa juga untuk mendaftarkan aplikasi tersebut pada setting.py di folder project_django. Semua pengaturan routing pada berkas urls.py di folder mywatchlist disesuaikan dengan permintaan soal Tugas 3.<br>

Berkas [urls.py](urls.py) di folder mywatchlist. <br>

Tambahan urls.py di folder project_django
```
urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]
```

Tambahan setting.py di folder project_django
```
INSTALLED_APPS = [
    ...
    'mywatchlist',
]
```

Setelah itu, buat pengaturan respons web pada berkas views.py di folder mywatchlist sesuai dengan spesifikasi pada soal Tugas 3. Untuk kode views.py bisa dilihat pada [link berikut](views.py) <br>

Tambahkan juga berkas .html pada folder templates yang sesuai dengan keinginan kita untuk menampilkan data dalam bentuk HTML. <br>

Jangan lupa untuk membuat model dari data yang ingin kita gunakan dalam aplikasi mywatchlist. Model data tersebut dapat dibuat pada file [models.py](models.py). Setelah model selesai dibuat, buat juga datanya pada folder fixtures dengan file [initial_watchlist_data.json](fixtures/initial_watchlist_data.json). Sesuaikan format, apa saja informasi, dan banyaknya data yang ingin dimasukkan dengan spesifikasi soal Tugas 3. <br>

Setelah selesai, jangan lupa untuk menjalankan perintah
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_watchlist_data.json
```

Jika diperlukan, dapat juga menambahkan unit test untuk memeriksa apakah URL yang telah dilakukan routing sebelumnya telah berfungsi dengan baik. Buat unit test tersebut pada file tests.py. Kode tests.py bisa dilihat pada [link berikut](tests.py).

Langkah berikutnya, hubungkan repository GitHub (asumsikan sudah dibuat repository dan telah dilakukan git add, git commit, dan git push) dengan Heroku jika belum melalui konfigurasi github (setting -> secrets -> actions). Data untuk penghubung antara keduanya diberi nama HEROKU_API_KEY dan HEROKU_APP_NAME.

## Tangkapan Layar dari Postman (Untuk Localhost dan Heroku)

### HTML
Untuk localhost
![html](htmllokal.jpg?raw=true)
Untuk Heroku
![html](htmlheroku.jpg?raw=true)

### JSON
Untuk localhost
![json](jsonlokal.jpg?raw=true)
Untuk Heroku
![json](jsonheroku.jpg?raw=true)

### XML
Untuk localhost
![html](xmllokal.jpg?raw=true)
Untuk Heroku
![html](xmlheroku.jpg?raw=true)