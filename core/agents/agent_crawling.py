from playwright.sync_api import sync_playwright, Page


class AgentCrawling:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

    def fetch_page(self, url):
        context = self.browser.new_context(user_agent=self.agent, java_script_enabled=True)
        page = context.new_page()
        page.goto(url)
        return page

    def extract_url(self, page: Page):
        title = page.query_selector_all("h3")
        paragraphs = page.query_selector_all('[data-component="CardDescription"]')
        content = "\n".join([f"{paragraphs[i].inner_text().strip()}" for i in range(len(paragraphs))])
        return content

    def close(self):
        self.browser.close()
        self.playwright.stop()


if __name__ == "__main__":
    agent = AgentCrawling()
    page = agent.fetch_page("https://www.abc.net.au/news/justi")
    page_content = agent.extract_url(page)
    print(page_content)
    agent.close()
