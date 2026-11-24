import os

TEXT = "ERROR: Your bread has left the toaster. It is now legally a crouton."

def main():
    assert 1 <= len(TEXT) <= 120, "entry must be 1-120 characters"
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
