# Makine Öğrenmesi için Lineer Cebir

Modern makine öğrenmesinin temelindeki lineer cebiri **saf NumPy ile sıfırdan**
yeniden inşa eden, ardından her yapıyı ona bağımlı olan modele geri bağlayan altı
haftalık, ilk ilkelerden bir kurs. Algoritmayı kendiniz uygulayıp tam olarak neyi
ve neden döndürdüğünü anlayana kadar kara kutu `np.linalg` çağrıları yok.

Her ders kendi içinde eksiksiz bir Jupyter not defteridir: teorik türetme,
sıfırdan bir uygulama, geometrinin görselleştirmeleri, referans kütüphaneye karşı
bir doğrulama ve çözümlü alıştırmalar.

---

## Felsefe

Çoğu makine öğrenmesi uygulayıcısı lineer cebiri bir API gibi ele alır. Bu kurs
onu *görebileceğiniz* ve *inşa edebileceğiniz* bir dizi geometrik fikir olarak ele
alır. Ana eksen her zaman aynı döngüdür:

> **matematiği türet → NumPy'da uygula → geometriyi görselleştir → `scipy`/`numpy` ile doğrula → gerçek bir makine öğrenmesi problemine uygula.**

Sonunda elle yazmış olacaksınız: Gauss eleme, Gram–Schmidt, kuvvet yöntemi, QR
yinelemesi, tam bir SVD, PCA, normal denklemler aracılığıyla ridge regresyonu ve
yalnızca lineer cebirden oluşan bir sinir ağı katmanı — ve her birinin gizlice
hangi ayrışıma dayandığını tam olarak bileceksiniz.

---

## Ön koşullar

- Rahat Python ve temel NumPy (diziler, dilimleme, yayınlama/broadcasting)
- Lise cebiri; önceden lineer cebir bilgisi varsayılmıyor
- Yöntemlerin yalnızca nasıl çağrılacağına değil, *neden* işlediğine dair merak

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
linear_algebra_for_ml/
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
git clone https://github.com/HAYDARKILIC/linear_algebra_for_ml.git
cd linear_algebra_for_ml
pip install -r requirements.txt
jupyter lab
```

`notebooks/01_vektorler_ve_vektor_uzaylari.ipynb` dosyasını açın ve baştan sona çalışın.
Her not defteri tek başına çalışır.

---

## Bu kurs nasıl kullanılır

1. **Türetmeyi okuyun** — matematik gerekçelendirilmiştir, öylece bırakılmamıştır.
2. **Uygulamayı önce kendiniz yazın**, verilenini okumadan önce.
3. **Görselleştirmeleri çalıştırın** — döndürün, girdileri değiştirin, bozun.
4. **Alıştırmaları yapın** — çözümler her not defterinin altında katlanmıştır.
5. **İleriye bağlayın** — her not defteri "Bunun makine öğrenmesinde karşımıza çıktığı yer" ile biter.

---

## Lisans

MIT — öğretim ve kişisel çalışma için serbestçe kullanılabilir.
