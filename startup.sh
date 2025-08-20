#!/bin/bash

# Optional: Activate virtual environment if needed
# source myenv/bin/activate

# Start the MCP server
mcp dev sample.py --host 0.0.0.0 --port 3000
#mcp dev sample.py --host 0.0.0.0 --port ${PORT}

