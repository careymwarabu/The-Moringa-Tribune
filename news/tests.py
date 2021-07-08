from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt


# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.carey= Editor(first_name = 'Carey', last_name ='Mwarabu', email ='carey@gmail.com')

     # To tear down instance
    def tearDown(self):
        Editor.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.carey,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.carey.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    # Testing delete method
    def test_delete_method(self):
        self.carey.delete_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors)== 0)
    def test_get_all(self):
        self.carey.get_all()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)==1)

    def test_update_editor(self):
        self.carey.save_editor()
        self.carey.update_editor(self.carey.id,'Carey')
        vee=Editor.objects.get(first_name='Carey')
        self.assertEqual(vee.first_name, 'Carey')


class ArticleTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.carey = Editor(first_name='Carey', last_name='Mwarabu', email='carey@gmail.com')
        self.carey.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name="testing")
        self.new_tag.save()

        # Creating a new article and saving it
        self.new_article = Article(title='Test Article', post='This is a random test post', editor=self.carey)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d')
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)

