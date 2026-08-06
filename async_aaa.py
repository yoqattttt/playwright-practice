from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://lavk.yandex.ru/")
        await page.screenshot(path="FirstAsyncTest.png")
        await browser.close()

asyncio.run(main())