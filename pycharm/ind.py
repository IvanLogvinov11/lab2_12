#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decorator_func(func):

    def wrapper(text, chars=' !?'):
        text = ''.join(['-' if i in chars else i for i in text])
        while '--' in text:
            text = text.replace('--', '-')
        return func(text)

    return wrapper


@decorator_func
def rus_lat(text):

    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

    text = ''.join([t[i] if i != '-' else '-' for i in text])
    return text


if __name__ == '__main__':
    txt = "Текст     ???? который .... нужно !!::заменить".lower()
    print(rus_lat(txt, chars='?!:;,. '))