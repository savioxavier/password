# Savio Xavier

encoded_password = None


def encode(password):
    global encoded_password

    password_list = [int(x) for x in password]
    return int("".join(str(i) for i in map(lambda x: abs(x + 3), password_list)))


def decode(encoded_password):
    decoded = ""
    for char in str(encoded_password):
        # Reverse the shift of digit by 3, use modulo to wrap around
        new_digit = (int(char) - 3) % 10
        decoded += str(new_digit)
    return decoded


def main():
    while True:
        print(
            """Menu
-------------
1. Encode
2. Decode
3. Quit
"""
        )

        choice = int(input("Please enter an option: "))

        if choice == 1:
            p = input("Please enter your password to encode: ")
            try:
                encoded_password = encode(password=p)

                print("Your password has been encoded and stored!")
            except Exception as e:
                print(e)

        elif choice == 2:
            decoded_password = decode(encoded_password=encoded_password)
            print(
                f"The encoded password is {encoded_password}, and the original password is {decoded_password}."
            )

        elif choice == 3:
            break


if __name__ == "__main__":
    main()
