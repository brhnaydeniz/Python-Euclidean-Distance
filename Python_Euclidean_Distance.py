# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 09:30:14 2024

@author: Burhan
"""

import math

# Points isimli listede 2D uzaydaki noktaları temsil eden tuple tanımlanması
points = [(1, 2), (4, 6), (5, 8)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance():
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    distance = math.sqrt((x3-y3)**2 + (x2 - x1)**2 + (y2 - y1)**2)
    return distance

distances = [] #Mesafelerin tutulacağı diziyi tanımlıyoruz.
for i in range(len(points)): # 
    for j in range(i + 1, len(points)):
        # Hesaplama için yazdığımız fonksiyonu çağırıyoruz ve sonucu değişkene atıyoruz.
        dist = euclideanDistance()
        # Değişkenin almış olduğu değeri distances listesine dahil ediyoruz.
        distances.append(dist)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

print("Minimum mesafe:", min_distance)
