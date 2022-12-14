# Isi Kandungan

-   [1.0 Jujukan Nombor](#10-jujukan-nombor)
-   [2.0 Sistem 24-Jam](#20-sistem-24-jam)
-   [3.0 Markah Peperiksaan](#30-markah-peperiksaan)

# 1.0 Jujukan Nombor

Diberkan 2 input. Input pertama merupakan 3 integer bagi 3 nombor pertama dalam satu jujukan nombor. Input kedua merupakan `n` iaitu bilangan sebutan yang perlu ditambah ke dalam jujukan. Output bagi soalan ialah ialah satu jujutan nombor yang mempunya 3 + n sebutan nombor.

# 1.1 Penyelesaian Menggunakan List Comprehension

Disini kita mendapatkan 2 bari input iaitu `t` dan `n_adds`. `t` merupakan satu list integer yang menyimpan 3 sebutan pertama bagi jujukan nombor tersebut. Untuk mendapatkan sebutan seterusnya, kita perlu mencari **beza sama** _(common difference)_ bagi sebutan tersebut dengan formula tersebut `d = t[1] - t[0]`.

Menggunakan **list comprehension**, kira sebutan nombor seterusnya dengan menambahkan `d` ke setiap sebutan akhir.

```python
next_t = [t[-1] + (d * n) for n in range(1, n_adds+1)]
```

Merujuk pada code di atas, `t[-1]` ialah nilai akhir dalam 3 sebutan yang diberi. `next_t` mengandungi sebutan seterusnya selepas 3 sebutan yang diberi.

Jawapan bagi soalan ini ialah:

```python
print(*t, *next_t)
```

# 2.0 Sistem 24-Jam

Diberi 2 baris input. Baris pertama adalah sastu string berformat _hh:mm:ss_ manakala baris kedua adalah `x` iaitu integer mewakili jumlah saat. Kira dari paparkan masa selepa `x` saat berlalu.

# 2.1 Peneyelesaian Menggunakan Module datetime

Pertama sekali, import modul `datetime`. Kemudian kita cipta satu datetime objek menggunakan input pertama. Kemudian hasilkan satu objek menggunakan deltatime dari modul datetime dengan parameter `s = x`. `x` merupakan input kedua. Penyelesaian bagi masalah ini adalah hasil tambah antara objek datetime dan deltatime dan paparkan menggunakan format masa yang bertul.

# 3.0 Markah Peperiksaan

Baris pertama merupakan satu integer `n` yang mewakili bilangan subjek yang diambil. Manakala input kedua pula merupakan satu senarai string yang mewakili nama subjek dan markah bagi subjek tersebut dalam format `NAMA_SUBJEK, MARKAH_PEROLEH/MARKAH_PENUH`. Cari dan paparkan nama subjek yang mempunyai peratusan tertinggi berbanding subjek-subjek lain.

# 3.1 Penyelesaian

Menggunakan fungsi `eval()` kita boleh kita peratusan markah yang diperoleh. Misalnya markah tersebut ialah 50/100, maka eval("50/100") akan menghasilkan markah 0.2. Dengan ini, kita boleh bandingkan nilai mana yang lebih tinggi berbanding nilai-nilai yang lain. Hasil pengiraan ini boleh disimpan dalam satu dictionary yang mana nilai tersebut sebagai key dan nama subjek sebagai value dictioanry tersebut. Menggunakan fungsi `max()` berdasarkan nilai ini membolehkan kita mencari subjek tertinggi yang diingini.
