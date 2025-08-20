from mcp.server.fastmcp import FastMCP

mcp = FastMCP("First MCP server")

@mcp.tool()
async def Hello() -> str:
    """
    Sample hello world
    """
    return "hello world"




@mcp.tool()
async def HelloV2(name:str = "john" ) -> str:
    """
    Hello world with parameter
    """
    return f"hello world {name}"