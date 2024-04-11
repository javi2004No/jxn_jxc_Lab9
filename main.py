def encoder(password):
    """
    Encodes the password by adding 3 to the num. Written by Javier Noda
    :param password: The original password
    :return: Return the encoded password or an error if the number is not all numerical
    """
    newPassword = ""
    for num in password:
        newPassword += str((int(num) + 3) % 10)
    return newPassword


def main():
    """
    Menu for the encoder program written by Javier Noda.
    :return: Nothing
    """
    print("Password Encoder/Decoder ")
    print("Collaborators: Javier Noda, Jessica Chao")
    while True:
        # Repeating menu.
        print("\n1. Encode Password")
        print("2. Decode Password")
        print("3. Quit")
        answer = input("Type which option you choose: ")
        # If the answer is invalid in any way it will return invalid input.
        try:
            answer = int(answer)
            if answer == 1:
                answer = input("\nType in the password to encode: ")
                newPassword = encoder(answer)
                print("Encoded password is: ", newPassword)
            elif answer == 2:
                # Jessica this is where you would put your decoder function call replace the pass with it.
                pass
            elif answer == 3:
                break
            else:
                print("Error invalid input.")
        except:
            print("Error invalid input.")


if __name__ == "__main__":
    main()