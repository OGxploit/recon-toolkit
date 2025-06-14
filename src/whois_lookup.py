import subprocess

def whois_lookup(domain):
    try:
        result = subprocess.check_output(['whois', domain], stderr=subprocess.DEVNULL, text=True)
        return result
    except Exception as e:
        return f"[!] Error: {e}"
