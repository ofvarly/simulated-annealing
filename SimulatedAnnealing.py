import math
import random
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def hedef_fonksiyon(x, formula): #hedef fonksiyonu tanımlama
    try:
        return eval(formula, {"x": x, "math": math})  # kullanıcının girdiği formülü değerlendir
    except:
        return 0  # hata durumunda 0 döndür    
    #return  7*(math.sin(2*x)+math.sin(x)+3/2*math.cos(0.8*x)) #hedef fonksiyonu döndürme    |||||  #(-3*(x**2))+(5*x)-4   #((1/199)*(x**3))+(x**2)+(10*x)-4   


def simulated_annealing(hedef_fonksiyon, x0, T, alpha, iterasyon_sayisi, alt_sinir, ust_sinir, adim_sayisi, formula): #simulated annealing algoritması

    x = x0 # başlangıç noktası
    en_iyi_x = x # en iyi nokta
    en_iyi_deger = hedef_fonksiyon(x, formula) # en iyi noktaya karşılık gelen değer

    for i in range(iterasyon_sayisi):# iterasyon döngüsü
        yeni_x = x + random.uniform(0, ust_sinir - alt_sinir) * adim_sayisi * random.choice([1, -1]) # rastgele bir komşu nokta seçme

        yeni_x = max(alt_sinir, min(ust_sinir, yeni_x))  # değerin sınırlarını kontrol etme
        deger_farki = hedef_fonksiyon(yeni_x, formula) - hedef_fonksiyon(x, formula) # yeni ve eski değer farkı

        if (deger_farki < 0) or  (random.random() < math.exp(-deger_farki / T)): # minimum noktayı bulma formülü
            # eğer fark negatifse veya  0'la 1 arasında oluşan rastgele bir sayı, exp(-deger_farki / T)'den küçükse
            x = yeni_x # yeni noktayı güncelle
            if hedef_fonksiyon(x, formula) < en_iyi_deger: # eğer yeni değer en iyi değerden küçükse
                en_iyi_x = x # en iyi x'i güncelle
                en_iyi_deger = hedef_fonksiyon(x, formula) # en iyi değeri güncelle

        T *= alpha  # sıcaklığı alpha katsayısı ile çarparak azalt
        result_label.insert(tk.END, f"Iterasyon {i+1} Minimum nokta: {round(en_iyi_x,2)}, Minimum değer: {round(en_iyi_deger,2)}\n") # iterasyon sonuçlarını ekrana yazdır
        result_label.see(tk.END) # iterasyon sonuçlarını ekranda göster

        plt.axvline(x=x, color='b', linestyle='--',alpha=0.5,linewidth = 0.5) # iterasyon noktalarına dikey nokta çiz

    return en_iyi_x, en_iyi_deger # en iyi nokta ve en iyi değeri döndür




def run_simulated_annealing(): # simulated annealing algoritmasını çalıştırma
    
    formula = fonksiyon_formula_entry.get()  # formülü kullanıcı girdisinden al
    alt_sinir = float(alt_sinir_entry.get())  # değerin alt sınırı girdisi
    ust_sinir = float(ust_sinir_entry.get())  # değerin üst sınırı girdisi
    x0 = random.uniform(alt_sinir, ust_sinir)  # başlangıç noktasının rastgele belirlenmesi
    T = float(T_entry.get())  # başlangıç sıcaklığı girdisi
    alpha = 0.95 # alpha (sıcaklık azaltma) katsayısı
    iterasyon_sayisi = int(iterasyon_sayisi_entry.get()) # iterasyon sayısı girdisi
    adim_sayisi = 0.3 # adım büyüklüğü


    x_degerleri = np.linspace(alt_sinir, ust_sinir, 1000) # grafikteki x değerlerini oluştur
    y_degerleri = [hedef_fonksiyon(x, formula) for x in x_degerleri] # grafikteki her bir x değerinin y değerlerini oluştur
    
    plt.clf() # halihazırda grafik varsa temizle
    plt.plot(x_degerleri, y_degerleri, label="Hedef Fonksiyon") # hedef fonksiyonu çiz
    result_label.delete(1.0,tk.END) # 1. satırdan son satıra halihazırda olan sonuç kutusunu temizler


    minimum_nokta, minimum_deger = simulated_annealing(hedef_fonksiyon, x0, T, alpha, iterasyon_sayisi, alt_sinir, ust_sinir, adim_sayisi, formula)
    # simulated annealing algoritmasını çalıştır, minimum noktayı ve minimum değeri al

    # Grafik Çizdirme
    plt.scatter(x0, hedef_fonksiyon(x0, formula), color='green', label="Başlangıç Noktası") #başlangıç noktasını çiz
    plt.axvline(x=x0, color='g', label=f"x = {round(x0,2)}  y = {round(hedef_fonksiyon(x0, formula),2)}") # başlangıç çizgisini çiz
    
    plt.scatter(minimum_nokta, minimum_deger, color='red', label="Minimum Nokta") # minimum noktayı çiz
    plt.axvline(x=minimum_nokta, color='r', label=f"x = {round(minimum_nokta,2)}  y = {round(minimum_deger,2)}") # minimum çizgisini çiz

    plt.xlabel("X Değeri") # x ekseninin başlığı
    plt.ylabel("Hedef Fonksiyon Değeri") # y ekseninin başlığı
    plt.title("Simulated Annealing Sonuçları") # grafik başlığı
    plt.legend() # legendı ekle
    plt.show() # grafiği göster




# GUI
root = tk.Tk() # tkinter penceresi oluştur
root.title("Simulated Annealing") # pencere başlığı
root.geometry("1000x600") # pencere boyutları

fonksiyon_formula_label = tk.Label(root, text="Hedef Fonksiyon Formülünü Girin", font=('Arial', 15))
fonksiyon_formula_label.pack()
fonksiyon_formula_entry = tk.Entry(root, width=60, font=('Arial', 15))
fonksiyon_formula_entry.pack()
fonksiyon_formula_entry.insert(0, "7*(math.sin(2*x)+math.sin(x)+3/2*math.cos(0.8*x))")

alt_sinir_label = tk.Label(root, text="Değerin alt sınırını girin:", font=('Arial', 15)) # değerin alt sınır girdi metni
alt_sinir_label.pack() # alt sınır girdi kısmını ekrana yerleştir
alt_sinir_entry = tk.Entry(root, width=30, font=('Arial', 15)) # alt sınır girdi kısmı
alt_sinir_entry.pack() # alt sınır girdi kısmını ekrana yerleştir

ust_sinir_label = tk.Label(root, text="Değerin üst sınırını girin:",font=('Arial', 15)) # değerin üst sınır girdi metni
ust_sinir_label.pack() # üst sınır girdi kısmını ekrana yerleştir
ust_sinir_entry = tk.Entry(root, width=30, font=('Arial', 15)) # üst sınır girdi kısmı
ust_sinir_entry.pack() # üst sınır girdi kısmını ekrana yerleştir

T_label = tk.Label(root, text="Başlangıç sıcaklığını girin:", font=('Arial', 15)) # başlangıç sıcaklık girdi metni
T_label.pack() # başlangıç sıcaklık girdi kısmını ekrana yerleştir
T_entry = tk.Entry(root, width=30, font=('Arial', 15)) # başlangıç sıcaklık girdi kısmı
T_entry.pack() # başlangıç sıcaklık girdi kısmını ekrana yerleştir

iterasyon_sayisi_label = tk.Label(root, text="İterasyon sayısını girin:", font=('Arial', 15)) # iterasyon sayısı girdi metni
iterasyon_sayisi_label.pack() # iterasyon sayısı girdi kısmını ekrana yerleştir
iterasyon_sayisi_entry = tk.Entry(root, width=30, font=('Arial', 15)) # iterasyon sayısı girdi kısmı
iterasyon_sayisi_entry.pack() # iterasyon sayısı girdi kısmını ekrana yerleştir

# çalıştır butonu
run_button = tk.Button(root, text="Simulated Annealing Çalıştır",font=('Arial', 15), command=run_simulated_annealing)
run_button.pack() # çalıştır butonunu ekrana yerleştir

result_label = tk.Text(root,font=('Arial', 15)) # sonuç kutusu
result_label.pack() # sonuç kutusunu ekrana yerleştir

root.mainloop() # pencereyi çalıştır

