#!/usr/bin/env python3
"""web cache and tracker"""
import requests
import redis
from functools import wraps
from typing import Callable

store = redis.Redis()


def count_url_access(method: callable):
    """ Decorator counting how many times the URL is accessed """
    @wraps(method)
    def wrapper(url: str):
        """wrapper func"""
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ get HTML content of a url """
    res = requests.get(url)
    return res.text
