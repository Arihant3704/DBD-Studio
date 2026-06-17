import os
import asyncio
from playwright.async_api import async_playwright
from PIL import Image
import re

async def capture_screenshots(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    async with async_playwright() as p:
        # Use the system's google-chrome to avoid downloads
        browser = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        # Create a page with 1280x720 viewport
        page = await browser.new_page(viewport={"width": 1280, "height": 720})
        
        # Get all html files and sort them numerically
        files = [f for f in os.listdir(input_dir) if f.endswith('.html')]
        def sort_key(f):
            num_match = re.search(r'(\d+)', f)
            return int(num_match.group(1)) if num_match else 0
            
        sorted_files = sorted(files, key=sort_key)
        
        screenshots = []
        for i, filename in enumerate(sorted_files):
            file_path = os.path.abspath(os.path.join(input_dir, filename))
            output_path = os.path.join(output_dir, f"slide_{i:03d}.png")
            
            print(f"Capturing {filename}...")
            # Use networkidle to wait for all assets (fonts, icons) to load
            await page.goto(f"file://{file_path}", wait_until="networkidle")
            # Extra wait just in case for complex animations
            await page.wait_for_timeout(1000) 
            
            # Instead of full_page=True which might add whitespace,
            # we capture the exact .slide-container element if possible
            slide_container = await page.query_selector('.slide-container')
            if slide_container:
                await slide_container.screenshot(path=output_path)
            else:
                # Fallback to normal screenshot if container not found
                await page.screenshot(path=output_path)
                
            screenshots.append(output_path)
            
        await browser.close()
    return screenshots

def create_pdf(image_paths, pdf_path):
    images = []
    for path in image_paths:
        img = Image.open(path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        images.append(img)
    
    if images:
        images[0].save(pdf_path, save_all=True, append_images=images[1:])
        print(f"PDF created at: {pdf_path}")
    else:
        print("No images found to create PDF.")

async def main():
    input_dir = "/home/arihant/Desktop/payu friend/DBD-Studio/DBD-Studio/ppt"
    temp_dir = "/home/arihant/Desktop/payu friend/DBD-Studio/DBD-Studio/temp_screenshots"
    pdf_path = "/home/arihant/Desktop/payu friend/DBD-Studio/DBD-Studio/presentation.pdf"
    
    # 1. Capture screenshots
    screenshot_paths = await capture_screenshots(input_dir, temp_dir)
    
    # 2. Create PDF
    create_pdf(screenshot_paths, pdf_path)
    
    # 3. Clean up
    for path in screenshot_paths:
        if os.path.exists(path):
            os.remove(path)
    if os.path.exists(temp_dir):
        os.rmdir(temp_dir)
    print("Cleanup completed.")

if __name__ == "__main__":
    asyncio.run(main())
