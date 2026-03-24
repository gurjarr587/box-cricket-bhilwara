import subprocess

def generate_code(task):
    result = subprocess.run(
        ["claude", "-p", task],
        capture_output=True,
        text=True
    )
    return result.stdout

def save_file(code):
    with open("main.py", "w") as f:
        f.write(code)

if __name__ == "__main__":
    task = input("What to build: ")
    code = generate_code(task)

    print("\n=== GENERATED CODE PREVIEW ===\n")
    print(code[:500])

    save_file(code)

    print("\n✅ Code saved to main.py")
