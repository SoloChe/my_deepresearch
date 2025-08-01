# reference: https://github.com/bytedance/deer-flow/blob/main/src/tools/crawl.py
from ..crawler.crawler import Crawler
from .tool import Tool
import logging

logger = logging.getLogger(__name__)


class CrawlerTool(Tool):
    def __init__(self):
        super().__init__(
            "crawl",
            "Use this to crawl a url and get a readable content in markdown format.",
        )

    def __call__(self, url: str) -> str:
        """Use this to crawl a url and get a readable content in markdown format."""
        try:
            crawler = Crawler()
            article = crawler.crawl(url)
            return {"url": url, "crawled_content": article.to_markdown()[:1000]}
        except BaseException as e:
            error_msg = f"Failed to crawl. Error: {repr(e)}"
            logger.error(error_msg)
            return error_msg
