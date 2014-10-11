"""
Tests for `cid` module
"""

# Copyright (C) 2009-2013 Thomas Aglassinger
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from cutplace import cid

import logging
import unittest


class Cidtest(unittest.TestCase):
    """
    Tests for cid module
    """
    _TEST_ENCODING = "iso-8859-1"

    def test_can_read_excel_and_create_dataformat(self):
        cidreader = cid.Cid()
        cidreader.read("c://icd_customers.xls")

        self.assertEqual(cidreader._data_format.format, "delimited")
        self.assertEqual(cidreader._data_format.header, 1)


