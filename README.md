# Project-Func-clean-data-python
This project about using functions to clean data in python (In Indonesia)

Terkadang ketika kita melakukan proses cleaning data membutuhkan banyak langkah. Misalnya, kita ingin mengekstrak digit dari string dan mengkonversinya menjadi angka. Kita dapat menggunakan sebuah fungsi di Python.
Ini merupakan contoh dataset, kita dapat menggunakan fungsi mean untuk kasus ini.
Fungsi mean akan mendapatkan nilai average (rata-rata) untuk masing - masing treatment (a & b). Total nilai treatment a yaitu 54 dibagi 3 maka 18. Total treatment b yaitu 100 dibagi 3 maka 33.33
Subset dari dataset pengajuan aplikasi pekerjaan (job application). Misalnya:
- Kita ingin mengecek initial cost dan total estimasi biaya untuk memastikan bahwa penulisan nilai mata uang tersebut valid.
- Kemudian kita ingin menghapus simbol dollar dan mengkonversi string menjadi tipe data float.
- Lalu menemukan perbedaan antara 2 nilai dan menyimpannya ke sebuah kolom baru
- Jika kolom tidak mengandung nilai mata uang yang valid, maka kita berikan nilai NaN missing value.
Mari kita mulai dengan library regular expression dan NaN missing value: 
- import re
- from numpy import NaN
- pattern = re.compile('^\$\d*\.\d{2}$')

Kita gunakan fungsi compile regular expression untuk mengecek pattern nilai mata uang. Langkah selanjutnya adalah membuat function:
Fungsi pertama yang kita buat yaitu my_function untuk me-return statement dan menampilkan nilai. Selanjutnya di fungsi yang kedua yaitu diff_money akan melakukan proses pengecekan validasi untuk nilai mata uang.
Kita akan mendapatkan nilai initial cost dan total est biaya dengan cara slicing tiap baris dan memastikan jika statement tersebut valid.  Lalu mengkonversi hasilnya ke dalam True/False boolean.
Setelah kita memiliki nilai mata uang yang valid, selanjutnya adalah menghapus simbol dollar dengan me-replace menjadi string kosong. Hingga akhirnya kita memiliki nilai angka float dan menemukan perbedaan antara Initial Cost dan Total Est Fee.
Jika tidak dapat mencocokan pattern tersebut maka akan menghasilkan NaN missing value.
Setelah membuat fungsi, maka kita dapat menerapkan method apply untuk dataframe tersebut. Kita gunakan fungsi diff_money, parameter axis = 1 dan pattern = pattern sebagai regular expression.
Maka sekarang dengan perintah head kita akan mendapatkan 5 baris awal dari dataframe tersebut serta kolom diff untuk menghitung perbedaan nilai Initial Cost dan Total Est. Fee
