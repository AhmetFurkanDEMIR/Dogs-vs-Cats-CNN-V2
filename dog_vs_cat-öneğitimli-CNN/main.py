from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications import VGG16
import matplotlib.pyplot as plt
from keras import optimizers
from time import sleep as sl
from keras import layers
from keras import models
import os, shutil
import numpy as np


# ----------- veri ön işleme (veri klasör yollarını kodda tanımlama) -----------

original_dataset_dir = os.path.join("traina")

train_dir = os.path.join("train") # eğitim seti

validation_dir = os.path.join("validation") # doğrulama seti

test_dir = os.path.join("test") # test seti

train_cats_dir = os.path.join(train_dir,"cats") # kedi eğitim setinin dizini.

train_dogs_dir = os.path.join(train_dir,"dogs") # köpek eğitim seti

validation_cats_dir = os.path.join(validation_dir,"cats") # kedi doğrulama setinin dizini.

validation_dogs_dir = os.path.join(validation_dir,"dogs") # köpek doğrulama seti

test_cats_dir = os.path.join(test_dir,"cats") # kedi test setinin dizini.

test_dogs_dir = os.path.join(test_dir,"dogs") # köpek test seti

# --- öneğitimli CNN ---

conv_base = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(150, 150, 3))

# --- CNN 'i modele dahil etmek ve bağzı katmanları dondurmak ---

model = models.Sequential()

model.add(conv_base)

model.add(layers.Flatten())

model.add(layers.Dense(256, activation="relu"))

model.add(layers.Dense(1,activation="sigmoid"))

conv_base.trainable = False # katman dondurma işlemi

# --- veri seti çeşitlendirme , hazır hale getirme. --- 

train_datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=40,
      width_shift_range=0.2,
      height_shift_range=0.2,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')

# Note that the validation data should not be augmented!
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        # This is the target directory
        train_dir,
        # All images will be resized to 150x150
        target_size=(150, 150),
        batch_size=20,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(150, 150),
        batch_size=20,
        class_mode='binary')

model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=2e-5),
              metrics=['acc'])

# --- eğitim ---

history = model.fit_generator(
      train_generator,
      steps_per_epoch=100,
      epochs=30,
      validation_data=validation_generator,
      validation_steps=50,
      verbose=2)

model.save('cats_and_dogs_small_3.h5')

# ----------- sonucları görselleştirme (modelin verimi) -----------

acc = history.history["acc"]

val_acc = history.history["val_acc"]

loss = history.history["loss"]

val_loss = history.history["val_loss"]

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, "bo", label="Eğitim başarımı")

plt.plot(epochs, val_acc, "b", label="Doğrulama başarımı")

plt.title("Eğitim ve doğrulama başarımı")

plt.legend()

plt.figure()

plt.plot(epochs, loss, "bo", label="Eğitim kaybı")

plt.plot(epochs, val_loss, "b", label="Doğrulama kaybı")

plt.title("Eğitim ve doğrulama kaybı")

plt.legend()

plt.show()