# Tugas 1 magang tim ichiro
Implementasi OOP dalam permainan blackjack

## Identitas 
Nama : Muhammad Zufarrifqi Prakoso<br/>
NRP : 5205201276 <br/>
Departemen : Teknik Informatika <br/>

<br/>

## implementasi blackjack
### Latar Belakang
Blackjack adalah sebuah permainan kartu yang dimana terbagi menjadi 2 pemain yaitu ada dealer dan player. dealer akan membagikan 2 kartu terbuka pada player dan mebagikan 2  kartu untuk dirinya sendiri 1 kartu terbuka dan 1 kartu tertutup atau tersembunyi. tujuan dari permainan ini adalah berupaya mendapatkan angka 21 dari kartu yang dimana kartu bernilai 1 - 10 sesuai dengan angkanya, J - K bernilai 10 dan Ace bernilai 1 ataupun 11. Jika kita mendapatkan jumlah dari kartu 21 pada awal dibagikan maka kita akan mendapatkan blackjack dan memenangkan permainan. aturannya tersebut juga berlaku pada dealer dan kita akan langsung kalah dalam permainan.  jika player dan dealer tidak mendalpatkan blackjack maka kita terus berupaya mendekati jumlah 21 dengan terus menambah kartu atau disebut dengan hit Jika jumlahnya ≥22, maka pemain tersebut akan langsung kalah dalam pertandingan. Dealer harus hit (tambah kartu) bila jumlah semua kartu ≤16. Dealer harus stand (tidak tambah kartu) bila jumlah semua kartu bernilai ≥17. 

### Class

#### Decks
Di kelas decks  adalah kelas untuk pengoperasian kartu dimana terdapat fungsi `__init__` sebagai inisialisasi. lalu ada fungsi `shuffle` dimana shuffle ini untuk mengacak kartu dengan menggunakan fungsi `random()` lalu ada fungsi `drawcard` untuk mengambil kartu yang sudah di shuffle.

#### game_init
Di kelas ini akan dilaksankan awal permainan yang dimana di kelas ini terdapat 3 fungsi di fungsi `__init__` ini ada
lah sebagai inisialisasi dan juga terdapat list kosong untuk kartu yang dibagikan kepada player dan dealer lalu di fungsi `initial_game` adalah untuk pembagian kartu pada player dan dealer yang dimana akan mengambil 2 kartu yang sudah diacak. lalu ada fungsi `total_score` untuk menghitung score dari masing masing kartu jika karu tersebut merupakan jack queen king maka skornya adalah 10 dan jika kartunya adalah ace maka akan ditambah 1 jika value yang sekarang lebih dari 11 dan ditambah 11 jika value kurang dari 11

#### game_result
di class result ini adalah kelas untuk dilakukannya permainan dan sekaligus menunjukkan hasil akhir dari permainan di class ini terdapat 5 fungsi yaitu adala `__init__` sebagai inisialisasi, lalu ada `blackjack_result`, di fungsi ini akan dicek apakah salah satu dari dealer ataupun player ada yang mendapatkan blackjack atau tidak. lalu ada fungsi hit_or_stand untuk mengetahui dari input player apakah player tersebut memilih stand atau hit jika memilih hit maka player tersebut akan mengambil dari kartu dari draw dan jika jumlah kartu yang dimiliki player ini mempunyai nilai lebih dari 21 maka player tersebut akan kalah, jika player memilih stand maka player tersebut tidak akan mangambil kartu dan nilai kartunya akan tetap. lalu yang keempat adalah fungsi 'dealers_hit' setelah player mangambil keputusan hit atau stand kemudian adalah dealer yang jalan. Dari peraturan blackjack diatas kita mengetahui bahwa dealer harus hit jika jumlah semua kartu ≤16 dan stand bila jumlah semua kartu bernilai ≥17. lalu yang terakhir adalah fungsi `compare_card` yang dimana fungsi ini adalah untuk menentukan siapa yang menang dan siapa yang kalah jika kartu dealer lebih banyak daripada player maka dealer akan menang jika kartu player lebih banyak daripada dealer maka player akan menang dan jika kedua nilainya sama maka akan seri.
