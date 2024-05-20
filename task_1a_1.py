#Please write a python program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Cricket","Ludo"].

subj=["I", "You"]
verb=["Play", "Love"]
obj=["Cricket", "Ludo"]
for s in subj:
    for v in verb:
        for o in obj:
            sentence = f"{s} {v} {o}."
            print(sentence)
