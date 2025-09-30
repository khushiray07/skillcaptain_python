import random

syllables = ["ka","mi","ra","lo","na","zi","tu","ve","shi","dra",
             "li","tor","fen","bel","zar","qu","ya","ru","sa","mo"]

n = int(input("How many names to generate? "))
names = set()
while len(names) < n:
    name = "".join(random.choice(syllables) for _ in range(3)).capitalize()
    names.add(name)
with open("character_names.txt", "w") as f:
    f.write("\n".join(sorted(names)))

print(" Done! Names saved to character_names.txt")