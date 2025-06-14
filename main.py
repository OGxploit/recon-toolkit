import argparse
from src.whois_lookup import whois_lookup
from src.dns_lookup import dns_lookup

def main():
    parser = argparse.ArgumentParser(description="Recon & Enumeration Toolkit")
    parser.add_argument('--whois', help='Perform WHOIS lookup on a domain')
    parser.add_argument('--dns', help='Perform DNS lookup on a domain')

    args = parser.parse_args()

    if args.whois:
        result = whois_lookup(args.whois)
        print(result)

    if args.dns:
        result = dns_lookup(args.dns)
        print(result)

if __name__ == '__main__':
    main()
