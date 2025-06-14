import argparse
from src.whois_lookup import whois_lookup

def main():
    parser = argparse.ArgumentParser(description="Recon & Enumeration Toolkit")
    parser.add_argument('--whois', help='Perform WHOIS lookup on a domain')

    args = parser.parse_args()

    if args.whois:
        result = whois_lookup(args.whois)
        print(result)

if __name__ == '__main__':
    main()
