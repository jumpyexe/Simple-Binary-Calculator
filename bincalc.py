# attempt at making a binary calc for ipv4 addresses

"""Simple IPv4 binary calculator."""

def validate_ipv4(ip: str) -> list[int]:
    """Validate and return a list of four integer octets.

    Raises ValueError if the input is not a valid IPv4 address.
    """

    parts = ip.strip().split(".")
    if len(parts) != 4:
        raise ValueError("IPv4 address must have four octets")

    octets = []
    for part in parts:
        if not part.isdigit():
            raise ValueError(f"Invalid octet: {part}")
        num = int(part)
        if not 0 <= num <= 255:
            raise ValueError(f"Octet out of range: {part}")
        octets.append(num)

    return octets


def main() -> None:
    ip = input("What is the IPV4 Address? ")
    try:
        octets = validate_ipv4(ip)
    except ValueError as exc:
        print(f"Error: {exc}")
        return

    bin_ip = ".".join(format(octet, "08b") for octet in octets)
    print(f"Your IP in Binary is {bin_ip}.")


if __name__ == "__main__":
    main()
