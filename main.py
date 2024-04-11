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


def decoder(encoded):
    decoded_password = ''.join(str((int(digit) - 3 + 10) % 10) for digit in encoded)
    return decoded_password
# Jess created the decoder function that will decode the encode given back to its original password


def main():
    """
    Menu for the encoder program written by Javier Noda.
    :return: Nothing
    """
    encoded_password = ""
    while True:
        # Repeating menu.
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        answer = input("\nPlease enter an option: ")
        # If the answer is invalid in any way it will return invalid input.
        try:
            answer = int(answer)
            if answer == 1:
                answer = input("Please enter your password to encode: ")
                encoded_password = encoder(answer)
                print("Your password has been encoded and stored!")
            elif answer == 2:
                decoded_password = decoder(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
                # Jess-applied the decoder function in choice 2 when selected and will print both the encoded password and the decoded password

            elif answer == 3:
                break
            else:
                print("Error invalid input.")
        except:
            print("Error invalid input.")


if __name__ == "__main__":
    main()
