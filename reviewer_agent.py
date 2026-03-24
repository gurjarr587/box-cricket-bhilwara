import subprocess

def review_code():
    with open("main.py") as f:
        code = f.read()

    prompt = f"""
You are a strict code reviewer.

Check this FastAPI code.

Rules:
- If code is correct → return ONLY: APPROVE
- If issues exist → return ONLY: REJECT

Code:
{code}
"""

    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()

if __name__ == "__main__":
    decision = review_code()
    print("\n=== REVIEW RESULT ===\n")
    print(decision)
