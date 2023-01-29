import requests
import string, sys, time, random
from datetime import datetime
from pystyle import Colors, Center, Colorate



banner = Center.XCenter("""
             
██╗███╗   ██╗██╗   ██╗ ██████╗ ███████╗███╗   ██╗
██║████╗  ██║██║   ██║██╔════╝ ██╔════╝████╗  ██║
██║██╔██╗ ██║██║   ██║██║  ███╗█████╗  ██╔██╗ ██║
██║██║╚██╗██║╚██╗ ██╔╝██║   ██║██╔══╝  ██║╚██╗██║
██║██║ ╚████║ ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║
╚═╝╚═╝  ╚═══╝  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                    
Made by WebUwU :3 |  join server discord.gg/boobss\n\n
""")


while True:
    print(Colorate.Vertical(Colors.red_to_purple, banner, 2))

    print(Colorate.Color(Colors.purple, '', False))
    print("1. Discord Server Invite Gen     | 1")
    print("2. Discord Server Invite Checker | 2")
    print("3. Proxy Checker                 | 3")
    print("4. Exit                          | 4")

    print(Colorate.Color(Colors.red, '', False))
    choice = input("Enter your choice: ")
    
    if choice == "1":
        num_codes = int(input("How many codes would you like to generate? "))
        with open("codes.txt", "w") as f:
            for i in range(num_codes):
                code_length = random.choice([7, 8, 10])
                code = ''.join(random.choices(string.ascii_letters + string.digits, k=code_length))
                f.write("https://discord.gg/" + code + "\n")
        print(f"{num_codes} codes have been generated and saved to codes.txt.")

    elif choice == "2":
        use_proxy = input("Do you want to use a proxy? (y/n) ")
        if use_proxy == "y":
            with open("proxy.txt", "r") as proxy_file:
                proxies = proxy_file.readlines()
            with open("codes.txt", "r") as input_file, open("valid.txt", "w") as output_file:
                for line in input_file:
                    invite_code = line.strip()
                    url = f"https://discord.com/api/invites/{invite_code}"
                    for proxy in proxies:
                        try:
                            response = requests.get(url, proxies={"http": proxy, "https": proxy})
                            if response.status_code == 200:
                                output_file.write(invite_code + "\n")
                                break
                        except requests.exceptions.HTTPError as err:
                            print(err)
                            continue
        else:
            with open("codes.txt", "r") as input_file, open("valid.txt", "w") as output_file:
                for line in input_file:
                    invite_code = line.strip()
                    url = f"https://discord.com/api/invites/{invite_code}"
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            output_file.write(invite_code + "\n")
                    except requests.exceptions.HTTPError as err:
                        print(err)
    
    elif choice == "3":
     target_url = 'https://www.discord.com'

    # The list of proxies to check
    proxies = []
    with open('proxy.txt', 'r') as f:
        for line in f:
            proxies.append(line.strip())

    good_proxies = []
    for proxy in proxies:
        try:
            start = datetime.now()
            response = requests.get(target_url, proxies={'http': proxy, 'https': proxy}, timeout=5)
            end = datetime.now()
            response_time = (end - start).microseconds / 1000
            if response.status_code == 200 and response_time < 200:
                print(f'Proxy {proxy} is working with a response time of {response_time} ms.')
                good_proxies.append(proxy)
            else:
                print(f'Proxy {proxy} is NOT working.')
        except:
            print(f'Proxy {proxy} is NOT working.')

    # Save the good proxies to the same file
    with open('proxy.txt', 'w') as f:
        for proxy in good_proxies:
            f.write(proxy + '\n')



if choice == "4":
    print("Exiting...")
    sys.exit()
else:
    print("Invalid choice. Please try again.")

