candidate_passwords = ['secure42', 'weak', 'P@ssword!', '123456789', 'SecurePass123']
for safe in candidate_passwords:
    if (len(safe) < 8) or safe.isnumeric():
        print("Password failed. Must be 8 characters or is purely numeric")
        continue
    elif (len(safe) >= 10) and safe[0].isupper():
        print("Password is strong. Meets security requirements")
    else:
        print("Password is acceptable. Meets basic requirements ")

