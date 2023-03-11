import os


class Playwright:
    PAGE_VIEWPORT_SIZE = {'width': 1920, 'height': 1080}
    BROWSER = os.getenv('BROWSER') or 'chrome'
    IS_HEADLESS = os.getenv('HEADLESS') or False
    SLOW_MO = os.getenv('SLOW_MO') or 50
    LOCALE = 'en-US'
