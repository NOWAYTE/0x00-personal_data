#!/usr/bin/env python3
"""Regex-ing"""

import logging
import re


def filter_datum(fields: list[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Replacing """
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}|$', message)
    return message
