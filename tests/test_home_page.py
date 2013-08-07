#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import datetime

from BeautifulSoup import BeautifulStoneSoup    # Only required for the test that doesn't use Selenium
import pytest
import requests
from unittestzero import Assert

from pages.home import HomePage
from base_test import BaseTest


class TestHomePage(BaseTest):


    @pytest.mark.nondestructive
    def test_that_search_text_field_is_available(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.true(is_search_text_available)

    @pytest.mark.nondestructive
    def test_that_search_button_is_available(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_page()
        Assert.true(is_search_button_available)



