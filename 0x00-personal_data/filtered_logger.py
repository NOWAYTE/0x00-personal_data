#!/usr/bin/env python3
"""Regex-ing"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Replacing"""
    if not (
            isinstance(fields, list) and
            all(isinstance(item, str) for item in fields)):
        raise TypeError("Fields must be a list of strings")
    if not isinstance(redaction, str):
        raise TypeError("Redaction must be a string")
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    if not isinstance(separator, str):
        raise TypeError("Separator must be a string")

    for field in fields:
        pattern = re.compile(rf"{field}=(.*?){separator}")
        message = pattern.sub(f"{field}={redaction}{separator}", message)

    return message
