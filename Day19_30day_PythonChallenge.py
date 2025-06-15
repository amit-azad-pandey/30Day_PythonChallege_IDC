import threading 
import requests

file_urls = ['https://example.com/file1.jpg',
             'https://example.com/file2.jpg',
             'https://example.com/file3.jpg']


def download_file(url):
    local_filename = url.split('/')[-1] 
    print(f"starting download: {local_filename}") 
    response = requests.get(url)
    with open(local_filename, 'wb') as f: 
        f.write(response.content)
    print(f"Finished download: {local_filename}")

threads = []
for url in file_urls:
    t = threading.Thread (target=download_file, args=(url,)) 
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print("All downloads completed!")