subjects=["matematias","español","quimica","ingles"]
scores=[]
for subjects in subjects:
    scores= input("que nota has sacado" + subjects + "?")
    scores.append(scores)
for i in range (len(subjects)):
    print("en" + subjects[i] + "has sacado" + scores[i])