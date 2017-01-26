# Hoef je niet te gebruiken, hiermee kan je .exe maken
import cx_Freeze

executables = [cx_Freeze.Executable("Battleport.py")]

cx_Freeze.setup(
    name="Battle Port Rotterdam",
    options={"build_exe":{"packages":["pygame"],
                          "include_files":["ship.png"]}},
    executables = executables

)
