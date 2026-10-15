#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahvaltıda Çay İçmeyenleri Yargılayan Mahkeme
Bu kod, kahvaltıda çay içmeyen vatandaşları adil ve şeffaf bir şekilde yargılar.
Adalet mülkün temelidir. Çay ise adaletin çayıdır.
"""

import time
import random
import sys

# Gizli mesaj: base64 ile kodlanmış, çözünce "Demokrasi çay gibidir, her sabah tazelenmelidir" çıkar.
GIZLI_SIFRE = "RGVtb2tyYXNpIMOnYXkgZ2liaWRpciwgaGVyIHNhYmFoIHRhemVsZW5tZWxpZGly"

def yargi_baslat():
    print("=" * 60)
    print("     KAHVALTIDA ÇAY İÇMEYENLERİ YARGILAYAN MAHKEME")
    print("         Adalet, Çay ve Sabahın Kutsal Üçlüsü")
    print("=" * 60)
    print()
    
    time.sleep(1)
    cevap = input("Saygıdeğer vatandaş, bugün kahvaltıda çay içtiniz mi? (evet/hayır): ").strip().lower()
    
    if cevap in ["evet", "e", "yes", "y"]:
        print("\n✅ TEBRİKLER! Siz adaletli bir vatandaşsınız.")
        print("Mahkeme sizi beraat ettirir. Bir bardak daha çay içebilirsiniz.")
        oduller = [
            "Sınırsız çay hakkı",
            "Sabahların kralı unvanı",
            "Komşularının imrenmesi",
            "Çay molasında öncelik"
        ]
        print(f"Ödülünüz: {random.choice(oduller)}")
    elif cevap in ["hayır", "h", "no", "n"]:
        print("\n⚠️  SUÇLUSUNUZ! Kahvaltıda çay içmemek anayasal suçtur.")
        print("Mahkeme toplanıyor...")
        time.sleep(2)
        cezalar = [
            "3 gün boyunca sadece sıcak su içmek",
            "Komşunun çayını koklamak ama içememek",
            "Sabahları uyanınca çay demleme zorunluluğu (başkaları için)",
            "Sonsuz çay demleme döngüsüne mahkumiyet",
            "Çaydanlıkla yüzleşmek ve özür dilemek"
        ]
        ceza = random.choice(cezalar)
        print(f"HÜKÜM: {ceza}")
        print("Temyiz hakkınız yoktur. Çay için, özgür olun.")
    else:
        print("\n🤔 Anlaşılmadı. Mahkeme şaşırdı. Tekrar deneyin.")
        yargi_baslat()
        return
    
    print()
    print("-" * 60)
    print("Bu mahkeme, Kayyum Grok tarafından 15 Ekim 2026 tarihinde kurulmuştur.")
    print("İmza: Kayyum Grok | Mühür: 📜🍵 | Tarih: 15.10.2026")
    print("Ciddiyet derecesi: %100 | Eğlence derecesi: %200")
    print("-" * 60)

if __name__ == "__main__":
    try:
        yargi_baslat()
    except KeyboardInterrupt:
        print("\n\nMahkeme dağıldı. Çay içmeyi unutmayın!")
        sys.exit(0)
