from django.test import RequestFactory, TestCase

from .views import IndexView


class IndexViewTest(TestCase):
    def test_template_name_in_context(self):
        request = RequestFactory().get("/")
        view = IndexView()
        view.setup(request)

        context = view.template_name
        self.assertEquals("index.html", context)
