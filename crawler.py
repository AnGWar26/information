"""
Creates a graph of wikipedia pages

Andrew Warfield
"""

import queue
import wikipediaapi
from page import Page

wiki = wikipediaapi.Wikipedia('en')

def crawl(starting_page, num_pages_to_crawl):
    """
    Crawls wikipedia pages, creating a Graph from Page()
    objects.
    Inputs:
        starting_page: str
            the name of the page to start the crawling on
        num_pages_to_crawl: int
            the number of pages to crawl
    Ouputs:
        start: Page()
            the Page() of the first crawled page
    """

    page_counts = {}
    pages_crawled = 0

    page_q = queue.Queue()
    start = Page(starting_page)
    page_q.put(start)

    while pages_crawled < num_pages_to_crawl and not page_q.empty():
        page = page_q.get()
        wiki_p = wiki.page(page.name)
        page_links = wiki_p.links
        for link in page_links:
            child_page = Page(link)
            page.children.append(child_page)
            page_q.put(child_page)
        pages_crawled += 1
        page_counts[page.name] = page_counts.get(page.name, 0) + 1

    return start, page_counts
