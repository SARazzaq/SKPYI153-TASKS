subj=["I", "You"]
verb=["Play", "Love"]
obj=["Cricket", "Ludo"]


for s in subj:
    for v in verb:
        for o in obj:
            sentence = f"{s} {v} {o}."
            print(sentence)
