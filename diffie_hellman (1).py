def diffie_hellman():
    p = int(input("Enter prime number p: "))
    g = int(input("Enter primitive root g: "))

    a = int(input("Enter Alice private key: "))
    b = int(input("Enter Bob private key: "))

    print("Public prime (p):", p)
    print("Public base (g):", g)

    A = pow(g, a, p)
    B = pow(g, b, p)

    print("Alice sends:", A)
    print("Bob sends:", B)

    secret_A = pow(B, a, p)
    secret_B = pow(A, b, p)

    print("Alice's secret:", secret_A)
    print("Bob's secret:", secret_B)

    if secret_A == secret_B:
        print("Shared key established successfully!")
    else:
        print("Key exchange failed!")


diffie_hellman()
