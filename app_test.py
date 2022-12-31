from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

test_boggle = Boggle()


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
            res = self.client.get('/')
            html = res.get_data(as_text=True)
            # gameboard generating?
            self.assertIn('<table id="game-board">', html)   
            # page loading appropriately
            self.assertEqual(res.status_code, 200)
            self.assertIn('board', session)
