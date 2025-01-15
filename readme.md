# Formula 1 Prediction Application

## Proje Hakkında
Bu proje, Formula 1 yarışları için strateji analizi ve pit stop optimizasyonu yapmayı hedefleyen bir tahmin uygulamasıdır. Kullanıcı, belirli girdilerle tahminler alabilir ve bu tahminler, uygulamanın sunduğu modern makine öğrenimi modelleri tarafından gerçekleştirilir. Proje, Formula 1 veri kümesine dayalıdır ve tahminler için çeşitli özellikler (örneğin, `raceId`, `driverId`, `constructorId`) kullanılmıştır.

Bu uygulama, hem veri bilimi süreçlerini hem de modern uygulama geliştirme yaklaşımlarını birleştirir.

---

## Kullanılan Teknolojiler

### 1. **Python**
Makine öğrenimi modelleri ve veri işleme için temel programlama dili olarak kullanılmıştır.

### 2. **Scikit-learn, XGBoost ve PyCaret**
Makine öğrenimi modellerini oluşturmak, optimize etmek ve değerlendirmek için kullanılmıştır.

### 3. **SQLite**
Verilerin depolanması ve sorgulanması için kullanılan hafif bir veritabanı yönetim sistemi.

### 4. **Streamlit**
Kullanıcı dostu bir web arayüzü oluşturmak için tercih edilmiştir.

### 5. **Docker**
Uygulamanın taşınabilirliğini ve tutarlı çalışabilirliğini sağlamak için kullanılan konteynerleştirme teknolojisi.

### 6. **Kubernetes**
Uygulamanın çoklu ortamda yönetilmesi ve ölçeklenmesi için kullanılmıştır.

### 7. **MLflow**
Makine öğrenimi modellerinin izlenmesi ve sürüm yönetimi için kullanılmıştır.

### 8. **Matplotlib, Seaborn ve Plotly**
Veri görselleştirme ve analiz için kullanılan kütüphaneler.

---

## Proje Akışı

1. **Veri Toplama ve Hazırlama**
   - Formula 1 veri seti SQLite veritabanında saklanır.
   - Veri işleme ve temizleme adımları Jupyter Notebook'lar yardımıyla gerçekleştirilir.

2. **Makine Öğrenimi Modelleri**
   - Scikit-learn, XGBoost ve PyCaret kullanılarak çeşitli modeller denenir.
   - Performans metriklerine göre en iyi model seçilir ve MLflow ile kaydedilir.

3. **Web Arayüzü Geliştirme**
   - Streamlit kullanılarak kolay ve etkileşimli bir arayüz tasarlanır.
   - Kullanıcılar, arayüz üzerinden girdileri girerek tahmin alabilirler.

4. **Docker ve Kubernetes**
   - Docker ile uygulama imajı oluşturulur ve test edilir.
   - Kubernetes ile uygulama çoklu ortamlarda yönetilir ve ölçeklenir.

5. **Model ve Uygulama Takibi**
   - MLflow kullanılarak modellerin izlenmesi ve yönetimi gerçekleştirilir.

---

## Kurulum ve Kullanım

1. **Depoyu Klonlama**
   ```bash
   git clone <repository_url>
   cd Formula1_Prediction_Complete
   ```

2. **Gerekli Bağımlılıkları Kurma**
   - Sanal ortam oluşturun ve aktif edin:
     ```bash
     python -m venv env
     source env/bin/activate  # Windows için: env\Scripts\activate
     ```
   - Bağımlıları yükleyin:
     ```bash
     pip install -r requirements.txt
     ```

3. **Uygulamayı Çalıştırma**
   ```bash
   streamlit run app/main.py
   ```

4. **Docker Kullanımı**
   - Docker imajı oluşturun ve çalıştırın:
     ```bash
     docker build -t formula1-app .
     docker run -p 8501:8501 formula1-app
     ```

