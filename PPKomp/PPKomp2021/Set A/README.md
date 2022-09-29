# Ayam dan Kambing

Bagi soalan ayam dan kambing ini, kita tahu bahasa seekor ayam mempunyai 2 kaki dan seekor kambing mempunyai 4 kaki. Oleh itu, kita hanya perlu darabkan bilangan ayam bersama bilangan kaki bagi seeokor ayam dan tambahkan dengan hasil darab antara bilangan kambing dengan bilangan kaki bagi seekor kambing. Untuk mendapatkan jumlah mata pula, kita hanya perlu tambahkan bilangan ayam dan bilangan kambing. Jumlah ini lalu di darabkan dengan 2 kerana ayam dan kambing mempunyai 2 mata.

# Beza Usia Syiling

Kita mempunya 2 input iaitu tahun bagi syiling A dan tahun bagi syiling B. Untuk dapatkan beza usia syiling ini, kita hanya perlu tolakkan tahun syiling A dengan tahun syiling B. Tetapi, kita mungkin akan mendapat hasil negatif kerana kita tidak tahu mana satu syiling yang lebih lama usianya. Oleh itu, kita perlu menggunakan fungsi yang tersedia dalam python iaitu `abs()` untuk pastikan hasil tolak itu sentiasa positif.

# Buku 1

Disini kita mempunya 2 input iaitu mukasurat mula `M` dan mukasurat akhir `N`. Untuk mendapatkan jumlah mukasurat yang telah dibaca, kita perlu cari beza mukasurat antara M dan N iaitu `beza_mukasurat = N-M`
Akhir sekali, kita perlu tambah 1 pada hasil tolak N dan M untuk mendapatkan jumlah mukasurat yang telah dibaca.

# Gula Gula dalam Cawan

Soalan ini sangat mudah. Yang pertama sekali, kita perlu cari bilngan gula-gula warna mera iaitu `Gula-gula Hijau - 3`. Kemudian kita boleh mengira bilangan gula-gula warna biru dengan `Gula-gula Merah + 10`

# Jujukan Huruf A-G

Pertama sekali, kita sediakan satu senari yang mengandungi semua huruf yang akan muncul iaitu huruf A hingga huruf G. Kemudian, kita dapatkan bilangan huruf yang terdapat dalam `set_huruf` ini menggunakan fungsi yang tersedia dalam python iaitu `n_set_huruf = len(set_huruf)`. Akhir sekali, kita moduluskan input `n` bersama `n_set_huruf` untuk mendapatkan nombor elemen ulangan dan tolakkan 1 untuk dapatkan nombor index huruf dalam `set_huruf`.

# Jujukan Nombor

Untuk masalah ini, teradapat 2 cara penyelesaian iaitu menggunakan `for` untuk kira satu persatu jujukan nombor yang diberikan. Penyelesaian ini agak perlahan jika input yang diberikan adalah satu nombor yang besar. Oleh itu, kita lihat kaedah yang kedua.

Jika kita lihat pada jujukan nombor dari 1 sehingga 5, kita akan dapat:

`-1, 2, -3, 4, -5`

Jika kita pecahkan nombor ini kedalam satu kelompok kumpulan, kita akan dapat:

`(-1, 2), (-3, 4), (-5, 6)`

Jika kita mendapat input 2, maka input 2 berada dalam kumpulan pertama. Oleh itu, jawapan bagi input 2 ialai 1 kerana:

1. Input 2 dalam kumpulan 1
2. Input 2 adalah genap

Jika input yang diberikan adalah 3 maka jawapannya adalah -2, kerana:

1. Input 3 dalam kumpulan 2
2. Input 3 adalah ganjil

Oleh itu, input yang kita dapat akan dibahagikan dengan 2 dan dibundarkan keatas menggunakan fungsi `ceil` daripada module `math`. Jika input itu adalah genap, maka jawapannya adalah positif, tetapi jika input itu adalah ganjil, maka kita darapkan hasil bahagi itu dengan -1 untuk mendapatkan jawapan negatif.
