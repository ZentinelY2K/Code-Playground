# Artistic DNA Helix — Compact & Styled

pairs = ["A-T", "T-A", "C-G", "G-C", "T-A", "A-T", "G-C", "C-G"]
twist = [
    "        {0}       ",
    "       / \\      ",
    "      /   \\     ",
    "     /     \\    ",
    "====/=======\\===",
    "    \\       /   ",
    "     \\     /    ",
    "      \\   /     ",
    "       \\ /      ",
    "        {1}       "
]

def render_helix(pairs, twist):
    for i in range(len(twist)):
        line = ""
        for p in pairs:
            left, right = p.split("-")
            segment = twist[i].format(left, right)
            line += segment + "  "
        print(line)

render_helix(pairs, twist)









