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

def git_push():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "AgentR update"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    task = input("What to build: ")
    code = generate_code(task)
    
    print("\nGenerated Code:\n", code[:500])  # preview
    
    save_file(code)
    git_push()
    
    print("✅ Code generated + pushed")
