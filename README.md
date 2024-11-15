# Simulated Annealing ile Minimum Nokta Bulma

Bu proje, Simulated Annealing algoritmasını kullanarak bir fonksiyonun minimum noktasını bulmayı amaçlar. Kullanıcıdan bir hedef fonksiyon, alt ve üst sınırlar, başlangıç sıcaklığı ve iterasyon sayısı gibi parametreleri alır ve ardından verilen fonksiyon üzerinde minimum değeri arar.

## Kullanılan Algoritma

**Simulated Annealing** (Benzetilmiş Tavlama), optimizasyon problemlerinde kullanılan bir algoritmadır. Algoritmanın temel mantığı, yüksek sıcaklıkla başlayarak olası çözümler arasında rastgele gezintiler yapması ve sıcaklık azaldıkça bu gezintilerin daha dar bir alanda yoğunlaşmasıdır. Böylece, global minimum değere yaklaşma şansı artar.

## Projenin Kullanımı

1. **Hedef Fonksiyon Formülü Girin:** İlgili fonksiyonu Python'da matematiksel olarak yazın (örneğin, `7*(math.sin(2*x)+math.sin(x)+3/2*math.cos(0.8*x))`).
2. **Değerlerin Alt ve Üst Sınırlarını Girin:** Fonksiyonun analiz edileceği aralıkları belirleyin.
3. **Başlangıç Sıcaklığını Girin:** Algoritmanın başlangıçtaki sıcaklık değerini belirleyin (örneğin, 200).
4. **İterasyon Sayısını Girin:** Algoritmanın kaç adımda sonuçlanacağını belirleyin (örneğin, 500).

## Sonuçlar

### Hedef Fonksiyon Grafiği
Bu grafikte, hedef fonksiyon ve Simulated Annealing algoritmasının başlangıç noktası ve ulaşılan minimum noktası gösterilmektedir. Algoritma, başlangıç noktasından (yeşil) başlayarak minimum noktaya (kırmızı) doğru ilerlemektedir.

![Hedef Fonksiyon Grafiği](https://github.com/user-attachments/assets/c8e6d6ec-b549-4902-9df3-ba6ae3a746d8)

### Simulated Annealing Kullanıcı Arayüzü
Bu arayüz, kullanıcının fonksiyon parametrelerini girebileceği bir form sunar ve sonuçları iterasyonlar boyunca günceller. Minimum nokta ve minimum değer her iterasyon sonunda güncellenir.

![Simulated Annealing Arayüzü](https://github.com/user-attachments/assets/7ba48a39-dd6f-415f-97b6-b0add39c083c)

## Gereksinimler

- Python 3
- `matplotlib` kütüphanesi (Grafik çizimi için)
- `tkinter` kütüphanesi (Arayüz için)

## Kurulum

```bash
pip install matplotlib






