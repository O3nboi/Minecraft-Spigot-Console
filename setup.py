from cx_Freeze import setup, Executable
setup(
    name = "Spigot Console",
    version = "1.1",
    description = "Open a Minecraft Server",
    executables = [Executable("Spigot Console.py")]
    )