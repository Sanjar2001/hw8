import numpy as np
import pandas as pd
import os
from fastai.vision.all import *

# Убедитесь, что у вас есть файл digit-recognition.zip в текущем каталоге
# Распакуем архив
!unzip digit-recognition.zip -d ./content/

# Установим путь к данным
data_dir = "./content/digit-recognition/digits"
filepaths = [f"./content/digit-recognition/digits/{i}.jpg" for i in range(42000)]
labels = pd.read_csv("./content/digit-recognition/labels.csv")["label"]

# Создаем DataFrame для удобства
df = pd.DataFrame({
    'image': filepaths,
    'label': labels
})

# Создаем DataLoaders
dls = ImageDataLoaders.from_df(df, 
                               path='.', 
                               folder='content/digit-recognition/digits', 
                               valid_pct=0.2, 
                               seed=42, 
                               item_tfms=None, 
                               batch_tfms=None)

# Просмотрим часть данных
dls.show_batch()

# Создаем learner
learn = vision_learner(dls, resnet34, metrics=error_rate)

# Найдем оптимальный learning rate
learn.lr_find()

# Обучаем модель с найденным learning rate
learn.fine_tune(3, base_lr=1e-2)

# Просмотрим результаты обучения
learn.show_results()

# Эксперименты с параметрами

# Создаем learner с другой моделью
learn = vision_learner(dls, resnet50, metrics=error_rate)

# Найдем оптимальный learning rate
learn.lr_find()

# Обучаем модель с новым learning rate
learn.fine_tune(5, base_lr=1e-2)

# Просмотрим результаты обучения
learn.show_results()

# Создаем DataLoaders с аугментацией
dls = ImageDataLoaders.from_df(df, 
                               path='.', 
                               folder='content/digit-recognition/digits', 
                               valid_pct=0.2, 
                               seed=42, 
                               item_tfms=None, 
                               batch_tfms=aug_transforms())

# Создаем learner
learn = vision_learner(dls, resnet34, metrics=error_rate)

# Найдем оптимальный learning rate
learn.lr_find()

# Обучаем модель с новым learning rate
learn.fine_tune(3, base_lr=1e-2)

# Просмотрим результаты обучения
learn.show_results()









