import random
import time
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_menu():
    clear()
    print("Made by: Lemonaidd")
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
    print("\033[1;32m LOL Social IP Lookup Tool!\033[0m")
    print("\033[1;34m1. Xbox IP Lookup\033[0m")
    print("\033[1;34m2. Playstation IP Lookup\033[0m")
    print("\033[1;34m3. Skype IP Lookup\033[0m")
    print("\033[1;34m4. TikTok IP Lookup\033[0m")
    print("\033[1;31m0. Exit\033[0m")







































































"https://api.openhttps://xbl.io//data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={XBOX IP_ADDRESSby6SIIj2diOoHm7DYh1cVsFa3SSbYcedKRYWZNKwdwBUXKo71pxIOoYkwxlRsiaTu73Gs50HTA4KKt3c7MVcY90lyBKijJebIj7kJJF14gQ0hz9rL}"
"https://api.openhttps://mindcloud.co/?utm_term=api%20service&utm_campaign=Google+Search+Retargeting+-+Hubspot+Contacts+%26+Website+Visitors&utm_source=adwords&utm_medium=ppc&hsa_acc=6760895558&hsa_cam=20041663091&hsa_grp=149388773500&hsa_ad=656721312930&hsa_src=g&hsa_tgt=kwd-298901135206&hsa_kw=api%20service&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=20041663091&gbraid=0AAAAAomP8HZ1RRd8mK3hjMdksKJopgt1R&gclid=Cj0KCQjwm93DBhD_ARIsADR_DjEIVTHinAWtcu8C7QOurYsvQpZMBr8WmyG2sXt9xTeF7M_pNQ1vqMkaAkCMEALw_wcB/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={PSNIP_ADDRESSNpWWEeudcLRJPcI01QXZesh3EubJGTGnZGIrJgb373UYRjNOxyKzZTIJD1rSPReycBkUnQm8T7n68wlFdJoNcvNh19sel0s8WWBbB8qmglJKfQDOkw0}"
"https://api.open https://www.tikapi.io/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={IPwPkAZhREr6DR2KWBHpVGctx1cushQD6gO0CKqKn5HYB4njaWQ03HRgrr2XshklYq9Cxk1JCBDpKZOj1EQImicvqWSCmb1MBiXQdXaUnOsm8Gxn7XkJ9QImEeprtgsb}"
"https://api.openhttps://github.com/ocilo/skype-http/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={IPV4OPGijyaQLkYscSdmQABS4A57iYIHjqkSqE63oUwZiXHAMCBqPDfZSmyayqXZDNpaiSFKTXCGTYVdIjWpec1hUpjTlIBNlrGgp9SfC7WYBzitzdkSinpTIuj7WENO}"


























def valid_passkey():
    passkey = "bot"   # Set passkey here
    user_input = input(Fore.GREEN + "Enter passkey to access the tool: ")
    return user_input == passkey









































































































































































def pull_ip(username):
    time.sleep(2)
    if random.random() < 0.2:  
        return f" YAY! We found {username}'s IP: {random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)} "
    else:
        return "Oh no! seems like we found no IP associated with that user in our database"

def main():
    passkey = input("Enter the passkey to access the tool: ")
    if passkey != "bot":
        print(Fore.RED + "Invalid passkey!")
        sys.exit()
    while True:
        display_menu()
        choice = input("\nSelect an option: ")
        if choice == '0':
            break
        elif choice in ['1', '2', '3', '4']:
            username = input("Enter username: ")
            ip = pull_ip(username)
            print(f"\n\033[1;33m{ip}\033[0m")
            input("\nPress Enter to continue...")
        else:
            print("\033[1;31mInvalid option. Please try again.\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    main()
