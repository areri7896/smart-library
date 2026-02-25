import subprocess
import sys
import os

def main():
    """ Runs the Smart Library System module. """
    print("--- Starting Smart Library System ---\n")
    
    # We need to run it as a module because of relative imports
    # The current directory should be the parent of the package folder
    # However, since we are inside the package folder (django rwanda assignment),
    # we should run it from the parent directory or use a trick.
    
    # Since the user specifically asked for a file in this project, 
    # and the project structure seems to be 'django rwanda assignment' as the root package,
    # we will run it using the parent directory logic.
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    package_name = os.path.basename(script_dir)
    
    try:
        # Run: python -m "package_name"
        subprocess.run([sys.executable, "-m", package_name], cwd=parent_dir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Error running: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
