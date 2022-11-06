# Isi Kandungan

-   [1.0 Sama Saiz](#1.0-sama-saiz)

# 1.0 Sama Saiz

Diberi 2 input iaitu `m` dan `n`. `m` adalah panjang 1 tali manakala `n` adalah panjang tali yang diperlukan.

Kira, berapa banyak tali yang boleh dihasilkan mengikut saiz potongan yang dikehendaki.

## 1.1 Penyelesaian

Untuk masalah ini, apa yang kita perlu lakukan ialah bahagikan `m` dengan `n`. Setiap kali kita mendapat jawapan perpuluhan, kita perlu bundarkan ke bawah.

</br>

## 1.2 Penerangan

Berikut kita ada 1 tali yang panjangnya adalah 10 unit. Jika kita perlukan tali sepanjang 3 unit, maka kita akan memperoleh 3 tali dan baki 1 tali yang panjangnya hanya 1 unit. Oleh kerana tali baki itu tidak cukup panjang, maka kita akan abaikan tali tersebut dan hanya mentgambil kira 3 tali yang awal.

![Alt text](assets/strip_01.png)

# 2.0 Sistem Nombor

Diberikan satu nobor antara 0 hingga 77777. Nyatakan `sah` jika nombor tersebut merupakan asas 8 dan `tidak sah` jika sebaliknya.

## 2.1 Penyelesaian 1 (Semak setiap angka)

Menggunakan `for` loop, semak setiap angka dalam nombor yang diterima. Jika, ada angka yang bukan antara `0 hingga 7`, maka nombor itu bukanlah nombor asas 8. Kita boleh gunakan satu `flag` untuk tentukan jika nombor itu sah atau tidak. Sekiranya kita selesai menyemak kesemua angka dan tiada angka diluar `0 hingga 7`, maka nombor itu adalah sah.

## 2.2 Penyelesaian 2 (Menggunakan Regular Expression)

Menggunakan module `re`, kita boleh semak jika nombor tersebut mengandungi angka selain `0 hingga 7` dengan menggunakan regular expression. Yang pertama sekali, kita perlu `import re`.

```python
p = re.compile(r"[^0-7]+")
```

Code di atas mencipta satu `pattern` yang mencari character selain 0 hingga 7.
