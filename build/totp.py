#!/usr/bin/env python3
"""
Generates a TOTP code.

Based on MinTOTP by Susam Pal.
"""
# Forked from <https://github.com/susam/mintotp>.


import base64
import binascii
import getpass
import hmac
import struct
import sys
import time


def hotp(key, counter, digits=6, digest='sha1'):
    key = base64.b32decode(key.upper() + '=' * ((8 - len(key)) % 8))
    counter = struct.pack('>Q', counter)
    mac = hmac.new(key, counter, digest).digest()
    offset = mac[-1] & 0x0f
    binary = struct.unpack('>L', mac[offset:offset+4])[0] & 0x7fffffff
    return str(binary)[-digits:].zfill(digits)


def totp(key, time_step=30, digits=6, digest='sha1'):
    return hotp(key, int(time.time() / time_step), digits, digest)


def normalize_key(key):
    return "".join((c for c in key if not c.isspace()))


def main():
    args = [int(x) if x.isdigit() else x for x in sys.argv[1:]]
    
    if (len(args) == 0):
        key = getpass.getpass(prompt="TOTP key: ")
    else:
        key = args[0]
    
    print(totp(normalize_key(key)))


if __name__ == "__main__":
    try:
        main()
    except binascii.Error as e:
        print(e, file=sys.stderr)
    except KeyboardInterrupt:
        sys.exit(1)