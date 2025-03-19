ProductDict = {}

# Function to add Product
def addProduct():
    ProductName = input("Enter Product Name: ")
    ProductPrice = input("Enter Product Price: ")
    ProductDict[ProductName] = ProductPrice

# Function to display Product
def DisplayPrize(ProductName):
    for Product in ProductDict:
        if Product == ProductName:
            print("The price of "+Product+" is "+ProductDict[Product] + " $")
        else:
            print("Product Not Found")

print("\n*********************************************************")
print("Welcome to the Product Management System")

# Menu Driven Program
while True:
    print("1. Add Product")
    print("2. Exit")

    Choice = input("Enter Your Choice: ")

    if Choice == "1":
        addProduct()
    elif Choice == "2":
        break
    else:   
        print("Invalid Choice")

    print("*********************************************************")

# Display Product
while True:

    print("_________________________________________________________\n")
    ProductName = input("Enter Product Name to display price: ")
    DisplayPrize(ProductName)
    Continue = input("Do you want to continue (Y/N)? :")
    if Continue == "N":
        break
    elif Continue == "Y":
        continue
    else:
        print("Invalid Choice")
        break

print("Thank You for using the Product Management System")