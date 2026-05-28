# Makine Öğrenmesi için Lineer Cebir

Bu depo, lineer cebiri makine öğrenmesi gözüyle sıfırdan öğreten 6 haftalık bir derstir. Buradaki yaklaşım, konuları soyut teoremler yığını olarak değil, geometrik sezgiyle ve çalışan kodla birlikte ele almaktır. Her kavram önce ne anlama geldiğiyle tanıtılır, sonra elle inşa edilir; hazır çözücülere güvenmek yerine algoritmaların içinde ne olduğu açıkça gösterilir.

Dersi bir arada tutan fikir, lineer cebirin makine öğrenmesinin dili olduğudur. Bir veri kümesi neden bir vektör bulutudur, bir öznitelik neden bir koordinattır, bir matris neden uzayı hareket ettiren bir fonksiyondur, bu sorular tüm boyunca yeniden karşımıza çıkar. Soyut bir kavram her tanıtıldığında, onun gerçek bir modelde nasıl iş gördüğü gösterilir: en küçük kareler doğrusal regresyonun motorudur, özproblemler PageRank'in kalbidir, SVD ise PCA'dan görüntü sıkıştırmaya kadar her şeyin altında yatar.

Ders, her biri tek başına yeterli olan 12 Jupyter notebook'tan oluşur ve altı haftaya yayılır. Birinci haftada vektörler, normlar ve izdüşümlerle temel atılır. İkinci hafta matrisleri sayı ızgaraları olarak görmeyi bırakıp onları doğrusal dönüşümler olarak ele alır. Üçüncü hafta doğrusal sistemleri Gauss elemesi ve LU ayrışımıyla çözer ve en küçük karelere ulaşır. Dördüncü hafta ortogonallik ile Gram–Schmidt ve QR ayrışımını, sayısal kararlılık vurgusuyla işler. Beşinci hafta özdeğerler ve özvektörlerle lineer cebirin spektral kalbine iner; kuvvet yöntemi ve QR yinelemesi elle kodlanır. Altıncı hafta ise bir bitirme doruğu niteliğindedir: en önemli ayrışım olan SVD özayrışımdan kurulur ve doğrudan PCA, düşük ranklı yaklaşım ve gerçek bir makine öğrenmesi modeline bağlanır.

---

## Müfredat

### Hafta 1 — Vektörler, Uzaylar & Geometri
Geri kalan her şeyin üzerine inşa edildiği nesneler. Oklar ve veri noktaları olarak
vektörler, uzaklık kavramı olarak normlar, benzerlik olarak nokta çarpımı, izdüşümler
ve doğrusal (bağımsızlık/)bağımlılık. Bir veri kümesinin neden bir vektör bulutu, bir
özniteliğin neden bir koordinat olduğu.
- `01_vektorler_ve_vektor_uzaylari.ipynb`
- `02_normlar_nokta_carpimlari_izdusumler.ipynb`

### Hafta 2 — Doğrusal Dönüşümler Olarak Matrisler
Matrisleri sayı ızgaraları olarak görmeyi bırakın. Bir matris, uzayı hareket ettiren
bir fonksiyondur. Matris–vektör çarpımları, bileşke, dört temel altuzay, rank ve
determinant ile izin geometrik anlamı.
- `03_donusum_olarak_matrisler.ipynb`
- `04_rank_temel_alt_uzaylar.ipynb`

### Hafta 3 — Doğrusal Sistemleri Çözmek
Elle uygulanan Gauss eleme ve LU ayrışımı. Koşullanma ve naif çözümlerin neden
patladığı. Normal denklemler ve en küçük kareler — doğrusal regresyonun arkasındaki
motor.
- `05_gauss_eleme_lu.ipynb`
- `06_en_kucuk_kareler_normal_denklemler.ipynb`

### Hafta 4 — Ortogonallik & QR
Ortonormal tabanlar, sıfırdan kurulan Gram–Schmidt süreci, QR ayrışımı ve ortogonal
izdüşümler. Ortogonalliğin her şeyi neden sayısal olarak kararlı kıldığı ve QR'nin
kararlı en küçük kareleri nasıl güçlendirdiği.
- `07_ortogonallik_gram_schmidt.ipynb`
- `08_qr_ayrisimi.ipynb`

### Hafta 5 — Özdeğerler & Özvektörler
Lineer cebirin spektral kalbi. Özayrışım, elle kodlanan kuvvet yöntemi ve QR
yinelemesi, köşegenleştirme ve simetrik matrisler için spektral teori. Özproblem
olarak PageRank ve Markov zincirleri.
- `09_ozdegerler_ozvektorler.ipynb`
- `10_kuvvet_yontemi_qr_iterasyonu.ipynb`

### Hafta 6 — SVD & Makine Öğrenmesindeki Uygulamaları
Makine öğrenmesindeki tek en önemli ayrışım. SVD'yi özayrışımdan kurun, ardından onu
konuşlandırın: ilk ilkelerden PCA, düşük ranklı yaklaşım ve görüntü sıkıştırma, SVD
merceğinden ridge regresyonu ve boyut indirgemeyi gerçek bir modele bağlayan kapanış
doruk projesi.
- `11_tekil_deger_ayrisimi.ipynb`
- `12_pca_dusuk_rank_doruk_projesi.ipynb`

---

## Depo yapısı

```
makine_ogrenmesi_icin_lineer_cebir/
├── README.md
├── requirements.txt
├── notebooks/          # 12 ders not defteri
├── utils/              # paylaşılan çizim & yardımcı fonksiyonlar
│   └── linalg_viz.py
├── data/               # uygulamalı bölümlerde kullanılan küçük veri kümeleri
└── assets/             # dışa aktarılan şekiller
```

## Başlarken

```bash
git clone https://github.com/HAYDARKILIC/makine_ogrenmesi_icin_lineer_cebir.git
cd makine_ogrenmesi_icin_lineer_cebir
pip install -r requirements.txt
jupyter lab
```

`notebooks/01_vektorler_ve_vektor_uzaylari.ipynb` dosyasını açın ve baştan sona çalışın.
Her not defteri tek başına çalışır.

---

## Lisans

MIT — öğretim ve kişisel çalışma için serbestçe kullanılabilir.
