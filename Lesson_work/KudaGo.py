url = 'https://kudago.com/msk/entertainment/stand-up/'

    resp = get(url)
    text = resp.text
    # print(resp.status_code)
    # with open("kudago.html", "w", encoding="utf-8") as f:
    #     f.write(resp.text)

    soup = bs.BeautifulSoup(text, "lxml")

    feed_child = soup.find("div", class_="feed-child")
    post_title_link = feed_child.find_all("a", class_="post-title-link")
    urls = [a["href"] for a in post_title_link]
    print(len(post_title_link))
    print(*urls, sep="\n")