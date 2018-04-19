#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the download helper object implementations."""

from __future__ import unicode_literals

import os
import unittest

from l2tdevtools.download_helpers import pypi


@unittest.skipIf(
    os.environ.get('TRAVIS_OS_NAME') == 'osx',
    'Test is flaky for macOS on Travis')
class PyPIDownloadHelperTest(unittest.TestCase):
  """Tests for the PyPi download helper."""

  _DOWNLOAD_URL = 'https://pypi.python.org/pypi/dfvfs'

  _PROJECT_NAME = 'dfvfs'
  _PROJECT_VERSION = '20180418'

  def testGetLatestVersion(self):
    """Tests the GetLatestVersion functions."""
    download_helper = pypi.PyPIDownloadHelper(self._DOWNLOAD_URL)

    latest_version = download_helper.GetLatestVersion(self._PROJECT_NAME, None)

    self.assertEqual(latest_version, self._PROJECT_VERSION)

  def testGetDownloadURL(self):
    """Tests the GetDownloadURL functions."""
    download_helper = pypi.PyPIDownloadHelper(self._DOWNLOAD_URL)

    expected_download_url = (
        'https://pypi.python.org/packages/source/d/{0:s}/'
        '{0:s}-{1:s}.tar.gz').format(self._PROJECT_NAME, self._PROJECT_VERSION)

    download_url = download_helper.GetDownloadURL(
        self._PROJECT_NAME, self._PROJECT_VERSION)

    self.assertEqual(download_url, expected_download_url)

  def testGetProjectIdentifier(self):
    """Tests the GetProjectIdentifier functions."""
    download_helper = pypi.PyPIDownloadHelper(self._DOWNLOAD_URL)

    project_identifier = download_helper.GetProjectIdentifier()

    expected_project_identifier = 'org.python.pypi.{0:s}'.format(
        self._PROJECT_NAME)

    self.assertEqual(project_identifier, expected_project_identifier)


if __name__ == '__main__':
  unittest.main()
