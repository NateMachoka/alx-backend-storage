#!/usr/bin/env python3
"""
Module for caching and storing data in Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class to interact with Redis."""

    def __init__(self):
        """Initialize Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
