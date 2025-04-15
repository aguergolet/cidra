import logging

def execute_tool(tool_id, params, config):
    """Executes a tool based on its ID and parameters."""
    try:
        # Find the tool configuration
        tool_config = next((tool for tool in config['tools'] if tool['id'] == tool_id), None)
        if not tool_config:
            raise Exception(f"Tool with ID {tool_id} not found.")

        # Simulate tool execution (replace with actual logic)
        logging.info(f"Executing tool: {tool_id} with params: {params}")
        result = {
            "tool_id": tool_id,
            "status": "success",
            "output": f"Executed {tool_id} with params {params}"
        }
        return result
    except Exception as e:
        logging.error(f"Failed to execute tool '{tool_id}': {e}")
        raise Exception(f"Error executing tool '{tool_id}'.")