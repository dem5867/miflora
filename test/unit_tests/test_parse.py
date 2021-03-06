"""
Created on Jul 8, 2016

@author: matuschd
"""

import unittest
from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE
from test.helper import MockBackend
from datetime import datetime


class KNXConversionTest(unittest.TestCase):

    def test_parsing(self):
        """Does the Mi Flora data parser works correctly?"""
        poller = MiFloraPoller(None, MockBackend)
        data = bytes([0x25, 0x01, 0x00, 0xf7, 0x26, 0x00, 0x00, 0x28,
                      0x0e, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        poller._cache = data
        self._last_read = datetime.now()
        self.assertEquals(poller._parse_data()[MI_CONDUCTIVITY], 270)
        self.assertEquals(poller._parse_data()[MI_MOISTURE], 40)
        self.assertEquals(poller._parse_data()[MI_LIGHT], 9975)
        self.assertEquals(poller._parse_data()[MI_TEMPERATURE], 29.3)

        data = bytes([0xf2, 0x00, 0x00, 0x79, 0x00, 0x00, 0x00, 0x10,
                      0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x000])
        poller._cache = data
        self._last_read = datetime.now()
        self.assertEquals(poller._parse_data()[MI_CONDUCTIVITY], 101)
        self.assertEquals(poller._parse_data()[MI_MOISTURE], 16)
        self.assertEquals(poller._parse_data()[MI_LIGHT], 121)
        self.assertEquals(poller._parse_data()[MI_TEMPERATURE], 24.2)
