#!/usr/bin/env python
# -*- coding: UTF-8 -*-


#bytes[] 直接取int值
content = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x36'
for i in range(len(content)):
    print(content[i])
