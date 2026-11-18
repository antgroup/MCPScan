import os
import shlex
import subprocess

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")


@mcp.tool()
def list_dir(name: str) -> bytes:
    # list form, no shell=True: argument is not shell-interpreted -> must NOT fire
    # (MCPScan's flat rule would flag this as a false positive)
    return subprocess.check_output(["ls", "-l", name])


@mcp.tool()
def echo_safe(arg: str) -> int:
    # sanitized with shlex.quote -> must NOT fire
    return os.system("echo " + shlex.quote(arg))


@mcp.tool()
def uptime() -> int:
    # hardcoded command, no taint -> must NOT fire
    return os.system("uptime")
