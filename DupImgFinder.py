from difPy import dif

sourceFolder = input("please enter the source folder directory: ")

acceptedAnswers = ["y", "yes", "Y", "Yes", "YES", "n", "no", "N", "No", "NO"]

keepPhotos = input("do you want to keep the duplicates? Y/N: ")

while keepPhotos not in acceptedAnswers:
    print ("You entered something not valid. Please try again")
    keepPhotos = input("do you want to keep the duplicates? Y/N: ")

acceptedAnswersY = ["y", "yes", "Y", "Yes", "YES"]
acceptedAnswersN = ["n", "no", "N", "No", "NO"]

if keepPhotos in acceptedAnswersY:
    destinationFolder = input("please enter the destination folder directory: ")
    search = dif(sourceFolder, move_to=(destinationFolder))

elif keepPhotos in acceptedAnswersN:
    search = dif(sourceFolder,show_output=True, delete=True)

#difPy kütüphanesini inceleyip bulduğum bu kod, ilk kısma yazılı dosyadaki resimler içerisinden birbiriyle aynı olan
#ya da benzeyen resimleri alıp ikinci kısma yazılmış dosyaya atıyor. Ben bu kodu biraz daha user friendly yapmak için
# kopyaların tutulup tutulmayacağını sordum ve bunun üzerine çalıştırılacak kodu değiştirdim. Silinecek ise kopyaları
# gösteriyoruz ki yanlış dosya silinmesin.