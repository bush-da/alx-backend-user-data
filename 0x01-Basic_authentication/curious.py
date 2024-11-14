#!/usr/bin/env python3
import base64


string = "hello world"


encoded_string = base64.b64encode(string.encode('utf-8')).decode('utf-8')

print(f"the first message {string} the encoded message {encoded_string}")
