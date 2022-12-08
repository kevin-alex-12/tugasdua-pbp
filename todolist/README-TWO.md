## Link menuju aplikasi

https://tugas-pbp22.up.railway.app/todolist/ <br>

## Akun pengguna dan dummy data

```
Username: pengguna1
Password: dummyuser1

Username: pengguna2
Password: dummyuser2
```

##  Jelaskan perbedaan antara <i>asynchronous programming</i> dengan <i>synchronous programming</i>.

### Asynchronous programming

Program bisa dijalankan secara pararel (bersamaan) tanpa menunggu program sebelumnya diselesaikan.

### Synchronous programming

Program akan dijalankan secara berurutan, sehingga tidak ada program yang berjalan secara pararel (bersamaan). Program sebelumnya akan diselesaikan terlebih dahulu sebelum menjalankan program selanjutnya.

Sumber: <br>
[Memahami Synchronous dan Asynchronous dalam Pemrograman](https://community.algostudio.net/memahami-synchronous-dan-asynchronous-dalam-pemrograman/)

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma <i>Event-Driven Programming</i>. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

<i>Event-Driven Programming</i> adalah salah satu paradigma pemrograman di mana alur bekerjanya suatu program akan ditentukan oleh <i>event</i> yang dilakukan oleh pengguna.<br>

Dalam tugas ini, salah satu contohnya berupa <i>user click</i>. Saat pengguna mengklik <i>button</i> yang terdapat pada elemen HTML, maka akan memanggil <i>script</i> JavaScript yang telah disediakan sebelumnya. <i>Script</i> tersebut akan dijalankan hanya jika <i>button</i> telah di-klik sehingga sesuai dengan definisi paradigma di atas.

##   Jelaskan penerapan <i>asynchronous programming</i> pada AJAX.

Salah satu penerapannya menggunakan Objek XMLHttpRequest sebagai media pertukaran data dengan web server.

1. Saat AJAX dipanggil, browser akan menyiapkan objek XMLHttpRequest untuk pertukaran data dengan web sever.
2. Pertukaran data pada XMLHttpRequest akan berjalan secara <i>asynchronous</i>, sehingga tinggal menunggu server merespons data yang dikirimkan
3. Setelah server mengirimkan respons, data akan langsung ditampilkan pada broswer

##   Jelaskan bagaimana cara kamu mengimplementasikan <i>checklist</i> di atas.

### AJAX GET

Untuk membuat AJAX, hanya perlu menyisipkan script pada bagian \<head> atau \<body> (pada tugas ini akan disisipkan pada \<head>) dengan menggunakan tag \<script>.<br>

Untuk AJAX GET, pertama buat dahulu routing dan function seperti tugas-tugas terdahulu sesuai dengan spesifikasi soal yang berguna untuk menghasilkan data.<br>

Pada views.py
```
...
@login_required(login_url='/todolist/login/')
def show_json(request):
    cuuser = request.user
    dataTask = Task.objects.all().filter(user = cuuser)
    return HttpResponse(serializers.serialize("json", dataTask), content_type="application/json")
...
```

Pada urls.py
```
urlpatterns = [
    ...
    path('json/', show_json, name='show_json'),
    ...
]

```

Setelah itu langsung saja tambahkan script pada berkas [todolist.html](templates/todolist.html). Script akan bekerja saat web telah selesai di-load dan akan mengambil data dari path /todolist/json dan akan diiterasi untuk setiap elemen untuk memilah antara yang telah selesai dengan yang belum selesai. Setelah itu, akan dibuat elemen div baru yang sesuai.<br>

### AJAX POST

Untuk AJAX POST, pertama buat dahulu routing dan function seperti tugas-tugas terdahulu sesuai dengan spesifikasi soal yang berguna untuk menghasilkan data.<br>

Pada views.py
```
...
@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == 'POST':
        task = Task()
        task.user = request.user
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('todolist:show_todolist')
...
```

Pada urls.py
```
urlpatterns = [
    ...
    path('add/', add_task, name='add_task'),
    ...
]

```

Jangan lupa juga membuat modal yang dapat diambil dari dokumentasi Bootstrap dan mengubahnya sesuai keinginan. Setelah itu langsung saja tambahkan script berikut pada berkas [todolist.html](templates/todolist.html). Script akan diaktifkan jika form dengan id = addTask di-klik dan akan mengirimkan data yang telah diubah menjadi format yang sesuai ke path sesuai yang tertulis pada kode dibawah ini. Setelah selesai mengirimkan data, modal akan dihapus dan form akan di-reset kembali. Jangan lupa juga untuk menerapkan asinkronus sehingga tidak perlu reload seluruh halaman.

```
$("#addTask").submit(function (e) {
      e.preventDefault();
      var serializedData = $(this).serialize();
      $.ajax({
          url: "{% url 'todolist:add_task' %}",
          type: "POST",
          data: serializedData,
          dataType: 'text',
          success: function (data) {
              $("#exampleModal").modal('hide');
              $('#addTask').each(function () {
                  this.reset();
              });

              // Empty div class and make new
              $("#data").empty();
              $.get( "{% url 'todolist:show_json' %}", function(data) {
                taskData(data);
              });
        }
    });    
});
```