#!/usr/bin/env python3
"""Regex-ing"""

import re
import typing


def filter_datum(fields: typing.list[str], redaction: str, message: str,
                 separator: str) -> str:
    """Replacing"""

    for field in fields:
        pattern = re.compile(rf"{field}=(.*?){separator}")
        message = pattern.sub(f"{field}={redaction}{separator}", message)

    return message
