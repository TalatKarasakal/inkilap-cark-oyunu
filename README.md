# inkilap-cark-oyunu 🏛️

Bu proje Talat Karasakal ve Mehmet Ata Erçetin tarafından ortak geliştirilmiştir. / Co-developed by Talat Karasakal and Mehmet Ata Erçetin.

## 🇹🇷 Türkçe Bölüm

### Proje Hakkında
**inkilap-cark-oyunu**, LGS (Liselere Geçiş Sistemi) hazırlık sürecindeki öğrenciler için T.C. İnkılap Tarihi ve Atatürkçülük ile Sosyal Bilgiler derslerini eğlenceli ve interaktif hale getiren bir masaüstü bilgi yarışması uygulamasıdır. Klasik bilgi yarışması formatını, heyecan verici bir "çarkıfelek" mekaniği ve premium bir kullanıcı arayüzü ile birleştirerek öğrenci motivasyonunu artırmayı hedefler.

### Öne Çıkan Özellikler 🚀
*   **Geniş Müfredat Desteği:** 5, 6, 7 ve 8. sınıf düzeylerini kapsayan, her sınıf için özel olarak hazırlanmış soru bankaları.
*   **İnteraktif Çark Mekaniği:** Puan kazanma, "İflas", "Pas" ve "X2" gibi oyun içi dinamiklerle zenginleştirilmiş çark deneyimi.
*   **Dinamik Tema Sistemi:** "Enerji", "Karanlık" ve "Aydınlık" opsiyonlarıyla kişiselleştirilebilen modern ve premium arayüz.
*   **Gelişmiş İstatistik Paneli:** Çözülen soru sayısı, doğru/yanlış oranları ve ünite bazlı başarı takibi.
*   **Zamanlı Yarışma Deneyimi:** Her soru için 45 saniyelik geri sayım süresi ile sınav kondisyonu desteği.
*   **Akıcı Animasyonlar ve Ses Efektleri:** Fizik tabanlı çark dönüşü ve oyun akışını destekleyen profesyonel sesler.

### Kullanılan Teknolojiler ve Kütüphaneler 🛠️
*   **Python 3.x:** Uygulamanın temel programlama dili.
*   **Tkinter:** Modern ve performanslı GUI (Grafik Kullanıcı Arayüzü) tasarımı için kullanıldı.
*   **Pygame (Mixer):** Yüksek kaliteli ses efektlerini yönetmek amacıyla entegre edildi.
*   **JSON:** Soru bankasının ve kullanıcı istatistiklerinin esnek bir şekilde saklanması için tercih edildi.
*   **Ctypes:** Yüksek çözünürlüklü (DPI-aware) ekran desteği sağlamak için kullanıldı.

### Kurulum ve Çalıştırma Talimatları 🖥️
Proje iki istemci içerir: `cark_oyunu.py` dosyasıyla çalışan Python/pygame masaüstü istemcisi ve `web/` klasöründeki web istemcisi. Her iki istemci de ortak soru bankası olarak `sorular.json` dosyasını kullanır.

1.  **Depoyu Klonlayın:**
    ```bash
    git clone https://github.com/TalatKarasakal/inkilap-cark-oyunu.git
    cd inkilap-cark-oyunu
    ```
2.  **Bağımlılıkları Yükleyin:**
    *(Not: Uygulama temel kütüphaneleri kullanır, ancak ses desteği için `pygame` gereklidir.)*
    ```bash
    pip install pygame
    ```
3.  **Uygulamayı Çalıştırın:**
    ```bash
    python cark_oyunu.py
    ```

---

## 🇺🇸 English Section

### About the Project
**inkilap-cark-oyunu** is a desktop quiz application designed to make Social Studies and History of Revolution courses engaging and interactive for students preparing for the LGS (Entrance Exam for High Schools) in Turkey. It aims to boost student motivation by combining traditional quiz formats with an exciting "Wheel of Fortune" mechanic and a premium user interface.

### Key Features 🚀
*   **Comprehensive Curriculum Support:** Dedicated question banks for 5th, 6th, 7th, and 8th-grade levels.
*   **Interactive Wheel Mechanics:** A wheel experience enriched with "Bankrupt," "Pass," and "X2" dynamics.
*   **Dynamic Theme System:** Personalized experience with "Energy," "Dark," and "Light" UI modes.
*   **Advanced Statistics Panel:** Track solved questions, correct/incorrect ratios, and unit-based achievements.
*   **Timed Challenges:** Support for exam conditioning with a 45-second countdown for each question.
*   **Smooth Animations & Sound Effects:** Physics-based wheel rotations and professional audio feedback.

### Technologies and Libraries Used 🛠️
*   **Python 3.x:** Core programming language.
*   **Tkinter:** Used for designing a modern and performant GUI.
*   **Pygame (Mixer):** Integrated for managing high-quality sound effects.
*   **JSON:** Preferred for flexible storage of question banks and statistics.
*   **Ctypes:** Utilized to provide high-resolution (DPI-aware) display support.

### Installation and Running Instructions 🖥️
The project includes two clients: the Python/pygame desktop client run from `cark_oyunu.py` and the web client in the `web/` directory. Both clients use `sorular.json` as the shared question bank.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/TalatKarasakal/inkilap-cark-oyunu.git
    cd inkilap-cark-oyunu
    ```
2.  **Install Dependencies:**
    *(Note: The app uses core libraries, but `pygame` is required for audio support.)*
    ```bash
    pip install pygame
    ```
3.  **Run the Application:**
    ```bash
    python cark_oyunu.py
    ```
