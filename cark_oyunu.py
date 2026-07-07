import os
import sys
import webview

def resource_path(relative_path):
    """PyInstaller ve normal geliştirme için kaynak yollarını çözer."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    # web/index.html dosyasının tam yolunu al
    html_path = resource_path(os.path.join("web", "index.html"))
    
    # Modern borderless/resizable Webview penceresi oluştur
    window = webview.create_window(
        title="LGS Sosyal Bilgiler – Çark Oyunu",
        url=html_path,
        width=1240,
        height=950,
        min_size=(900, 680),
        resizable=True
    )
    
    # WebView motorunu başlat (Windows'ta Edge Chromium WebView2 kullanılır)
    webview.start(gui='cef' if os.name != 'nt' else 'edgechromium')

if __name__ == "__main__":
    main()
