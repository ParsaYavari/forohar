import os
import subprocess
import shutil

cwd = os.getcwd()

print('''
      
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B?Y5G&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5JJ?Y&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#JJ?75@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G?YY?Y&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##&@@@@@@&J5YJP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@GYJPGB&@@B5J77?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#BGGY??YP5J7775@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#5@G?55????777?G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#BBB##J777777YG@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        YJJJG5JYYYYYYBYJYYYYYYYYYYYY5GPJJJJJJJJJJJJJJYJ7777?Y?JJJJJJJJJJJJJJYGPYYYYYYYYYYYJJJYBYYYYYYYBYYYJY
        BJ??YGJJJJJJJPPJ?JJJJJJJJJJYYY5P5YJ????????77YGJ?77Y?5J77???????JJY5P5YYYJJJJJJJJJJ?JP5JJJJJ?5PJJ?JB
        @BY?J5GYJJJJJJ5PYJJJJJJJJJJYYYYY5555555555PYY@PJJ?JJ7#&J5P555555555YYYYYJJJJJJJJJJJ5G5JJJJJJPPJJ?YB@
        @@&GYJJPPYYJJJJJ5PYYJJJJJJJJJJJJJJJ?J?J??J5JP@Y??YY77G@5YYJJJJJJJJJJJJJJJJJJJJJJY5P5JJJJJY5P5JJYG&@@
        @@@@@#PYJY555YYJJJYY55555555Y5Y5Y5Y5Y5Y55YPPJ#Y7??777P#JG55Y5Y5Y555Y5Y5Y5Y55555Y5YJJJYY55YYJYP#@@@@@
        @@@@@@@@##GPGPP55Y5Y55Y555P5555P5P555555P5PP5Y55YYYY55YPP5P55555P55YPYP55P555Y5555555P5GPG##@@@@@@@@
        @@@@@@@@@@@@@@@&#&##&##&###B#BB#B#B#B###5J5GJ5555555555?P5JP###B#B#B##B#B##B&##&##&#&@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5Y#@PJJJJYYYYJJYJP@BJP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@YJ@@&YYYJJJJJJJJYYY#@#?G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5J5@@PJ&@@55PP5P555PP5P555@@B?G@&YJP@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&J??P55&@@G55PPY5P55P55PP5PP@@#555??Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&@@@@&?JJJYYY5YYYYYY?JJJ#@@@&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BBP55JYJJYY55PB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
        
                                              Developed By ParsaYavari   
                                            The Irnain Termux For Windows     
                                               For Exit Enter Ctrl+C    
                                                 Docs In a Git Hub  
                                    GitHub -> https://github.com/ParsaYavari/Forohar 
                                                          
      
      ''')

# Simple map of known packages and their winget or choco names
pkg_map = {
    "git": "Git.Git",
    "python": "Python.Python.3",
    "nodejs": "OpenJS.NodeJS",
    "nmap": "nmap",  # available via choco
    "curl": "curl",
    "wget": "GnuWin32.Wget"
}

# Check if winget exists
has_winget = shutil.which("winget") is not None

while True:
    try:
        cmd = input(f"{cwd} $ ").strip()
        if not cmd:
            continue

        if cmd == "exit":
            break

        elif cmd.startswith("cd "):
            path = cmd[3:].strip()
            new_path = os.path.abspath(os.path.join(cwd, path))
            if os.path.isdir(new_path):
                cwd = new_path
            else:
                print(f"[ ✕ ] Not Found ▹ '{path}'")

        elif cmd.startswith("pkg install "):
            pkg_name = cmd[len("pkg install "):].strip()
            mapped_pkg = pkg_map.get(pkg_name)
            if not mapped_pkg:
                print(f"[✗] Package '{pkg_name}' not found in this Termux.")
                continue

            print(f"[+] Installing {pkg_name}...")
            try:
                if has_winget:
                    subprocess.run(["winget", "install", "--silent", "--accept-package-agreements", "--accept-source-agreements", mapped_pkg], cwd=cwd)
                else:
                    print("[✗] Winget not available. Please install Chocolatey or another package manager.")
            except Exception as e:
                print(f"[✗] Installation failed: {e}")

        else:
            subprocess.run(cmd, shell=True, cwd=cwd)

    except KeyboardInterrupt:
        print("\n[✗] Exited with Ctrl+C.")
    except Exception as e:
        print(f"[!] Error: {e}")










