#!/usr/bin/env python3
"""Regex-ing"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Replacing """
    for f in fields:
        pattern = re.compile(rf"{f}=(.*?){separator}")
        message = pattern.sub(f"{f}={redaction}{separator}", message)
    return message
