# Otsu-Esikleme-Yontemi

  Otsu’nun ikili eşikleme yöntemi, görüntü eşikleme alanında yapılan ilk çalışmalardan biri olan ve Otsu (1979) tarafından önerilen eşikleme yöntemidir. Otsu yönteminde gri seviye görüntüler üzerinde çalışılmakta ve sadece renklerin görüntü üzerinde bulunma sıklığına bakılmaktadır. Eşikleme için, görüntüdeki gri seviye dağılımlarını gösteren görüntü histogramından faydalanılır ve tüm işlemler histogram dizisi üzerinden yapılır. Bu metot kullanılırken görüntünün arka plan ve ön plan olmak üzere iki renk sınıfından oluştuğu varsayımı yapılır. Daha sonra tüm eşik değerleri için bu iki renk sınıfının sınıf içi varyans değeri hesaplanır. Bu değerin en küçük olmasını sağlayan eşik değeri optimum eşik değeridir.    

  Sınıf içi varyans değeri minimum değerinde iken sınıflar arası varyans değer maksimum değerinde olur. Sınıflar arası varyans değerinin hesaplanması daha az işlem gerektirdiğinden kodlama aşamasında sınıflar arası varyans değeri hesaplanmaktadır. 
 
 

![kizkulesi-horz](https://user-images.githubusercontent.com/37310263/53898939-29874800-404a-11e9-8467-5d2efec3a746.jpg)
