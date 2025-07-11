import requests
from bs4 import BeautifulSoup

def crawl_chinadaily_tech():
    url = 'https://www.chinadaily.com.cn/business/tech'
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; WebScraper/1.0)'
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 保证中文编码正确
    if response.status_code != 200:
        print("Failed to retrieve page:", response.status_code)
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    results = []

    for span in soup.find_all('span', class_='tw3_01_2_t'):
        h4 = span.find('h4')
        a_tag = h4.find('a') if h4 else None
        b_tag = span.find('b')

        if a_tag and b_tag:
            title = a_tag.get_text(strip=True)
            publish_time = b_tag.get_text(strip=True)
            results.append({
                'title': title,
                'publishTime': publish_time
            })

    return results


# 示例调用
if __name__ == '__main__':
    articles = crawl_chinadaily_tech()
    for article in articles:
        print(f"Title: {article['title']}, Publish Time: {article['publishTime']}")
