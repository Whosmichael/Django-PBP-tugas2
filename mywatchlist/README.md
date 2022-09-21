**Jelaskan perbedaan antara JSON, XML, dan HTML!**

Definisi

1.  JSON adalah singkatan dari JavaScript Object Notation. JSON didesain menjadi self-describing, sehingga JSON sangat mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile, 
    yaitu untuk menyimpan dan mengirimkan data. Sintaks JSON merupakan turunan dari Object JavaScript.
    
2.  XML (Extensive Markup Language), adalah bahasa markup bersifat extensible yang berguna untuk menyimpan data. XML digunakan untuk mendefinisikan elemen markup dan menghasilkan bahasa markup yang disesuaikan.

3.  HTML (Hypertext Markup Language), adalah bahasa markup ysng digunakan untuk mendefinisikan struktur laman web. HTML dapat menampilkan elemen-elemen seperti button, hyperlink, image, dan data dari database terkait.

Perbedaan antara XML dan JSON

Penggunaan XML:

1.  menghasilkan dokumen dengan format XML ``(.xml) ``
2.  DOM Menyimpan value dalam variabel
3.  Jika ingin melakukan looping, harus menggunakan XML
4.  Berasal dari SGML

Penggunaan JSON:

1.  Memiliki produk JSON string ``(.json)``
2.  Menggunakan JSON.parse() untuk parse pada JSON string
3.  Relatif lebih mudah dan cepat dibandingkan XML. Terutama bagi beberapa aplikasi.
4.  Dibuat berdasarkan JavaScript

Mengapa saya tidak ikut membandingkan HTML dengan XML dan JSON?
HTML tidak dapat dibandingkan, karena HTML hanya berguna untuk menampilkan struktur laman web. HTML lebih fokus pada presentasi dari data yang ada ke dalam sebuah laman web

Contoh:

XML

``` py
<?xml version="1.0" encoding="UTF-8"?>
<phone>
  <brand>Apple</brand>
  <type>iPhone 14 plus</type>
  <color>Red</color>
  <memory>256</memory>
</phone>

```

JSON

```py
{
    "brand": "Samsung",
    "type": "S22 Ultra",
    "color": "Black",
    "memory": "256",
}

```

HTML

```py

<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>

<p>My first paragraph.</p>

</body>
</html>

```

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Pada proses kerja platform, data delivery merupakan hal yang sangat esensial. Kita membutuhkan data delivery untuk menampilkan data dari database pada laman yang ditampilkan. Sebagai contoh, pada smartphone kita terdapat waktu terkini pada interface-nya, jika tidak ada proses data delivery maka hal tersebut tidak dapat ditampilkan pada interfacenya. Artinya tujuan dari program jam tersebut tidak tercapai.



**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

Pertama saya melakukan hal yang saya lakukan di lab 1.

Pertama saya membuat app Django baru dengan nama mywatchlist. Kemudian saya menambahkan mywatchlist pada variabel INSTALLED_APPS yang ada di ``settings.py`` sebagai aplikasi baru. 
Lalu, di ``models.py`` input atribut sesuai kebutuhan (dalam hal ini sesuai soal) seperti di bawah ini.
``` py
class Watchlists(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
```

Membuat data yang akan digunakan pada ``initial_mywatchlist_data.json``. Dibuat dalam folder fixtures
Kemudian saya membuat file mywatchlist.html
Memodifikasi dan menambahkan path di file urls.py (di folder project-django)
Membuat fungsi-fungsi pada ``views.py``, yang berguna untuk penyajian dalam format HTML,JSON, dan XML
Kemudian, membuat routing mywatchlist di urls.py.
Push ke GitHub. Setelah di-push, deployment akan bekerja secara otomatis


**Mengakses URL yang ada pada postman**

JSON

![Screenshot (388)](https://user-images.githubusercontent.com/90233205/191586302-51e4ba84-f2da-4c36-9990-86dea8eae0af.png)

XML

![Screenshot (387)](https://user-images.githubusercontent.com/90233205/191586574-37501d77-0140-4eed-a066-eb4aa365b7ba.png)

HTML

![Screenshot (386)](https://user-images.githubusercontent.com/90233205/191586689-5413486e-6d4a-4124-91ac-32c884bcfc5e.png)



























