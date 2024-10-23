#!/usr/bin/env python3
"""
Module for caching and tracking page requests in Redis.
"""
import redis
import requests
from typing import Callable
from functools import wraps

# Initialize the Redis client
r = redis.Redis()

def cache_page(method: Callable) -> Callable:
    """
    Decorator to cache the result of a web page request in Redis.
    It caches the HTML content and tracks the count of accesses.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        # Track how many times the URL has been accessed
        r.incr(f"count:{url}")

        # Check if the page content is already cached
        cached_page = r.get(f"cached:{url}")
        if cached_page:
            print(f"Cache hit for {url}")
            return cached_page.decode('utf-8')

        # If not cached, fetch the page content
        print(f"Fetching new content for {url}")
        page_content = method(url)

        # Cache the result with an expiration of 10 seconds
        r.setex(f"cached:{url}", 10, page_content)

        return page_content

    return wrapper

@cache_page
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL using the requests module.
    Args:
        url (str): The URL of the page to fetch.
    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url)
    return response.text
