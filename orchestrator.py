import subprocess

def run_builder():
    subprocess.run(["python", "builder_agent.py"])

def run_reviewer():
    result = subprocess.run(
        ["python", "reviewer_agent.py"],
        capture_output=True,
        text=True
    )
    return result.stdout

def git_push():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Approved by Reviewer"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    print("🚀 Starting AI Agent Pipeline...\n")

    run_builder()

    decision = run_reviewer()

    print("\n=== FINAL DECISION ===\n")
    print(decision)

    if "APPROVE" in decision:
        git_push()
        print("\n✅ Code approved and pushed to GitHub 🚀")
    else:
        print("\n❌ Code rejected — fix needed")
