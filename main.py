import argparse
from src.whois_lookup import whois_lookup
from src.dns_lookup import dns_lookup
from src.nmap_scan import nmap_scan

def main():
    parser = argparse.ArgumentParser(description="Recon & Enumeration Toolkit")
    parser.add_argument('--whois', help='Perform WHOIS lookup on a domain')
    parser.add_argument('--dns', help='Perform DNS lookup on a domain')
    parser.add_argument('--nmap', help='Perform Nmap scan on a target')

    args = parser.parse_args()

    if args.whois:
        print(whois_lookup(args.whois))

    if args.dns:
        print(dns_lookup(args.dns))

    if args.nmap:
        print(nmap_scan(args.nmap))

if __name__ == '__main__':
    main()
