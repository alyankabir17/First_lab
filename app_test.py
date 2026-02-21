import os

def test_file_exists():
    if os.path.exists("index.html"):
        print("Test Passed: index.html found.")
    else:
        print("Test Failed: index.html missing!")
        exit(1)

if __name__ == "__main__":
    test_file_exists()
