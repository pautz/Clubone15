from cx_Freeze import setup, Executable

build_options = {
    "packages": ["webview"],
    "includes": [],
    "include_files": [],
    "excludes": [],
}

setup(
    name="Clubone15",
    version="1.0",
    description="Abrir site em tela cheia",
    options={"build_exe": build_options},
    executables=[Executable("clubone15.py")]
)
