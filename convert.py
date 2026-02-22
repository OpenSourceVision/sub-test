import subprocess
import os
import sys

def test_url(url):
    result = subprocess.run(
        ['curl', '-sL', '-o', '/dev/null', '-w', '%{http_code}', '--connect-timeout', '5', '--max-time', '10', url],
        capture_output=True, text=True
    )
    status = result.stdout.strip()
    if status and int(status) < 400:
        return True, status
    return False, status

with open('url.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

urls = []
for line in lines:
    url = line.lstrip('-').strip().strip('"').strip("'")
    if url:
        urls.append(url)

original = len(urls)
unique_urls = list(dict.fromkeys(urls))
dedup_count = len(unique_urls)

valid_urls = []
failed = 0
total = len(unique_urls)

for i, url in enumerate(unique_urls):
    print(f"[{i+1}/{total}] Testing: {url[:60]}...", end=" ")
    success, status = test_url(url)
    if success:
        valid_urls.append(url)
        print(f"OK (HTTP {status})")
    else:
        failed += 1
        print(f"FAIL (HTTP {status})")

with open('out.txt', 'w') as f:
    for url in valid_urls:
        f.write(f'{url}\n')

with open('log.txt', 'w') as f:
    f.write(f"原始网址: {original}\n")
    f.write(f"去重数量: {dedup_count}\n")
    f.write(f"有效数量: {len(valid_urls)}\n")
    f.write(f"无效数量: {failed}\n")

print(f"\n原始: {original}, 去重: {dedup_count}, 有效: {len(valid_urls)}, 无效: {failed}")
