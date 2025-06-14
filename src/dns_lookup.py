import subprocess

def dns_lookup(domain):
    try:
        result = subprocess.check_output(['nslookup', domain], stderr=subprocess.DEVNULL, text=True)
        return result
    except Exception as e:
        return f"[!] Error: {e}"
