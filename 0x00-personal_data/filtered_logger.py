#!/usr/bin/env python3
"""Regex-ing"""

import logging
import re


def filter_datum(fields: list[str], redaction: str, message: str,separator: str) -> str:
    """Replaces values with specified fields"""
    for i in fields:
        print(i)
        pattern = re.sub(rf"{i}=(.*?)(?={separator}|$)",
               f'{i}={redaction}', message)

    return pattern
