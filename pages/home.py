#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import time
import datetime

from selenium.webdriver.common.by import By

from base import Base
from page import PageRegion


class HomePage(Base):
    """This Page Object models the Google Home Page (https://google.com/)."""

    # The title of this page, which is used by is_the_current_page() in page.py
    _page_title = u'Google'
    _search_text_field = (By.NAME, 'q')
    _search_button = (By.CSS_SELECTOR, 'button#gbqfba.gbqfba')


    def go_to_page(self):
    """Open the home page."""
    self.open('/')

    @property
    def is_search_text_available(self):
        return self.is_element_present(*self._search_text_field)

    @property
    def is_search_button_available(self):
        return self.is_element_present(*self._search_button)

    
