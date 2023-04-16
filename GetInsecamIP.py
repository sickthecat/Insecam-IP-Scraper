import re
import urllib.request

# Define constants
FILENAME = "IP.txt"
REGEX = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})")
URL_TEMPLATE = "http://www.insecam.org/en/bytype/Foscam/?page={}"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

def scrape_ips(url):
    """Scrapes the IP addresses from a given URL."""
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    ip_list = REGEX.findall(html)
    return ip_list

def write_to_file(ip_list):
    """Writes a list of IP addresses to a file."""
    with open(FILENAME, "a") as f:
        for ip, port in ip_list:
            f.write(f"{ip}:{port}\n")

def main():
    """Main function."""
    for i in range(1, 55):
        url = URL_TEMPLATE.format(i)
        ip_list = scrape_ips(url)
        if ip_list:
            print(f"Found {len(ip_list)} IPs on page {i}")
            write_to_file(ip_list)
        else:
            print(f"No IPs found on page {i}")

if __name__ == '__main__':
    main()
