import subprocess
import sys
import os

def main():
    """ Runs the Smart Library System unit tests. """
    print("--- Running Smart Library System Tests ---\n")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    package_name = os.path.basename(script_dir)
    
    try:
        # Run: python -m unittest "package_name".test_system
        subprocess.run(
            [sys.executable, "-m", "unittest", f"{package_name}.test_system"], 
            cwd=parent_dir, 
            check=True
        )
    except subprocess.CalledProcessError:
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
