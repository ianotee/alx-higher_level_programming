#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the names."""
    import hidden_4

    naun = dir(hidden_4)
    for naun in names:
        if naun[:2] != "__":
            print(naun)
