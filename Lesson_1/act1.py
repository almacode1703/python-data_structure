from colorama import Fore, Style

lst = ["Apple", "Banana", "grapes", "oranges","jackfruit", "raspberry"]

print(f"Length of List : {Fore.GREEN}{len(lst)}{Style.RESET_ALL}")
print(f"First Element : {lst[0]}")
print(f"Last Element : {lst[-1]}")

lst.append("nuts")
print("Updated List : ", lst)

lst.remove("Banana")
print(f"Updated List :{Fore.CYAN}{lst}{Style.RESET_ALL}")

