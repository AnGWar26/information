"""
Creates a graph of wikipedia pages

Andrew Warfield
"""

import queue
import wikipediaapi

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
        node_dict: dict
            key is page, value is tuple of all links on page
    """

    page_counts = {}
    pages_crawled = 0

    page_q = queue.Queue()
    page_q.put(starting_page)
    node_dict = {}

    while pages_crawled < num_pages_to_crawl and not page_q.empty():
        page = page_q.get()
        wiki_p = wiki.page(page)
        page_links = tuple(wiki_p.links.keys())
        node_dict[page] = page_links
        for link in page_links:
            page_q.put(link)
        pages_crawled += 1
        page_counts[page] = page_counts.get(page, 0) + 1

    return node_dict, page_counts
