from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.litres.ru/")
        await page.screenshot(path="screenshots/FirstAsyncTest.png")
        await browser.close()

asyncio.run(main())