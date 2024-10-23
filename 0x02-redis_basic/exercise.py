#!/usr/bin/env python3
"""
Module for caching and counting method calls in Redis
"""
import redis
import uuid
from typing import Callable, Union, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    Args:
        method (Callable): The method to be decorated.
    Returns:
        Callable: The wrapped function that increments the call count.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count in Redis.
        """
        # Get the qualified name of the method
        key = method.__qualname__

        # Increment the call count using Redis INCR command
        self._redis.incr(key)

        # Call the original method
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Cache class to interact with Redis."""

    def __init__(self):
        """Initialize Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the key.
        Args:
            data (Union[str, bytes, int, float]): The data to store.
        Returns:
            str: The generated key where the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->
    Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and apply a callable function if provided.
        Args:
            key (str): The key to retrieve data from.
            fn (Callable, optional): A function to apply to the retrieved data.
        Returns:
            Union[str, bytes, int, float, None]:
            The retrieved data, possibly transformed.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.
        Args:
            key (str): The key to retrieve data from.
        Returns:
            str: The retrieved data decoded as a string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.
        Args:
            key (str): The key to retrieve data from.
        Returns:
            int: The retrieved data converted to an integer.
        """
        return self.get(key, int)
