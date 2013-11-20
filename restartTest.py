import sys
import os
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
if __name__ == "__main__":
    answer = input("Do you want to restart this program ? ")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
