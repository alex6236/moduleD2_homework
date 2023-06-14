**Что вы должны сделать в консоли Django?**

```python
from news.models import *
```

1. Создать двух пользователей (с помощью метода `User.objects.create_user`).

   ```python
   user1 = User.objects.create_user(username='user1', first_name='Альберт', last_name='Клячкин')
   user2 = User.objects.create_user(username='user2', first_name='Бронислав', last_name='Пупков')
   ```

2. Создать два объекта модели Author, связанные с пользователями.
   ```python
   author1 = Author.objects.create(authorUser=user1)
   author2 = Author.objects.create(authorUser=user2)
   ```
3. Добавить 4 категории в модель Category.
   ```python
   Category.objects.create(name='sports')
   Category.objects.create(name='politics')
   Category.objects.create(name='education')
   Category.objects.create(name='technology')
   ```
4. Добавить 2 статьи и 1 новость.
   ```python
   Post.objects.create(author=Author.objects.get(id=1), categoryType='AR', title='Статья 1', text='Текст статьи 1')
   Post.objects.create(author=Author.objects.get(id=2), categoryType='NW', title='Новость', text='Текст новости')
   Post.objects.create(author=Author.objects.get(id=1), categoryType='AR', title='Статья 2', text='Текст статьи 2')
   Post.objects.create(author=Author.objects.get(id=2), categoryType='NW', title='Новость 2', text='Текст новости 2')
   ```
5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).

```python
   PostCategory.objects.create(postThrough=Post.objects.get(title='Статья 1'), categoryThrough=Category.objects.get(name='education'))
   PostCategory.objects.create(postThrough=Post.objects.get(title='Новость'), categoryThrough=Category.objects.get(name='sports'))
   PostCategory.objects.create(postThrough=Post.objects.get(title='Статья 2'), categoryThrough=Category.objects.get(name='technology'))
   PostCategory.objects.create(postThrough=Post.objects.get(title='Новость 2'), categoryThrough=Category.objects.get(name='politics'))
   PostCategory.objects.create(postThrough=Post.objects.get(title='Статья 1'), categoryThrough=Category.objects.get(name='technology'))
```

6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
8. Обновить рейтинги пользователей.
9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
