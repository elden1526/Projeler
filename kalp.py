import math
from turtle import *

# --- 🛠️ AYARLAR KISMI (Burayı Düzenleyin) ---

# Kalbin içine yazılacak İSİM
ISIM = "FİLİZİM" # Burayı istediğiniz isimle/metinle değiştirin!

# İsim altına yazılacak ek MESAJ/Tarih
EK_MESAJ = "Senin bir yazılımcı sevgilin var." # İsteğe bağlı, boş bırakabilirsiniz: ""

# --- 💖 KALBİ ÇİZEN FONKSİYONLAR ---

# Kalbin x koordinatını hesaplayan parametrik fonksiyon
def heart_x(k):
    # Denklem: 15 * sin(k)^3
    return 15 * math.sin(k)**3

# Kalbin y koordinatını hesaplayan parametrik fonksiyon
def heart_y(k):
    # Denklem: 12*cos(k) - 5*cos(2*k) - 2*cos(3*k) - cos(4*k)
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

# --- 🎨 ÇİZİM VE ANİMASYON ---

# Pencere ve çizim ayarları
setup(width=600, height=600) # Pencere boyutunu ayarla
speed(0)        # Çizim hızını en yükseğe ayarlar (animasyon hızını artırır)
bgcolor('black') # Arka plan rengini siyah yapar
color('red')   # Kalp çizgi rengini pembe yapar
pensize(2)      # Kalem kalınlığını ayarlar
hideturtle()    # Kalemi gizler

# Kalbi çizen döngü (Animasyon kısmı)
# Not: heart_x ve heart_y değerlerini 20 ile çarparak boyutu büyütüyoruz.
# Parametre aralığını 0..~2π olarak kullanarak düzgün bir kalp çizimi yap
penup()
# Başlangıç noktasına git ve sonra çizime başla
k0 = 0.0
goto(heart_x(k0) * 20, heart_y(k0) * 20)
pendown()
steps = 628  # yaklaşık 2π * 100
for j in range(steps + 1):
    k = j / 100.0  # 0.00 .. ~6.28 (radyan cinsinden)
    goto(heart_x(k) * 20, heart_y(k) * 20)

# --- ✍️ İSİM VE MESAJI YAZMA ---

# Yazmak için kalemi kaldır
penup()

# 1. İSMİ yazma
color('white') 
# Konumu ayarla: Merkezi (0,0) ve yazının üst kısmını biraz yukarı kaydır (örneğin y=30)
goto(0, 30) 
isim_stili = ('Arial', 40, 'bold')
write(ISIM, align='center', font=isim_stili)

# 2. EK MESAJI/Tarihi yazma (Eğer varsa)
if EK_MESAJ:
    color('white') # Ek mesaj için farklı bir renk
    # Konumu ayarla: İsimden biraz daha aşağıya (örneğin y=-30)
    goto(0, -30) 
    mesaj_stili = ('Verdana', 20, 'normal')
    write(EK_MESAJ, align='center', font=mesaj_stili)

done() # Turtle penceresini açık tutar
