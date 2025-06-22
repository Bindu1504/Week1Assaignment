from string_utils import stringoper as ops
from string_utils import stringvalid as val

def main():
    test_string = input("Enter a string: ")

    print("\n--- String Operations ---")
    print("Reversed String:", ops.reverse_string(test_string))
    print("Uppercase String:", ops.to_uppercase(test_string))
    print("Length of String:", ops.string_length(test_string))

    print("\n--- String Validations ---")
    print("Is Palindrome?", "Yes" if val.is_palindrome(test_string) else "No")
    print("Contains Only Alphabetic Characters?", "Yes" if val.is_alpha(test_string) else "No")

if __name__ == "__main__":
    main()