import json
import time

import bs4.element as bs4
import requests as rq
from bs4 import BeautifulSoup


def get_manga_title(finished_manga):
    finished_manga_titles = []
    for read_manga in finished_manga.values():
        if isinstance(read_manga, dict):
            finished_manga_title = read_manga.get("title")
            if finished_manga_title:
                replace_strs = {"â€™": "'", "â€“": "–"}
                for old_str, new_str in replace_strs.items():
                    finished_manga_title = finished_manga_title.replace(
                        old_str, new_str
                    )
                kissmanga = finished_manga_title.find("Kissmanga")
                kumascans = finished_manga_title.find("Kuma Translation")
                if kissmanga != -1:
                    finished_manga_titles.append(finished_manga_title[: kissmanga - 3])
                elif kumascans != -1:
                    finished_manga_titles.append(finished_manga_title[: kumascans - 3])
    return finished_manga_titles


def read_or_write_json(file: str, fmode: str, outfile: dict = {}, indent: int = None):
    if fmode == "r":
        with open(file, fmode) as f:
            I_json = json.load(f)
        return I_json
    elif fmode == "w":
        with open(file, fmode) as f:
            json.dump(outfile, f, indent=indent)
    elif fmode == "a":
        with open(file, fmode) as f:
            json.dump(outfile, f, indent=indent)


def traverse_html_tree(html, tag, attrs: dict = {}, index: int = None):
    parent = html.find_all(tag, attrs=attrs)
    if index:
        parent = html.find_all(tag, attrs=attrs)[index]
    return parent


def request_and_parse(url):
    html = rq.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    return soup


def main():
    url = "https://kumascans.com"
    outfile = []
    checked_manga = None
    while True:
        try:
            checked_manga = read_or_write_json("read_manga.json", "r")
            if checked_manga:
                outfile = checked_manga
        except FileNotFoundError as e:
            pass
        finished_manga = read_or_write_json("readinglist.json", "r")
        finished_manga_title_list = get_manga_title(finished_manga)
        for x in range(1, 6):
            x += 1
            soup = request_and_parse(url)
            latest_manga_list = traverse_html_tree(
                soup, "div", {"class": "listupd"}, index=2
            )
            content = (
                new_manga
                for new_manga in latest_manga_list.children
                if not isinstance(new_manga, bs4.NavigableString) and new_manga != "\n"
            )
            for manga in content:
                new_manga_releases = manga.find("div", attrs={"class": "tt"})
                if new_manga_releases:
                    new_manga_releases_title = new_manga_releases.contents[0].strip()
                    if new_manga_releases_title in finished_manga_title_list:
                        link_to_manga_read = manga.find("a").get("href")
                        soup_read_manga = request_and_parse(link_to_manga_read)
                        new_chapters_list = traverse_html_tree(
                            soup_read_manga, "span", {"class": "chapternum"}
                        )
                        chapters = [
                            chapter.contents[0] for chapter in new_chapters_list
                        ]
                        outfile_new_manga = {
                            "title": new_manga_releases_title,
                            "chapter_lists": chapters,
                        }
                        if outfile_new_manga in outfile:
                            index_new_release = outfile.index(outfile_new_manga)
                            outfile_indexed = outfile[index_new_release]
                            len_outfile, len_outfile_new_manga = len(
                                outfile_indexed.get("chapter_lists")
                            ), len(outfile_new_manga.get("chapter_lists"))
                            if len_outfile_new_manga > len_outfile:
                                outfile_indexed = outfile_new_manga
                        else:
                            outfile.append(outfile_new_manga)
            url = f"https://kumascans.com/page/{x}"
        read_or_write_json("read_manga.json", "w", outfile, indent=4)
        print("now waiting")
        time.sleep(3600)


if __name__ == "__main__":
    main()
