#!/usr/bin/env python
"""encrypt a secret to avoid plain text"""
import hashlib

ENCRYPTION_KEY = 'v1k1k3y'
SECRET = 'no-0ne-kn0w5-m3'

ENCRYPTION_SECRET = hashlib.sha224(ENCRYPTION_KEY.encode()).hexdigest()

print(ENCRYPTION_SECRET)
