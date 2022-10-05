## Link menuju aplikasi

https://tugas-pbp22.herokuapp.com/todolist/ <br>

## Akun pengguna dan dummy data

```
Username: pengguna1
Password: dummyuser1
```

```
Username: pengguna2
Password: dummyuser2
```

# TUGAS 4

## Apa kegunaan {% csrf_token %} pada elemen \<form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen \<form>?

Pada django, csrf_token berguna untuk menghidari serangan CSRF pada web. Django akan membuat suatu token pengenal saat <i>render</i> halaman web dan akan dicek apakah <i>request</i> dari <i>user</i> memiliki token yang sama. Jika sama, proses akan dilanjutkan dan jika tidak sama, tidak akan dilanjutkan.<br>

Jika tidak terdapat kode pembuat token seperti csrf_token, maka halaman tersebut tidak akan memiliki token pengenal dan setiap <i>request</i> yang datang akan diproses sehingga bisa saja <i>request</i> yang merupakan serangan kepada suatu server dapat terjadi.

## Apakah kita dapat membuat elemen \<form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat \<form> secara manual.

Bisa saja, tidak ada kewajiban untuk menggunakan generator dalam membuat suatu form.<br>

Untuk membuat form secara manual, kita bisa langsung menuliskannya pada berkas .html yang diinginkan sesuai dengan format tag \<form> yang berlaku. Contohnya saja seperti pada berkas login.html berikut:

```
<form method="POST" action="">
    {% csrf_token %}
    <table>
        <tr>
            <td>Username: </td>
            <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
        </tr>
                
        <tr>
            <td>Password: </td>
            <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
        </tr>

        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login"></td>
        </tr>
    </table>
</form>
```

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

<b>Asumsikan data yang disimpan bukan data seperti <i>username</i> dan <i>password</i>. Hanya berupa data biasa, dalam hal ini dapat seperti data pada model Task. Serta hanya menggunakan method "POST" untuk membuat data baru karena pada soal tidak diminta untuk memanipulasi data</b><br>

### Pembuatan berkas HTML
Pastikan telah membuat berkas .html yang sesuai dengan keinginan. Misalnya saja seperti berikut (dari berkas createtask.html). Ingat untuk membuat tag \<form> agar dapat menerima <i>input user</i>.

```
<div class = "create-task">

    <h1>Create Task</h1>

    <form method="POST" action="">
        {% csrf_token %}
            <p>Title:</p>
            <input type="text" name="title" placeholder="Title" class="form-control"><br/>
                    
            <p>Description:</p>
            <textarea cols="35" rows="8" name="description" placeholder="Description"></textarea><br/>
            
            <input type="submit" name="submit" value="Add">
    </form>
</div>
```

### Pengolahan data
Beberapa bagian penting, yaitu terdapat method "POST' untuk menambahkan data, terdapat <i>input text</i> dan <i>input button</i>.<br>

Setelah HTML berhasil di-<i>render</i>, maka <i>user</i> hanya tinggal mengisi form sesuai dengan ketentuan yang diinginkan dan pada sisi <i>server</i>, kita mengolah datanya pada berkas views.py (kode dibawah menggunakan contoh dari aplikasi ini)

```
if request.method == 'POST':
        task = Task()
        task.user = request.user
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('todolist:show_todolist')
```

Kita harus mengecek bahwa method yang digunakan adalah "POST". Jika benar maka harus membuat objek Task baru dan mengambil <i>input user</i>. Setelah diambil, maka kita harus menyimpan objek tersebut ke <i>database</i> menggunakan method save().

### Menampilkan data pada berkas HTML
Setelah berhasil dimasukkan ke dalam <i>database</i>, hal berikutnya adalah menampilkan datanya pada berkas .html yang diinginkan (contoh berikut berasal dari todolist.html)

```
{% if task|length != 0 %}
    <table>
            <tr>
                <th>Date</th>
                <th>Title</th>
                <th>Description</th>
                <th>Delete</th>
            </tr>
            {% for data in task %}
            <tr>
                <th>{{data.date}}</th>
                <th>{{data.title}}</th>
                <th>{{data.description}}</th>
                <th>
                    <button><a href="/delete">Hapus</a></button>
                </th>
            </tr>
        {% endfor %}
    </table>
{% else %}
    <p>Belum ada tugas</p>
{% endif %}
```

Pertama, periksa dahulu apakah <i>database</i> tersebut tidak kosong. Jika tidak kosong, maka lakukan looping untuk mengambil setiap datanya. Jika kosong, maka lakukan hal sesuai keinginan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama, buat terlebih dahulu aplikasi todolist dengan perintah

```
python manage.py startapp todolist
```

Kemudian, tambahkan pengaturan routing pada berkas urls.py di folder todolist serta pada variabel urlpatterns di folder project_django. Jangan lupa juga untuk mendaftarkan aplikasi tersebut pada setting.py di folder project_django. Routing pada urls.py disesuaikan dengan ketentuan tugas. (Bonus tidak dimasukkan pada jawaban ini) <br>

urls.py pada folder todolist

```
...
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
]
```

Tambahan urls.py di folder project_django

```
urlpatterns = [
    ...
    path('todolist/', include('todolist.urls')),
]
```

Tambahan setting.py di folder project_django

```
INSTALLED_APPS = [
    ...
    'todolist',
]
```

Kemudian, buat sebuah model pada models.py di folder todolist sesuai dengan ketentuan tugas.

```
class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
```

Implementasikan semua form sesuai tugas pada views.py di folder todolist. (Form berupa registrasi, login, dan logout)

```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')
```

Setelah itu, buat berkas .html untuk masing-masing form di atas pada berkas todolist/templates kecuali untuk logout<br>
[login.html](templates/login.html).<br>
[register.html](templates/register.html).<br>

Kemudian, buat dua berkas .html baru. Pertama adalah halaman utama todolist dan halaman untuk menambahkan <i>task</i> baru.<br>
Untuk halaman utama todolist dapat dilihat pada [link berikut](templates/todolist.html).<br>
Untuk halaman menambahkan <i>task</i> dapat dilihat pada [link berikut](templates/createtask.html).<br>

Jangan lupa juga untuk memasikan agar halaman utama todolist dapat dibuka hanya jika <i>user</i> telah login dengan menambahkan kode berikut

```
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    cuuser = request.user
    dataTask = Task.objects.all().filter(user = cuuser)
    context = {
        'user': cuuser,
        'task': dataTask,
    }
    return render(request, "todolist.html", context)
```

Terakhir lakukan <i>deployment</i> ke Heroku, baru setelah itu kita membuat <i>dummy</i> akun dan datanya. Jika ingin membuat <i>superuser</i>, maka sebelum melakukan <i>deployment</i> ke Heroku, kita harus menjalankan perintah berikut dan ikuti petunjuknya.

```
python manage.py createsuperuser
```

# TUGAS 5

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

### Perbedaan

| Inline CSS     | Internal CSS   | External CSS   |
| -------------- | -------------- | -------------- |
| Tidak memerlukan file .css | Tidak memerlukan file .css | Memerlukan file .css |
| Ditulis langsung pada atribut elemen HTML | Ditulis pada tag \<style> pada bagian header HTML | Ditulis pada file terpisah dari HTML |
| Ruang linkupnya hanya dalam satu elemen | Ruang lingkupnya hanya dalam satu HTML | Ruang lingkupnya bisa lebih dari satu HTML asalkan HTML tersebut menambahkan file .css |

### Kelebihan

<b>Inline CSS</b>
* Permintaan HTTP lebih kecil sehingga proses loading lebih cepat
* Cukup berguna jika hanya ingin terdapat perubahan di satu elemen

<b>Internal CSS</b>
* Hanya berlaku pada satu HTML saja sehingga perubahan style tidak mempengaruhi HTML lain
* Tidak perlu mengunggah banyak file karena kode CSS sudah di dalam HTML

<b>External CSS</b>
* Ukuran HTML menjadi lebih kecil
* Memisahkan antara pengaturan HTML dengan style CSS
* Dapat menerapkan style pada beberapa HTML

### Kekurangan

<b>Inline CSS</b>
* Tidak efisien jika ingin menerapkan style yang sama pada banyak elemen

<b>Internal CSS</b>
* Tidak bisa digunakan untuk beberapa HTML
* Memperberat proses loading web jika menggunakan HTML yang berbeda
* Ukuran HTML menjadi lebih besar

<b>External CSS</b>
* Bisa terjadi kegagalan pengambilan file CSS sehingga membuat HTML terlihat berantakan

Sumber: <br>
[Perbedaan Inline CSS, External CSS dan Internal CSS](https://www.hostinger.co.id/tutorial/perbedaan-inline-css-external-css-dan-internal-css)

## Jelaskan tag HTML5 yang kamu ketahui.

Asumsikan bahwa yang dijelaskan hanya tag yang baru dirilis saat HTML5.

| Jenis Tag | Penjelasan |
| --------- | ---------- |
| \<mark> | Untuk menyorot teks (<i>highlight</i>) |
| \<nav> | Untuk membuat navigasi pada halaman web |
| \<header> | Untuk menandai bagian header pada HTML |
| \<footer> | Untuk menandai bagian footer pada HTML |
| \<section> | Untuk membagi suatu halaman menjadi beberapa bagian |
| \<article> | Untuk menandai suatu konten utama |
| \<aside> | Untuk menambahkan konten sampingan |

Sumber: <br>
[Tag-tag Pada HTML beserta Fungsinya](https://gilacoding.com/read/tag-tag-pada-html-beserta-fungsinya)<br>
[HTML Element Reference](https://www.w3schools.com/tags/default.asp)

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.

| Jenis Selector | Penjelasan |
| --------- | ---------- |
| Selector Tag (Element) | Selector yang mewakili penggunaan tag pada HTML (tanpa awalan # atau .) |
| Selector Class | Selector yang akan digunakan jika menggunakan class tersebut (dengan awalan .) |
| Selector ID | Selector yang hanya dapat digunakan oleh satu elemen saja karena bersifat unik (dengan awalan #) |

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama, pilih dahulu ingin menggunakan framework yang mana (Saya memilih Bootstrap).<br>

Lalu tambahkan kode berikut pada berkas base.html sehingga menjadi:
```
...
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  {% block meta %}
  {% endblock meta %}
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
</head>

<body>
  {% block content %}
  {% endblock content %}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
</body>
...
```

Kemudian ganti berkas .html pada folder templates di aplikasi todolist sesuai dengan keinginan, contohnya di sini akan memakai berkas .html berikut:<br>

login.html, hanya menambahkan posisi agar berada di tengah halaman web.
```
...
<div class = "login position-absolute top-50 start-50 translate-middle">
...
<h1 style="text-align: center; margin-bottom: 20px;">Login</h1>
...
<input class="btn btn-primary d-flex flex-row-reverse" style="margin: 20px auto;" type="submit" value="Login">
...
```

todolist.html, menambahkan navbar.
```
...
<nav class="navbar navbar-expand-lg bg-primary" style="margin-bottom: 20px;">
    <div class="container-fluid">
        <a class="navbar-brand text-bg-primary" href="#">To Do List</a>
    <div class="navbar-nav float-end">
        <p style="margin: auto 20px; color: white;">Selamat datang, {{ user.username }}!</p>
        <button class="btn btn-danger"><a class = "link-light text-decoration-none" href="{% url 'todolist:logout' %}">Logout</a></button>
    </div>
    </div>
</nav>
...
```

todolist.html, mengubah penggunaan tabel menjadi card sesuai dengan ketentuan tugas 5.
```
...
  <div class="row" style="margin-left:10px; margin-right:10px">

    {% for data in task %}
      <div class="col-sm-6">
        {% if data.is_finished == True %}
          <div class="card text-bg-secondary mb-3">
            <div class="card-header">Added: {{data.date}}</div>
            <div class="card-body">
              <h5 class="card-title">{{data.title}}</h5>
              <p class="card-text">{{data.description}}</p>
              <a href="delete/{{ data.id }}" class="btn btn-danger">Remove</a>
              <button class="btn btn-success"><a class = "link-light text-decoration-none" href="update/{{ data.id }}">Unfinisihed</a></button>
            </div>
          </div>
        {% else %}
          <div class="card text-bg-success mb-3">
            <div class="card-header">Added: {{data.date}}</div>
            <div class="card-body">
              <h5 class="card-title">{{data.title}}</h5>
              <p class="card-text">{{data.description}}</p>
              <a href="delete/{{ data.id }}" class="btn btn-danger">Remove</a>
              <button class="btn btn-primary"><a class = "link-light text-decoration-none" href="update/{{ data.id }}">Finished</a></button>
            </div>
          </div>
        {% endif %}
      </div>
    {% endfor %}
  </div>
...
```

createtask.html, sama seperti todolist.html, menambahkan navbar dan menengahkan elemen form.
```
...
<nav class="navbar navbar-expand-lg bg-primary" style="margin-bottom: 20px;">
    <div class="container-fluid">
        <a class="navbar-brand text-bg-primary" href="#">To Do List</a>
        <div class="navbar-nav float-end">
            <p style="margin: auto 20px; color: white;">Selamat datang, {{ user.username }}!</p>
            <button class="btn btn-danger"><a class = "link-light text-decoration-none" href="{% url 'todolist:logout' %}">Logout</a></button>
        </div>
    </div>
 </nav>
...
<div class = "create-task" style="margin: 10px auto; max-width: 500px;">
...
```

register.html, menengahkan elemen dan mengubah style table.
```
...
<div class = "login position-absolute top-50 start-50 translate-middle">
...
<table class="table table-borderless">
...
<input class="btn btn-primary d-flex flex-row-reverse" style="margin: 20px auto;" type="submit" name="submit" value="Daftar"/> 
...
```