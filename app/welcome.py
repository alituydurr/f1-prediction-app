import streamlit as st

# Uygulama genel açıklamaları için hoş geldiniz sayfası
def main():
    st.title("Formula 1 Tahmin Uygulamasına Hoş Geldiniz!")
    
    st.write("""
    ### Bu Uygulama Nedir?
    Formula 1 yarışlarının sonuçlarını tahmin etmek için tasarlanmış bir uygulamadır. 
    Yarış pistleri, sürücüler, takımlar ve diğer özelliklere dayanarak, bir sürücünün yarışı kazanıp kazanamayacağını öngörebilirsiniz.
    
    ### Bölümler:
    - **Açıklama**: Uygulamanın amacını ve kullanılan veri setini tanıyın.
    - **Tahmin**: Belirttiğiniz yarış detaylarına göre tahmin yapın.
    
    ### Nasıl Kullanılır?
    1. **Menüden bir sayfa seçin:** 
       Sol taraftaki menüyü kullanarak tahmin yapmak veya proje hakkında bilgi almak için farklı sayfalara geçiş yapabilirsiniz.
    2. **Tahmin yapmak için gerekli bilgileri doldurun:** 
       Pist, sürücü, takım gibi bilgileri seçerek tahmin sonuçlarını alın.

    ### Hedeflerimiz
    - Formula 1 fanları için keyifli ve veri odaklı bir deneyim sunmak.
    - Geçmiş verilere dayanarak tahmin yapmanın heyecanını yaşatmak.
    
    Keyifli tahminler!
    """)

if __name__ == "__main__":
    main()
