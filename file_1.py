import requests
from bs4 import BeautifulSoup
import os

os.makedirs("tech_data", exist_ok=True)

companies = [
"Apple Inc.",
"Microsoft",
"Google",
"Amazon (company)",
"Meta Platforms",
"Tesla, Inc.",
"IBM",
"Intel",
"NVIDIA",
"Oracle Corporation",
"Samsung Electronics",
"Sony",
"Dell Technologies",
"HP Inc.",
"Cisco Systems",
"Adobe Inc.",
"Salesforce",
"Uber",
"Airbnb",
"Netflix",
"Spotify",
"PayPal",
"Xiaomi",
"Huawei",
"Lenovo",
"ASUS",
"Acer Inc.",
"LG Electronics",
"Tencent",
"ByteDance",
"Baidu",
"Alibaba Group",
"Zoom Video Communications",
"Snap Inc.",
"Qualcomm",
"Nvidia Corporation",
"Dropbox",
"Slack Technologies",
"Shopify",
"Red Hat",
"Stripe",
"GitHub",
"Atlassian",
"VMware",
"ServiceNow",
"Twilio",
"SpaceX",
"Palantir Technologies",
"Electronic Arts",
"Nintendo",
"Red Hat",
"Pinterest",
"Yandex",
"X Corp (Twitter)",
"Salesforce",
"LinkedIn",
"Epic Games",
"Valve Corporation",
"IBM Watson",
"Oracle Cloud",
"Databricks",
"Snowflake Inc.",
"Unity Technologies",
"Razer Inc.",
"GoDaddy",
"DigitalOcean",
"Cloudflare",
"Elastic N.V.",
"GitLab",
"Autodesk",
"Intuit",
"ZoomInfo",
"RingCentral",
"Okta",
"Fortinet",
"Zscaler",
"Nokia",
"Ericsson",
"BlackBerry",
"Alibaba Cloud"
]
headers = {
    "User-Agent": "Mozilla/5.0"
}

for company in companies:
    print("Scraping:", company)

    url = "https://en.wikipedia.org/wiki/" + company.replace(" ", "_")

    try:
        r = requests.get(url, headers=headers)

        if r.status_code != 200:
            print("❌ Page not found")
            continue

        soup = BeautifulSoup(r.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = ""
        for p in paragraphs:
            if p.text.strip():
                text = p.text.strip()
                break

        if text == "":
            print("❌ No content")
            continue

        filename = company.replace(" ", "_").replace(",", "") + ".txt"

        with open(f"tech_data/{filename}", "w", encoding="utf-8") as f:
            f.write(text)

        print("✔ Saved")

    except Exception as e:
        print("❌ Error:", e)