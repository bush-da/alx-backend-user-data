#!/usr/bin/env python3
"""obfuscate the log message"""
import re

def filter_datum(fields, redaction, message, separator):
    """func that obfuscate the log"""
    pattern = f"({'|'.join(fields)})=[^({separator})]+"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
