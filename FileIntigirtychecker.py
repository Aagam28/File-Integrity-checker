import hashlib
import time
import os

# Function to calculate the SHA-256 hash of a file
def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read the file in chunks to avoid memory issues with large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to monitor the file for changes
def monitor_file(file_path, check_interval=5):
    # Get the initial hash value
    previous_hash = calculate_file_hash(file_path)
    if previous_hash is None:
        return  # Exit if the file doesn't exist or there's another error
    
    print(f"Monitoring changes to '{file_path}'...")
    print(f"Initial hash: {previous_hash}")
    
    while True:
        # Wait for the next check interval
        time.sleep(check_interval)
        
        # Calculate the current hash
        current_hash = calculate_file_hash(file_path)
        if current_hash is None:
            return  # Exit if the file doesn't exist or there's another error
        
        # Compare the hashes
        if current_hash != previous_hash:
            print(f"[ALERT] File '{file_path}' has changed!")
            print(f"Old hash: {previous_hash}")
            print(f"New hash: {current_hash}")
            previous_hash = current_hash  # Update the stored hash
        else:
            print(f"File '{file_path}' is unchanged.")
        
        # You can set the program to run indefinitely or add a condition to stop it
        # For example, you could use a keyboard interrupt (Ctrl+C) to stop it.

# Example usage:
if __name__ == "__main__":
    # File to monitor
    file_to_monitor = "example.txt"  # Change this to the path of the file you want to monitor
    monitor_file(file_to_monitor, check_interval=10)  # Check every 10 seconds
