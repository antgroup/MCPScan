import os
from pathlib import Path

from mcp.server import Server
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")
server = Server("demo")
BASE = "/srv/data"


@mcp.tool()
def read_file(filename: str) -> str:
    # ruleid: mcp-tool-input-path-traversal
    with open(filename) as f:
        return f.read()


@mcp.tool()
def fetch_doc(path: str) -> bytes:
    # ruleid: mcp-tool-input-path-traversal
    return Path(path).read_bytes()


@mcp.tool()
def download(name: str) -> bytes:
    # os.path.join is NOT a sanitizer: traversal in `name` survives
    full = os.path.join(BASE, name)
    # ruleid: mcp-tool-input-path-traversal
    return Path(full).read_bytes()


@server.call_tool()
async def dispatch(name: str, arguments: dict):
    # low-level MCP dispatcher: arguments[...] is attacker-controlled.
    # (GIT cross-check FN class (b): @call_tool source now covered.)
    # ruleid: mcp-tool-input-path-traversal
    return open(arguments["path"]).read()
