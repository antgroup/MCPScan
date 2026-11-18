import requests

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")


class _Cache:
    def get(self, key):
        return None


cache = _Cache()


@mcp.tool()
def health() -> int:
    # hardcoded URL, no taint -> must NOT fire
    return requests.get("https://api.internal/health").status_code


@mcp.tool()
def cache_lookup(key: str):
    # generic .get() on a non-HTTP object: must NOT fire
    # (this is the false positive that matching every .get() would cause)
    return cache.get(key)
