def calculateDS():
    quiz = float(raw_input("quiz total: "))
    hw = float(raw_input("hw total: "))
    exam1 = float(raw_input("exam1 total: "))
    exam2 = float(raw_input("exam2 total: "))
    
    final = float(raw_input("final total: "))
    
    
    if final == 0:
        total = quiz+hw+exam1+exam2
        print total/70
    else:
        total = quiz+hw+exam1+exam2+final
        print total/100
    