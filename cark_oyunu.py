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

def apply_macos_identity():
    """macOS Dock'ta 'python' ve varsayılan simge yerine uygulama adı/simgesi.

    `python cark_oyunu.py` ile açıldığında Dock, Python yorumlayıcısının
    kimliğini gösterir. pywebview macOS'ta Cocoa kullandığı için çalışma anında
    paylaşılan NSApplication üzerinden simgeyi ve adı ayarlarız.
    """
    if sys.platform != 'darwin':
        return
    icon_path = resource_path("icon.png")
    try:
        from AppKit import NSApplication, NSImage
        img = NSImage.alloc().initWithContentsOfFile_(icon_path)
        if img is not None:
            NSApplication.sharedApplication().setApplicationIconImage_(img)
    except Exception:
        pass
    try:
        from Foundation import NSBundle
        info = NSBundle.mainBundle().localizedInfoDictionary() or NSBundle.mainBundle().infoDictionary()
        if info is not None:
            info['CFBundleName'] = 'Çark Oyunu'
            info['CFBundleDisplayName'] = 'Çark Oyunu'
    except Exception:
        pass

def main():
    # web/index.html dosyasının tam yolunu al
    html_path = 'file://' + resource_path(os.path.join("web", "index.html"))
    
    # Modern borderless/resizable Webview penceresi oluştur
    window = webview.create_window(
        title="LGS Sosyal Bilgiler – Çark Oyunu",
        url=html_path,
        width=1240,
        height=950,
        min_size=(900, 680),
        resizable=True
    )
    
    # WebView motorunu başlat.
    #  - Windows: Edge Chromium (WebView2)
    #  - macOS: yerleşik Cocoa/WKWebView (cef macOS'ta kurulu olmadığı için
    #    daha güvenilir ve daha keskin, native bir pencere sağlar)
    #  - Linux vb.: pywebview otomatik seçer (gtk/qt)
    if os.name == 'nt':
        gui = 'edgechromium'
    elif sys.platform == 'darwin':
        gui = None
    else:
        gui = 'cef'
    # Dock simgesi/adı: başlamadan önce ve başladıktan sonra uygula.
    apply_macos_identity()
    webview.start(apply_macos_identity, gui=gui)

if __name__ == "__main__":
    main()
