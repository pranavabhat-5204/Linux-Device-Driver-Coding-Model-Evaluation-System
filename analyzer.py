import subprocess

def run_cppcheck(file_path):
    result = subprocess.run(["cppcheck", "--enable=all", "--std=c99", file_path], capture_output=True, text=True)
    issues = result.stderr.splitlines()
    return {"issue_count": len(issues), "details": issues}

if __name__ == "__main__":
    print(run_cppcheck("driver_from_model.c"))
