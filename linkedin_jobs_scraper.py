from playwright.sync_api import sync_playwright
import pandas as pd

url = "https://www.linkedin.com/jobs/search/?currentJobId=4414745951&f_TPR=r86400&geoId=106155005&keywords=software%20engineer&sortBy=DD"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)
    page.wait_for_timeout(10000)

    # كل كروت الوظائف
    cards = page.locator(".base-search-card")

    job_titles = []
    company_name = []
    location = []
    job_urls = []
    posted_date = []

  
    for i in range(cards.count()):

        card = cards.nth(i)

        title = card.locator(".base-search-card__title").inner_text()
        company = card.locator(".base-search-card__subtitle").inner_text()
        job_location = card.locator(".job-search-card__location").inner_text()
        job_url = card.locator('a[href*="/jobs/view/"]').get_attribute("href")
        date = card.locator("time").inner_text()

        job_titles.append(title)
        company_name.append(company)
        location.append(job_location)
        job_urls.append(job_url)
        posted_date.append(date)


    job_descriptions = []
    job_criterias = []

    for job_url in job_urls:

        page.goto(job_url)
        page.wait_for_timeout(3000)

        job_description = page.locator(
            ".show-more-less-html__markup"
        ).all_inner_texts()

        job_criteria = page.locator(
            ".description__job-criteria-text.description__job-criteria-text--criteria"
        ).all_inner_texts()

        job_descriptions.append(job_description)
        job_criterias.append(job_criteria)


   
    print("Titles:", len(job_titles))
    print("Companies:", len(company_name))
    print("Locations:", len(location))
    print("URLs:", len(job_urls))
    print("Posted dates:", len(posted_date))
    print("Descriptions:", len(job_descriptions))
    print("Criteria:", len(job_criterias))


    
    df = pd.DataFrame({
        "job_title": job_titles,
        "company_name": company_name,
        "location": location,
        "job_url": job_urls,
        "posted_date": posted_date,
        "job_description": job_descriptions,
        "job_criteria": job_criterias
    })


   
    print(df)


  
    df.to_csv("linkedin_jobs.csv", index=False)

    print("CSV saved successfully")
