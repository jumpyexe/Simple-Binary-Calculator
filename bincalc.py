# attempt at making a binary calc for ipv4 addresses

IP = input("What is the IPV4 Address? ")

IP_octs = IP.split(".")
bin_ip = [format(int(octet), '08b') for octet in IP_octs]

print(f"Your IP in Binary is {bin_ip}.")
