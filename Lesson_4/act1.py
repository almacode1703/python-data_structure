class Country:

    # Initializing (Constructor)
    def __init__(self):
        print("Country created.")

    # Deleting (Destructor)
    def __del__(self):
        print("Destructor called, Country deleted.")


# Creating object
obj = Country()

# Deleting object
del obj