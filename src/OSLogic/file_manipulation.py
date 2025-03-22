from langgraph.graph import StateGraph
import openai
import os

# Custom file operation tools
def read_file(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def write_file(path, content):
    try:
        with open(path, 'w') as f:
            f.write(content)
        return f"Successfully wrote to {path}"
    except Exception as e:
        return f"Error writing to file: {str(e)}"
        
def delete_file(path):
    try:
        os.remove(path)
        return f"Successfully deleted {path}"
    except Exception as e:
        return f"Error deleting file: {str(e)}"