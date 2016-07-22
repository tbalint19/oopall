class UserInterface():

    @classmethod
    def createPicture(cls):
        pixels = input("Set resolution: ")
        choice = input("\n(1) Black\n(2) White\n(3) Red\n(4) Blue")
        if choice == '1':
            color = "black"
        if choice == '2':
            color = "white"
        if choice == '3':
            color = "red"
        if choice == '3':
            color = "blue"

        return ("RGB", (pixels, pixels), color)