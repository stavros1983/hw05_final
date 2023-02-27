from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post, Comment

User = get_user_model()

STR_NUMBER = 15


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="auth")
        cls.group = Group.objects.create(
            title="Тестовая группа",
            slug="Тестовый слаг",
            description="Тестовое описание",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text="Тестовая запись",
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей поста корректно работает __str__."""
        expected_object_name = PostModelTest.post.text[:STR_NUMBER]
        self.assertEqual(expected_object_name, str(PostModelTest.post))

    def test_verbose_name(self):
        """verbose_name в полях поста совпадает с ожидаемым."""
        field_verboses = {
            "text": "Текст поста",
            "pub_date": "Дата публикации",
            "author": "Автор",
            "group": "Группа",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.post._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        """help_text в полях поста совпадает с ожидаемым."""
        field_help_texts = {
            "text": "Введите текст поста",
            "group": "Группа, к которой будет относится пост",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.post._meta.get_field(value).help_text, expected
                )


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title="Заголовок тестовой группы",
            slug="testslug",
            description="Тестовое описание",
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей группы корректно работает __str__."""
        expected_object_name = GroupModelTest.group.title
        self.assertEqual(expected_object_name, str(GroupModelTest.group))

    def test_verbose_name(self):
        """verbose_name в полях модели совпадает с ожидаемым."""
        field_verboses = {
            "title": "Название",
            "slug": "Ссылка на группу",
            "description": "Описание",
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.group._meta.get_field(value).verbose_name, expected
                )

    def test_help_text(self):
        """help_text в полях модели совпадает с ожидаемым."""
        field_help_texts = {
            "title": "Введите название группы",
            "slug": "Укажите ссылку на группу",
            "description": "Введите описание группы",
        }
        for value, expected in field_help_texts.items():
            with self.subTest(value=value):
                self.assertEqual(
                    self.group._meta.get_field(value).help_text, expected
                )


class CommentModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            text='Тестовый пост',
            author=cls.user,
        )
        cls.comment = Comment.objects.create(
            text='Комментарий для поста',
            author=cls.user,
            post=cls.post,
        )

    def test_сomment_str(self):
        """Проверка __str__ у сomment."""
        self.assertEqual(self.comment.text[:15], str(self.comment))

    def test_сomment_verbose_name(self):
        """Проверка verbose_name у сomment."""
        field_verboses = {
            'post': 'Пост',
            'author': 'Автор',
            'text': 'Коментарий',
            'created': 'Создан',
            'updated': 'Обнавлен',
            'active': 'Активен',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                verbose_name = self.comment._meta.get_field(value).verbose_name
                self.assertEqual(verbose_name, expected)
