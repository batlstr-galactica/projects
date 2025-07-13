
**dns-zone-xfer.py**
```python
import dns.query
import dns.zone

def attempt_axfr(domain):
    try:
        z = dns.zone.from_xfr(dns.query.xfr(domain, 'ns1.' + domain))
        for name in z.nodes.keys():
            print(z[name].to_text(name))
    except Exception as e:
        print(f"[!] Zone transfer failed for {domain}: {e}")

if __name__ == "__main__":
    with open('domains.txt') as f:
        domains = [line.strip() for line in f]
    for domain in domains:
        attempt_axfr(domain)
