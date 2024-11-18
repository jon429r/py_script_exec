import sys

# Check for arguments passed to the script
if len(sys.argv) > 1:
    print(f"Arguments received: {sys.argv[1:]}")
else:
    print("No arguments received.")
