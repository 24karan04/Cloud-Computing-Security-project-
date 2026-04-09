import os

RULE_FILE = "data/firewall_rules.txt"

def block_ip(ip):
    os.makedirs("data", exist_ok=True)
    with open(RULE_FILE, "a") as f:
        f.write(ip + "\n")
    return "IP blocked"

def allow_ip(ip):
    try:
        with open(RULE_FILE, "r") as f:
            ips = f.readlines()

        with open(RULE_FILE, "w") as f:
            for i in ips:
                if i.strip() != ip:
                    f.write(i)

        return "IP allowed"
    except:
        return "Firewall rule file missing"

def check_ip(ip):
    try:
        with open(RULE_FILE, "r") as f:
            ips = f.readlines()

        if ip + "\n" in ips:
            return "Access Denied"
        else:
            return "Access Allowed"
    except:
        return "Firewall rule file missing"
