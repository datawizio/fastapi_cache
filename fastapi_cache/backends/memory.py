from typing import Any, Union

from .base import BaseCacheBackend

DEFAULT_TIMEOUT = 0
CACHE_KEY = 'IN_MEMORY'


class InMemoryCacheBackend(BaseCacheBackend):
    def __init__(self):
        self._cache: dict = {}

    async def add(
        self,
        key: Union[str, int],
        value: Any,
        timeout: int = DEFAULT_TIMEOUT
    ) -> bool:
        if key in self._cache:
            return False
        self._cache[key] = value

        return True

    async def get(
        self,
        key: Union[str, int],
        default: Union[str, int] = None,
        **kwargs
    ) -> Any:
        return self._cache.get(key, default)

    async def set(
        self,
        key: Union[str, int],
        value: Any,
        timeout: int = DEFAULT_TIMEOUT
    ) -> bool:
        self._cache[key] = value

        return True

    async def exists(self, *keys: Union[str, int]) -> bool:
        return any(
            map(lambda key: key in self._cache, keys)
        )

    async def delete(self, key: Union[str, int]) -> bool:
        if key not in self._cache:
            return False
        del self._cache[key]

        return True

    async def flush(self) -> None:
        self._cache = {}

    async def close(self) -> None:  # pragma: no cover
        return None
