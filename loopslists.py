def listloop(threshold):
    inp = []
    while True:
        # try/except for when the number isn't a float or an int
        try:
            num = float(input("Please enter a number: "))
            inp.append(num)
            if num < 0:
                break
        except:
            print("That is not a valid number! ")
    # if not above the threshold, doesn't getting appended
    reached = [x for x in inp if x > threshold]
    return(sum(reached)/len(reached))

