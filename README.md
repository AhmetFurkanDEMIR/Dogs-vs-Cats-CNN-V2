![licence](https://img.shields.io/badge/Keras-V2.3.1-red)
![licence](https://img.shields.io/badge/Tensorflow-V2.0-yellow)
![licence](https://img.shields.io/badge/Ahmet%20Furkan-DEM%C4%B0R-blue)
![licence](https://img.shields.io/badge/demir-ai-blueviolet)

# Dogs-vs-Cats-CNN-V2 

* Bu sürümde Veri seti çeşitlendirme, iletim sönümü ekleme ve Öneğitimli Evrişimli Sinir Ağı kullanarak modelimizin başarısını arttırıp kaybını düşültük.
* iki adet model mevcuttur sırasıyla inceleyelim.

# dogs-vs-cats-CNN

* dogs-vs-cats-CNN adlı klasörde kendi oluşturduğumuz Evrişimli Sinir Ağı modelimizi kullandık
* Keras 'ta bulunan modül ile Veri setinde çeşitlendirmeler yaparak elimizdeki veri sayısını arttırdık
(keras.preprocessing.image.ImageDataGenerator())

![Screenshot_2020-03-25_14-31-26](https://user-images.githubusercontent.com/54184905/77532193-6f0cf200-6ea5-11ea-982d-6b11dfc01c6a.png)

    Daha fazla bilgi için Keras documentation = https://keras.io/preprocessing/image/

* Evrişimli Sinir Ağımıza iletim sönümü ekledik. Bu sayede aşırı uydurmanın önüne geçtik.
(keras.models.model.add(layers.Dropout(0.5)))

![Screenshot_2020-03-24_23-22-50](https://user-images.githubusercontent.com/54184905/77530444-67981980-6ea2-11ea-8a8f-03ee1c470e04.png)

* Resimde de gördüğünüz gibi eğitim ve doğrulama başarımı ilk örnekten daha iyi sonuçlar verdi, eğitim ve doğrulama kaybı ise ilk örnekten daha düşük kayıp grafiği sergiledi.

# dog_vs_cat-öneğitimli-CNN

* dogs-vs-cats-CNN adlı örnekteki herşeyi burdada yaptık
* Farklı olan ise sıfırdan model eğitmek yerine daha önce eğitilmiş model üzerinden eğitim yapıyoruz.
* Biz ImageNet (1.4 milyon etiketli resim ve 1000 farklı sınıf.) veri setini kullanarak eğitilmiş bir modeli (VGG16) kullanacağız.
* Modelden öznitelik çıkarımı: öznitelik çıkarımı, daha önce ağ tarafından öğrenilen gösterimler ile yeni örnekler için ilginç niteliklerin çıkarılmasıdır. Bu nitelikler en baştan eğitilen yeni sınıflandırıcıda kullanılır.
* Kullanacağımız model VGG16, bu model keras.aplications modülünü içe aktararak içerisinde bulunan resim sınıflandırma modellerini kullanabilirsiniz.
* Kullanabileceğiniz diğer öneğitimli modeller:
 
      1-) Xception
 
      2-) VGG16
 
      3-) VGG19
 
      4-) ResNet, ResNetV2, ResNeXt
 
      5-) InceptionV3
 
      6-) InceptionResNetV2

      7-) MobileNet
 
      8-) DenseNet
 
      9-) NASNet
      
      Daha fazla bilgi için Keras documentation = https://keras.io/applications/
 
* VGG16 dondurulmuş evrişim tabanı oluşturmak:

![Screenshot_2020-03-25_14-35-29](https://user-images.githubusercontent.com/54184905/77532468-f65a6580-6ea5-11ea-939e-5409a73193af.png)

    * Dondurulmuş dememizin sebebi VGG16 evrişimli tabanı 14714688 adet parametreye sahiptir. bu da çok fazla 
    işlem kapasitesi demektir.
    
    * Dondurma sebebimiz Dense katmanları rastgele başlatıldığından eğitim esnasnında çok büyük güncellemeler 
    alacaktır ve buda daha önce öğrenilen gösterimleri yok edecektir.
    
    * Bu haliyle sadece eklediğimiz iki Dense katmanının ağırlıkları öğrenebilecek. 
    buda toplam dört ağırlık tensörü eder. katman başına ikitane (ağırlık, önyargı vektörü)

* Kullandığımız VGG16 model ile eğitim ve doğrulama sonuçları 

![ön_cnn](https://user-images.githubusercontent.com/54184905/77533457-f22f4780-6ea7-11ea-9186-50593a836407.png)

    Resimde de gördüğünüz gibi çıkan sonuçlar şimdiki yaptığımız örneklerden daha iyi. 

# Ara çıktılar

* ilk katmanın dördüncü kanalının kedi resmi için aktivasyonu.

![Screenshot_2020-03-25_14-00-57](https://user-images.githubusercontent.com/54184905/77536542-8c45be80-6ead-11ea-8dda-5943db2912f9.png)

* ilk katmanın yedinci kanalının kedi resmi için aktivasyonu.

![Screenshot_2020-03-25_14-00-50](https://user-images.githubusercontent.com/54184905/77536544-8d76eb80-6ead-11ea-9bc7-febef9ba3e6c.png)

* Test resimleri için tüm katmanların tüm filitreleri

![Screenshot_2020-03-25_14-01-08](https://user-images.githubusercontent.com/54184905/77536823-0aa26080-6eae-11ea-93b7-25f6288817f5.png)


