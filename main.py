"""The Meeting That Should Have Been an Email — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: an email cannot sigh — the meeting exists so people can be heard sighing live.
TEXT = "This meeting could have been an email, but then nobody would have heard me sigh in real time."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
