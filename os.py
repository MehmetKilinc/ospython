import os

print(dir(os))       #fonksiyonları göster

print(os.getcwd())    #klasör konum görüntüle

os.chdir("/root/Downloads")  #klasör konum değiştir

print(os.listdir())      #dosyaları görüntüle

os.mkdir("merhaba")     #klasör oluştur

os.makedirs("naber/naber2")   #alt alta klasör oluştur

os.rmdir("naber/naber2")     #klasör silme

os.removedirs("naber/naber2")  #klasörleri silme 

os.rename("test.txt" , "test2.txt")   #isim değiştirme

print(os.stat("test.txt"))     #dosya bilgiler

print(os.stat("test.txt").st_mtime)   #belirli bilgi çekme

print(datetime.fromtimestamp(os.stat("test.txt")).st_mtime)  #düzgün değiştirilme tarihi çekme

###########################

for i in os.walk("/root"):

	print(i)                   #root altındaki bütün dosyalar


###########################

for i,j,k in os.walk("/root"):

	print("""

		klasör yolu     : {}
		klasör isimleri : {}
		dosya isimleri  : {}



		""".format(i,j,k))       #dosyaları düzenli görme

############################

for i,j,k in os.walk("/root"):

	for i in k:

		if (i.endswith(".txt"):

			print(i)                 #root altındaki txt dosyalarını bulma