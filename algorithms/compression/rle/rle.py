#!/usr/bin/env python3

def encode(text):
    """Encode text using Run-Length Encoding algorithm"""
    res = []
    counter = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            counter += 1
        else:
            res += [str(counter), text[i-1]]
            counter = 1
    res += [str(counter), text[i-1]]
    return "".join(res)

def decode(text):
    """Decode text using Run-Length Encoding algorithm"""
    res = ''
    for i in range(len(text)):
        if text[i].isdigit():
            res += text[i+1] * int(text[i])
    return res

