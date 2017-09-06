from django.core.urlresolvers import reverse
from django.test import TestCase


class PraiseListView(TestCase):
    def test_praise_list_view_should_be_accessible(self):
        response = self.client.get(reverse('praise_list'))
        self.assertEqual(response.status_code, 200)

    def test_praise_list_view_should_have_title_saying_pronto_praise(self):
        response = self.client.get(reverse('praise_list'))

        expected = '<title>Pronto Praise</title>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_list_view_should_use_jquery_and_semantic_ui(self):
        response = self.client.get(reverse('praise_list'))

        expected = '<link rel="stylesheet" type="text/css" ' \
            'href="/static/semantic/semantic.min.css">'
        self.assertContains(response, expected, status_code=200)
        expected = '<script\n    src="https://code.jquery.com/' \
            'jquery-3.1.1.min.js"\n    ' \
            'integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDY' \
            'GmIJLv2b8="\n    crossorigin="anonymous"></script>'
        self.assertContains(response, expected, status_code=200)
        expected = '<script src="/static/semantic/semantic.min.js"></script>'
        self.assertContains(response, expected, status_code=200)

    def test_praise_list_view_should_have_header_saying_praise(self):
        response = self.client.get(reverse('praise_list'))

        expected = '<h1 class="ui header">Praise</h1>'
        self.assertContains(response, expected, status_code=200)
