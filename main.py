from interface import Statement

def main():
    result = []
    with open("dialog.tab", "r") as f:
        content = f.readlines()
    for c in content[1:]:
        s = Statement(c)
        result.append(f"{s.character} {s.dialogue}")
    return "".join(result)

if __name__ == "__main__":
    main()
