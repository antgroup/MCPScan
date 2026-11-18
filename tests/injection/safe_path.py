import os

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")
BASE = "/srv/data"


@mcp.tool()
def read_file_safe(filename: str) -> str:
    # sanitized: basename strips traversal sequences
    safe = os.path.basename(filename)
    with open(os.path.join(BASE, safe)) as f:
        return f.read()


@mcp.tool()
def read_config() -> str:
    # hardcoded path, no taint source: must NOT fire
    with open("/etc/myapp/config.yml") as f:
        return f.read()


def _internal_read(p: str) -> str:
    # not a @tool entry point: not directly attacker-reachable, must NOT fire
    with open(p) as f:
        return f.read()
