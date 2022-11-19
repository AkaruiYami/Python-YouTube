# Isi Kandungan

-   [1.0 Sama Saiz](#1.0-sama-saiz)
-   [2.0 Sistem Nombor](#2.0-sistem-nombor)
-   [3.0 Markah Peperiksaan 1](#3.0-markah-peperiksaan-1)
-   [4.0 Sistem 24 Jam](#4.0-sistem-24-jam)

# 1.0 Sama Saiz

Diberi 2 input iaitu `m` dan `n`. `m` adalah panjang 1 tali manakala `n` adalah panjang tali yang diperlukan.

Kira, berapa banyak tali yang boleh dihasilkan mengikut saiz potongan yang dikehendaki.

## 1.1 Penyelesaian

Untuk masalah ini, apa yang kita perlu lakukan ialah bahagikan `m` dengan `n`. Setiap kali kita mendapat jawapan perpuluhan, kita perlu bundarkan ke bawah.

</br>

## 1.2 Penerangan

Berikut kita ada 1 tali yang panjangnya adalah 10 unit. Jika kita perlukan tali sepanjang 3 unit, maka kita akan memperoleh 3 tali dan baki 1 tali yang panjangnya hanya 1 unit. Oleh kerana tali baki itu tidak cukup panjang, maka kita akan abaikan tali tersebut dan hanya mentgambil kira 3 tali yang awal.

![Alt text](assets/strip_01.png)

## 1.3 Video Penerangan:

[![YouTube PPKomp2022 Set A Q1](https://img.youtube.com/vi/SYDVUrEPaIQ/0.jpg)](https://www.youtube.com/watch?v=SYDVUrEPaIQ)

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

## 2.3 Video Penerangan

[![YouTube PPKomp2022 Set A Q2](https://img.youtube.com/vi/YtzRZ-dUKSE/0.jpg)](https://www.youtube.com/watch?v=YtzRZ-dUKSE)

# 3.0 Markah Peperiksaan 1

Diberi 4 string input berformat `{markah}/{markah penuh}`. Daripada 4 string ini, cari dan paparkah subjek peperiksaan yang mendapat markah tertinggi.

## 3.1 Peneyelesaian

Cipta sati dictionary untuk simpan markah bagi setiap subjek. Kita namakan dictionary ini sebagain `marks`. Untuk setiap subjek, kita dapatkan kirakan markah menggunakan fungi `eval()`.

```python
marks["Sains"] = eval(input())
```

Code diatas menetapkan markah bagi subjek `Sains` kepada nilai input yang dikira. Fungi `eval()` mengambil satu string dan mengeluarkan nilai setelah string itu dinilai. Contohnya, `eval("10/2")` akan pulangkan hasil bahagi 10 / 2, iaitu `5`.

Menggunakan fungsi `max()` kita akan cari nilai paling besar dalam dictionary marks. Kita beri argument tambahan, `key = marks.get` kepada fungsi `max()` untuk pastikan fungsi tersebut mmembandingkan nilai berdasarkan `value` dictionary dan bukannya `key` dictionary tersebut.

# 4.0 Sistem 24 Jam

Diberi 2 baris input. Baris pertama merupakan masa dalam format _hh:mm_ dimana _hh_ adalah jam dan _mm_ adalah minit yang dipisahkan dengan :. Baris kedua pula merupakan _x_ minit. Cari dan paparkan masa setelah _x_ minit berlalu daripada input pertama.

## 4.1 Penyelesaian

Menggunakan module `datetime`, kita boleh mengira masa yang berlalu dengan mudah. Untuk input baris pertama, masukkan input tersebut kepada fungsi datetime seperti yang ditunjukkan di bawah:

```python
import datetime

input1 = input()
masa_awal = datetime.datetime.strptime(input1, "%H:%M")
```

Dalam method `strptime()` kita perlu sertakan sekalai format masa yang kita ada iaitu dalam kes ini, format input kita ialah JAM:MINIT dimana `%H` merujuk kepada jam, dan `%M` merujuk kepada minit.

Seterusnya, input kedua akan dimasukkan ke dalam fungsi `timedelta()` daripada module `datetime` seperti di bawah:

```python
x = input()
d = datetime.timedelta(minutes = int(x))
```

Akhir sekali, tambahkan `masa_awal` dengan `d` untuk mendapatkan jawapan bagi masalah ini.

```python

jawapan = masa_awal + d
print(jawapan)
```
