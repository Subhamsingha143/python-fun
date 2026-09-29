question=[
    ["what is the capital city of india",["1.delhi","2.kolkata","3.bangalore"],1],
    ["what is 'python' in programming ?",["1.snake","2.language","3.game"],2],
    ["which language is called as 'mother of all language'?",["1.python","2.java","3.c language"],3],
    ["who is known as father of the computer",["1.charles babbage","2.bill gates","3.steve jobs"],1],
    ["which operating system is open source",["1.windows","2.linux","3.macOS"],2]
]
s=0
for i in range(5):
    q,option,answer=question[i]
    print(f"\nQ{i+1}.{q}")
    for opt in option:
        print(opt)
    ans=int(input("enter your choice: "))
    if not 1<=ans<=3:
     print("invalid choice..")
    elif ans==answer:
     print("answer is correct")
     s+=1
    else:
       print("wrong answer")

print(f"\nQuize is over!Total score {s}/5")
