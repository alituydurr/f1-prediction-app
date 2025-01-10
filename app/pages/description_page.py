import os
import streamlit as st
import pandas as pd

# Sayfa başlığı
st.title("Formula 1 Tahmin Uygulaması")
st.header("Veri Seti ve Metadata")

# Veri setinin dinamik yolunu belirleme
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Bu dosyanın bulunduğu dizin
data_path = os.path.join(BASE_DIR, "..", "..", "notebooks", "data.csv")  # Veri setinin göreceli yolu

try:
    # Veri setini yükleme
    data = pd.read_csv(data_path)
    st.write(f"Toplam Satır: {data.shape[0]}")
    st.write(f"Toplam Sütun: {data.shape[1]}")

    # Veri setinden örnek gösterim
    st.write("### İlk 5 Satır")
    st.dataframe(data.head())

    # Metadata açıklamaları tablo formatında
    st.write("### Sütun Açıklamaları")
    metadata_table = """| Sütun Adı         | Açıklama                                                                  |
|-------------------|---------------------------------------------------------------------------|
| `raceId`          | Her bir yarış için benzersiz bir kimlik numarası.                         |
| `year`            | Yarışın gerçekleştiği yıl.                                               |
| `round`           | Sezon içindeki yarışın tur numarası.                                     |
| `circuitId`       | Yarışın yapıldığı pistin benzersiz kimlik numarası.                      |
| `driverId`        | Yarışa katılan sürücünün benzersiz kimlik numarası.                      |
| `constructorId`   | Sürücünün takımı (konstrüktör) için benzersiz kimlik numarası.           |
| `pit_stop_time`   | Sürücünün yarıştaki toplam pit stop süresi (milisaniye cinsinden).       |
| `positionOrder`   | Sürücünün yarıştaki bitiş sırasındaki pozisyonu.                         |
| `grid`            | Sürücünün yarışa başladığı grid pozisyonu.                               |
| `points`          | Sürücünün yarış performansı için aldığı puanlar.                         |
| `laps`            | Sürücünün yarışta tamamladığı toplam tur sayısı.                         |
| `statusId`        | Sürücünün yarış durumunu temsil eden benzersiz kimlik numarası (ör. bitirdi, yarış dışı kaldı). |"""

    st.markdown(metadata_table)

except FileNotFoundError:
    st.error(f"Veri seti bulunamadı. Lütfen '{data_path}' yolunu kontrol edin.")
except Exception as e:
    st.error(f"Bir hata oluştu: {e}")
