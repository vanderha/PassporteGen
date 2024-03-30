from django.shortcuts import render

# Create your views here.
import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters
    symbols = string.punctuation
    digits = string.digits

    # Ensure at least one capital letter and one symbol
    password = random.choice(letters.upper()) + random.choice(symbols) + random.choice(digits)

    # Fill the rest of the password with random characters
    password += ''.join(random.choice(letters + string.digits + symbols) for _ in range(length - 3))

    # Shuffle the password to make it less human-readable
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Example usage
#password_length = 12  # Change this to desired password length
#password = generate_password(password_length)
#print("Generated password:", password)

def generate_password_view(request):
    if request.method == 'POST':
        length = int(request.POST.get('length', 12))  # Default length is 12 if not specified
        password = generate_password(length)
        return render(request, 'password_generator.html', {'password': password})
    else:
        return render(request, 'password_generator.html')