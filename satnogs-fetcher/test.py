import os
import subprocess

# Specify the directory containing the binary files
directory = 'cache'

# Iterate through all files in the specified directory
for filename in os.listdir(directory):
    # Construct full file path
    file_path = os.path.join(directory, filename)

    # Check if it's a file and has no extension
    if os.path.isfile(file_path) and '.' not in filename:
        # Call the command with the file name
        subprocess.run(['decode_frame', 'lightsail2', file_path])
