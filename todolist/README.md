## Link menuju aplikasi

https://tugas-pbp22.herokuapp.com/todolist/ <br>

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