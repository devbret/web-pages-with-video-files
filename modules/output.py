def save_links_as_txt(links, filename: str = 'links.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')
