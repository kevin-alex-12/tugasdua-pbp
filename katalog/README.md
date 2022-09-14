##### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
![bagan](/bagandjango.png)

##### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab: Virtual environment digunakan untuk mengisolasi lingkungan virtual python agar tidak bisa diakses dari luar. Selain itu untuk menghindari adanya upgrade modul global yang menyebabkan aplikasi web yang dibuat bisa saja tidak bisa digunakan karena harus menggunakan versi modul tertentu. Kita bisa saja membuat aplikasi web tersebut tanpa menggunakan virtual environment, tetapi kita harus berhati-hati dalam menginstall/upgrade modul-modul yang digunakan.

##### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Jawab:
[Poin 1] Sesuai dengan lab 1, saya membuat fungsi yang menerima parameter request dan mengembalikan response sesuai dengan permintaan tugas 2

views.py di folder katalog
```pyhton 
from django.shortcuts import render

# Create request parameter.
def show_katalog(request):
    return render(request, "katalog.html")
```

[Poin 2] Menambahkan pengaturan routing pada berkas urls.py di folder katalog yang telah disediakan sebelumnya dan mendaftarkan juga katalog di berkas urls.py pada folder project_django pada variabel urlpatterns. Jangan lupa juga untuk mendaftarkannya di setting.py pada folder project_django

urls.py di folder katalog
```pyhton
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```

urls.py di folder project_django
```pyhton
....
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
]
....
```

setting.py di project_django
```pyhton
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'example_app',
    'katalog',
]
```

[Poin 3] Mengubah isi views.py agar dapat menerima data yang disimpan untuk diproses dalam aplikasi web serta menambahkan kode html yang dapat menerima parameter request agar dapat menampilkan data yang sesuai

views.py di folder katalog
```
from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Kevin Alexander',
        'studentid': '2106705026'
    }
    return render(request, "katalog.html", context)
```

---- berkas html
```html
{% for barang in list_barang %}
    <tr>
        <th>{{barang.item_name}}</th>
        <th>{{barang.item_price}}</th>
        <th>{{barang.item_stock}}</th>
        <th>{{barang.rating}}</th>
        <th>{{barang.description}}</th>
        <th>{{barang.item_url}}</th>
    </tr>
    {% endfor %}
```

[Poin 4] Menghubungkan repository github dengan heroku melalui konfigurasi github (setting -> secrets -> actions). Data untuk penghubung antara keduanya diberi nama HEROKU_API_KEY dan HEROKU_APP_NAME.