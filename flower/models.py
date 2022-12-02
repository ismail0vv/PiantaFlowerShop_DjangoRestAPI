from django.db import models
from Pianta import settings

# Create your models here.

# Моделька Цветов (flower)
# title
# price
# description
# categories ManyToMany
# colors ManyToMany
# sold_quantity

# Моделька категорий
# title


# Моделька Цветов (color)
# color_title


# Моделька Фото
# flower Foreign Key related_name
# image = ImageField


# Отзывы
# user
# text
# stars 0 - 10 типо пол звезды еще есть
# created_at
# Initials