"""Run with: python -m unittest discover -s tests -v."""
import os
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
import unittest

from playwright.sync_api import sync_playwright, expect


class LandingFlows(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[1]
        cls.server = ThreadingHTTPServer(
            ('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(root)))
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f'http://127.0.0.1:{cls.server.server_port}'
        cls.playwright = sync_playwright().start()
        options = {}
        if os.environ.get('PLAYWRIGHT_CHROMIUM_EXECUTABLE'):
            options['executable_path'] = os.environ['PLAYWRIGHT_CHROMIUM_EXECUTABLE']
        cls.browser = cls.playwright.chromium.launch(**options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        self.page = self.browser.new_page(viewport={'width': 1440, 'height': 1000})
        self.page.goto(self.url)

    def tearDown(self):
        self.page.close()

    def test_contact_validation_and_honest_confirmation(self):
        form = self.page.locator('#sales-form')
        form.get_by_role('button').click()
        expect(form.locator('[aria-invalid=true]')).to_have_count(6)
        for name, value in {'name': 'Rúbens', 'company': 'Granja piloto',
                            'email': 'invalid', 'phone': 'abc', 'ponds': '1.5',
                            'message': 'Solicito una demostración'}.items():
            form.locator(f'[name={name}]').fill(value)
        form.get_by_role('button').click()
        expect(form.locator('[aria-invalid=true]')).to_have_count(3)
        form.locator('[name=email]').fill('piloto@example.com')
        form.locator('[name=phone]').fill('999888777')
        form.locator('[name=ponds]').fill('3')
        form.get_by_role('button').click()
        expect(form.locator('[aria-invalid=true]')).to_have_count(0)
        expect(self.page.get_by_role('status')).to_contain_text('no se ha enviado')
        form.locator('[name=name]').fill('Otro nombre')
        expect(self.page.get_by_role('status')).to_be_empty()

    def test_trace_and_web_navigation(self):
        self.page.locator('nav').get_by_role('link', name='YakuTrace').click()
        expect(self.page).to_have_url(self.url + '/#section-yakutrace')
        self.page.get_by_role('link', name='Ver cómo verificar un lote').click()
        expect(self.page.locator('#trace-demo')).to_contain_text('no verifica un lote real')
        links = self.page.locator('a[href="https://yakucontrol-v2.web.app"]')
        expect(links).to_have_count(2)
        expect(self.page.locator('.pricing-grid')).to_contain_text('Por definir')

    def test_terms_and_privacy(self):
        self.page.locator('footer').get_by_role('link', name='Términos y Condiciones').click()
        expect(self.page.get_by_role('heading', name='Términos y Condiciones')).to_be_visible()
        expect(self.page.locator('#datos')).to_be_visible()
        self.page.get_by_role('link', name='Volver a YakuControl').click()
        expect(self.page.locator('#sales-form')).to_have_count(1)

    def test_mobile_navigation_and_no_horizontal_overflow(self):
        self.page.set_viewport_size({'width': 390, 'height': 844})
        self.page.reload()
        self.page.locator('nav').get_by_role('link', name='Solicitar Demo').click()
        expect(self.page.locator('#sales-name')).to_be_in_viewport()
        self.assertTrue(self.page.evaluate(
            'document.documentElement.scrollWidth <= window.innerWidth'))
        expect(self.page.locator('footer').get_by_role('link', name='Términos y Condiciones')).to_be_visible()


if __name__ == '__main__':
    unittest.main()
