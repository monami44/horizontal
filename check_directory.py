import os

def check_directory_access(directory_path):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Directory does not exist: {directory_path}")
        return False
    
    # Check if the directory is readable
    if not os.access(directory_path, os.R_OK):
        print(f"Directory is not readable: {directory_path}")
        return False
    
    try:
        # Attempt to list the directory contents
        files = os.listdir(directory_path)
        print(f"Directory is accessible, contents: {files}")
        return True
    except Exception as e:
        # Handle any error that occurred while reading the directory
        print(f"Error accessing the directory: {e}")
        return False

# Example usage
directory_path = '/Users/maksymliamin/Desktop/Work/Data Science/Crew AI/brad_Financeteam/output'
check_directory_access(directory_path)
