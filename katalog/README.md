Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
![PBP Diagram](https://github.com/Whosmichael/Django-PBP-tugas2/blob/main/PBPDiagram.png?raw=true)

-Saat client me-request untuk menuju ke server melalui link url, django akan mengintegrasikan link url yang telah client request dengan link url yang telah didefinisikan pada file urls.py yang ada pada folder project_django.
-Link url akan didefinisikan ke dalam fungsi tertentu yang terdapat pada views.py yang kemudian akan memanggil fungsi view.
-Fungsi view ini akan request ke database dengan menggunakan penghubung dengan memanggil objek yang terdapat pada models.py.
-Fungsi view akan meresponse dengan menampilkan template html
-Kemudian akan di render oleh template sehingga akan memunculkan display interface yang akan dilihat user.

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Dalam membuat sebuah proyek django, kita tentunya dapat membuat tanpa virtual environment. Kita menggunakan virtual environment agar dapat memisahkan dependencies antar project dan mencegah gangguan sistem lainnya. Jika kita ingin membuat aplikasi yang tidak akan diakses oleh umum dan hanya untuk sementara, maka tidak membutuhkan virtual environment.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
- Pada folder katalog, di file views.py, terdapat fungsi show_catalog dengan parameter request dari user. show_catalog akan menggunakan class dari model yang kemudian akan request data ke database dan menyimpan hasil request tersebut ke dalam data_barang_katalog. Kemudian,file katalog.html di-render untuk dimunculkan di halaman HTML.
- Menambahkan path('katalog/', include('katalog.urls')) ke urls.py di folder project_django
- Fungsi view pada views.py melakukan render ke katalog.html. Saat render di-mapping dengan sintaks {{data}} dan data yang ada akan di-mapping ke halaman HTML dan dilakukan looping pada list katalog untuk mengambil data dari database, yang kemudian akan ditampilkan pada user.
-Pertama kita connect heroku dengan repository pada github kita untuk melakukan deployment. Kemudian aplikasi di deploy pada heroku console. Kita menginput heroku app name dan heroku api key pada github secret, agar repository dapat terhubung ke heroku.