import random
import time
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_menu():
    clear()
    print(r"""
██╗      ██████╗ ██╗             
██║     ██╔═══██╗██║             
██║     ██║   ██║██║             
██║     ██║   ██║██║             
███████╗╚██████╔╝███████╗        
╚══════╝ ╚═════╝ ╚══════╝        
                                 
██████╗ ██╗   ██╗██╗     ██╗     
██╔══██╗██║   ██║██║     ██║     
██████╔╝██║   ██║██║     ██║     
██╔═══╝ ██║   ██║██║     ██║     
██║     ╚██████╔╝███████╗███████╗
╚═╝      ╚═════╝ ╚══════╝╚══════╝
    """)
    print("\033[1;32mBufferOverflow  Pull Tool!\033[0m")
    print("\033[1;34m1. Discord IP Puller\033[0m")
    print("\033[1;34m2. Xbox IP Puller\033[0m")
    print("\033[1;34m3. Playstation IP Puller\033[0m")
    print("\033[1;34m4. InstaGram IP Puller\033[0m")
    print("\033[1;34m5. TikTok IP Puller\033[0m")
    print("\033[1;34m6. Snapchat IP Puller\033[0m")
    print("\033[1;31m0. Exit\033[0m")









































































































































































































































































def pull_ip(username):
    time.sleep(2)
    if random.random() < 0.4:  # 40% chance to "find" an IP
        return f"{username}'s IP: {random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    else:
        return "IP not found."

def main():
    while True:
        display_menu()
        choice = input("\nSelect an option: ")
        if choice == '0':
            break
        elif choice in ['1', '2', '3', '4','5','6']:
            username = input("Enter username: ")
            ip = pull_ip(username)
            print(f"\n\033[1;33m{ip}\033[0m")
            input("\nPress Enter to continue...")
        else:
            print("\033[1;31mInvalid option. Please try again.\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    main()
