# telegram: @kirito340866
import requests
import json
from bs4 import BeautifulSoup
def taking_target_data(target_url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(target_url, headers=headers)
    soup = BeautifulSoup(response.text,'html.parser')
    data_box = soup.find_all('script')
    target_data = None
    for data in data_box:
        if data.string and "var data =" in data.string:
            target_data = data.string
            break
    return target_data
def making_clean_data(target_data):
    if target_data:
        raw_json = target_data.split("var data =")[1]
        raw_json = raw_json.split("];")[0] + "]"
        clean_data = json.loads(raw_json.strip())
        return clean_data
def handling_json_data(clean_data):
    all_data = []
    if clean_data:
        number = 1
        for q in clean_data:
            datas = {
                "Number":number,
                "Author_Name": q['author']['name'],
                "Text":q['text']
            }
            all_data.append(datas)
            number += 1
    return all_data
def saving_as_json(all_data):
    with open("Json.json","w",encoding="utf-8") as file:
        json.dump(all_data,file,ensure_ascii=False,indent=4)
    print(f"+ Saved {len(all_data)} Datas at Json.json")
if __name__ == "__main__":
    url = "https://quotes.toscrape.com/js/"
    print(f"[*] Taking Datas from {url}...")
    targetData = taking_target_data(url)
    cleanData = making_clean_data(targetData)
    allData = handling_json_data(cleanData)
    saving_as_json(allData)
