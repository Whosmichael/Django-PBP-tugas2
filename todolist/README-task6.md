**Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
Pemrograman asynchronous membuat program untuk mengeksekusi program tanpa menunggu eksekusi dari program lainnya dan pemrograman synchronous menunggu eksekusi program sebelumnya untuk mengeksekusi.

**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
Paradigma event-driven programming meupakan alur program yang berdasar atas event yang dilakukan antara user dan client. Sehingga terjadi pengiriman pesan yang berupa event yang akan diproses. Pada tugas ini penerapannya adalah onReady dimana program menunggu dokumen untuk fully loaded untuk running program

Jelaskan penerapan asynchronous programming pada AJAX.
Dengan menggunakan AJAX memungkinkan program untuk tetap berjalan tanpa dilakukan refresh page dengan cara memberikan pesan yang berisikan data2 yang dibutuhkan oleh views untuk melakukan perubahan di page

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
membuat method yang mengembalikan data task user dalam bentuk json
melakukan routing
Menggunakan GET untuk mengambil data dan mengiterasi ke semua elemen yang ada pada data tsb untuk memunculkanya ke page
Membuat modal
Membuat listener untuk button yang akan berfungsi sebagai submit
menambahkan task ke database degan memberikan request kepada views dan mengupdate cards2 yang ada dengan data yang baru
