from cx_Freeze import setup, Executable

setup(
    name="ExecDont_Bother",
    version="0.1",
    description="The python file that makes the MAIN.py a executable",
    executables=[Executable("MAIN.py")]
)

