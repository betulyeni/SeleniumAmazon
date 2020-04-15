import browser
link = input("Lütfen ürün linkini giriniz")
count = int(input("Kaçkez fiyat kontrol edilecek"))
time = int(input("Her kontrol arasında kaç saniye beklenecek"))
browser = browser.Browser(link=link, time=time, count=count)
