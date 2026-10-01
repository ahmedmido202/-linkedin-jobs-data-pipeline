# -linkedin-jobs-data-pipeline
    Data collection pipeline for extracting, cleaning, and structuring LinkedIn job postings using Python and Playwright
# LinkedIn Jobs Data Pipeline

This project collects job postings from LinkedIn using Python and Playwright.

I built the scraper to collect job data for different technical roles and locations. The project collected more than 10,000 job postings.

## Data Collected

For each job posting, the scraper collects:

- Job title
- Company name
- Location
- Job description
- Job URL
- Job details and requirements

## How It Works

The script uses Playwright to automate the browser, load LinkedIn job search pages, collect job links, and visit individual job pages to extract the required information.

The collected data is stored in CSV format so it can be cleaned and used later for data analysis or data engineering projects.

## Tools

- Python
- Playwright
- Pandas
- CSV

## Project Files

- `linkedin_jobs_scraper.py` - LinkedIn scraping script
- `README.md` - Project documentation

## Result

More than 10,000 LinkedIn job postings were collected using the scraper.
