import random
import string

def generate_password(length):
    """
    Generate a random password of the specified length using a mix of characters.
    
    Parameters:
    - length (int): The desired length of the password.
    
    Returns:
    - str: The generated password.
    """
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Main Program
if __name__ == "__main__":
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length must be a Positive integer.")
        
        password = generate_password(length)
        
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")