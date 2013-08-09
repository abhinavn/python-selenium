#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.page import Page


class Base(Page):
    """
    Base class for global project specific functions
    """

    @property
    def footer(self):
        """Return the common Footer region."""
        return self.Footer(self.testsetup)

    class Footer(Page):
        """The common Footer region that is present on every page."""

        # The locators in this list contain examples of positional locators, a unique css locator,
        # and a link text locator
        copyright_links_list = [
            {
                'locator': (By.CSS_SELECTOR, 'div#flls a:nth-of-type(1)'),
                'url_suffix': 'https://www.google.com/intl/en/ads/',
            }, {
                'locator': (By.CSS_SELECTOR, 'div#flls a:nth-of-type(2)'),
                'url_suffix': 'https://www.google.com/services/'
            }, {
                'locator': (By.CSS_SELECTOR, 'div#flls a:nth-of-type(3)'),
                'url_suffix': 'https://www.google.com/intl/en/policies/'
            }, {
                'locator': (By.CSS_SELECTOR, 'div#flrs a:nth-of-type(1)'),
                'url_suffix': 'https://plus.google.com/+google/'
            }, {
                'locator': (By.CSS_SELECTOR, 'div#flrs a:nth-of-type(2)'),
                'url_suffix': 'https://www.google.com/intl/en/about/'
            }
        ]
