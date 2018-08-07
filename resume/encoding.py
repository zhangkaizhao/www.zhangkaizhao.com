import base64
import os.path
from textwrap import wrap

FILES = [
    'zhangkaizhao-resume-en.txt',
    'zhangkaizhao-resume-en.pdf',
    'zhangkaizhao-resume-zh.txt',
    'zhangkaizhao-resume-zh.pdf',
]
LINE_LENGTH = 80
ENCODED = '.encoded'
DECODED = '.decoded'


def append_filename(filename, appended):
    raw, ext = os.path.splitext(filename)
    return f"{raw}{appended}{ext}"


def encode():
    for filename in FILES:
        with open(filename, 'rb') as f:
            content = f.read()

        encoded_content = base64.b64encode(content)
        wrapped = wrap(encoded_content.decode('utf-8'), LINE_LENGTH)
        wrapped_content = '\r\n'.join(wrapped).encode('utf-8')
        encoded_filename = f'{filename}{ENCODED}.txt'

        with open(encoded_filename, 'wb') as f:
            f.write(wrapped_content)


def decode():
    for filename in FILES:
        encoded_filename = f'{filename}{ENCODED}.txt'
        with open(encoded_filename, 'rb') as f:
            content = f.read()

        unwrapped_content = b''.join(content.split(b'\r\n'))
        decoded_content = base64.b64decode(unwrapped_content)

        decoded_filename = append_filename(filename, DECODED)
        with open(decoded_filename, 'wb') as f:
            f.write(decoded_content)


if __name__ == '__main__':
    import sys
    action = sys.argv[1:2]
    if action == ['encode']:
        encode()
    elif action == ['decode']:
        decode()
    else:
        print(f"Usage: python {sys.argv[0]} encode|decode")
