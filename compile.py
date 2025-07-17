import subprocess
import os

def compile_driver(source_path):
    compile_cmd = f"gcc -Wall -Werror -D__KERNEL__ -DMODULE -I/usr/src/linux-headers-$(uname -r)/include -c {source_path}"
    result = subprocess.run(compile_cmd, shell=True, capture_output=True, text=True)
    return {
        "success": result.returncode == 0,
        "warnings": result.stderr.count("warning"),
        "errors": result.stderr.count("error"),
        "output": result.stderr
    }

if __name__ == "__main__":
    res = compile_driver("driver_from_model.c")
    print(res)
