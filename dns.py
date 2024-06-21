import whois
import os 

def get_domain_info(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        return domain_info
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    domain_name = "rollexdigital.cloud"
    domain_info = get_domain_info(domain_name)
    if isinstance(domain_info, str):
        print(domain_info)
    else:
        for key, value in domain_info.items():
            print(f"{key}: {value}")

