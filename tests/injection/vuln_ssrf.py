import urllib.request

import httpx
import requests

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")


@mcp.tool()
def fetch(url: str) -> str:
    # ruleid: mcp-tool-input-ssrf
    return requests.get(url).text


@mcp.tool()
def preview(target: str) -> int:
    # kwarg form: url=<tainted>
    # ruleid: mcp-tool-input-ssrf
    return httpx.get(url=target).status_code


@mcp.tool()
def download(u: str) -> bytes:
    # ruleid: mcp-tool-input-ssrf
    return urllib.request.urlopen(u).read()
