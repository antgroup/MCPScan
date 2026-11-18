import os
import subprocess

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")


@mcp.tool()
def run_cmd(cmd: str) -> int:
    # ruleid: mcp-tool-input-command-injection
    return os.system(cmd)


@mcp.tool()
def build(target: str) -> bytes:
    # f-string keeps the taint; shell=True makes it injectable
    # ruleid: mcp-tool-input-command-injection
    return subprocess.check_output(f"make {target}", shell=True)


@mcp.tool()
def calc(expr: str):
    # ruleid: mcp-tool-input-command-injection
    return eval(expr)
