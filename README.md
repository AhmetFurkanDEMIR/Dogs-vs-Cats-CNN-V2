# Dogs-vs-Cats-CNN-V2 

* Bu sürümde Veri seti çeşitlendirme, iletim sönümü ekleme ve Öneğitimli Evrişimli Sinir Ağı kullanarak modelimizin başarısını arttırıp kaybını düşültük.
* iki adet model mevcuttur sırasıyla inceleyelim.

# dogs-vs-cats-CNN

* dogs-vs-cats-CNN adlı klasörde kendi oluşturduğumuz Evrişimli Sinir Ağı modelimizi kullandık
* 1. sürümden farklı olarak Keras 'ta bulunan modül ile Veri seti çeşitlendirme yaparak elimizdeki veri sayısını arttırdık:

      train_datagen = ImageDataGenerator(
      
           rescale=1./255,
           
           rotation_range=40,
           
           width_shift_range=0.2,
           
           height_shift_range=0.2,
           
           shear_range=0.2,
           
           zoom_range=0.2,
           
           horizontal_flip=True,
           
           fill_mode='nearest')

* Evrişimli Sinir Ağımıza iletim sönümü ekledik. Bu sayede aşırı uydurmanın önüne geçtik.

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
 
* VGG16 evrişim tabanı oluşturmak:




