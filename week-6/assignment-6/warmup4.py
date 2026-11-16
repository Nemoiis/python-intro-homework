def is_valid_score(score):
    if score >= 0 and score <= 100:
        return True

    else:
        return False

testScore = int(input("Enter test score: "))

if is_valid_score(testScore):
    print("Valid Score")

else:
    print("Invalid Score - Must be between 0 and 100")