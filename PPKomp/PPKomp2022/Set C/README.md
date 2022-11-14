# Isi Kandungan

- [1.0 Jujukan Nombor](#1.0-jujukan-nombor)

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
