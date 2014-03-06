import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["tkinter"], "include_files": ["hearsomething.wav", "fellowscientist.wav"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Sound Board",
        version = "0.1.2",
        description='Sound Board',
        author='Erik Forsberg',
        author_email='erik.c.forsberg@gmail.com',
        options = {"build_exe": build_exe_options},
        executables = [Executable("SoundBoard.py", base=base)])
