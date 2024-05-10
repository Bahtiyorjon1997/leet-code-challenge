def countSegments(s: str) -> int:
    if len(s.strip()) == 0:
        return 0
    else:
        return len(s.strip().split(" ")) - s.strip().split(" ").count("")


print(countSegments(", , , ,        a, eaefa"))
