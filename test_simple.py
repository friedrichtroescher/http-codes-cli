import os

print("Testing basic operations...")

# Test 1: Check if we can get the home directory
print(f"Home directory: {os.path.expanduser('~')}")

# Test 2: Check if we can create a directory
test_dir = os.path.join(os.path.expanduser("~"), "test_http_cli")
print(f"Creating test directory: {test_dir}")
os.makedirs(test_dir, exist_ok=True)
print(f"Directory exists: {os.path.exists(test_dir)}")

# Test 3: Check if we can create a file
test_file = os.path.join(test_dir, "test.txt")
print(f"Creating test file: {test_file}")
with open(test_file, "w") as f:
    f.write("test")
print(f"File exists: {os.path.exists(test_file)}")

# Clean up
os.remove(test_file)
os.rmdir(test_dir)
print("Test completed successfully!")
