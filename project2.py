def factorial():
    math = input()

    factorailSetings = None
    time = None
    forQB = None

    if math == "!":
        try:




            factorailSetings = int(input())
            time = factorailSetings -1
            forQB = factorailSetings

        except:
            print("you need a number")

        while time != 0 and forQB != 0:

            if time == 1:

                print(forQB * (factorailSetings - 1))

            forQB = forQB * (factorailSetings - 1)

            factorailSetings = factorailSetings - 1

            time = time - 1


factorial()
