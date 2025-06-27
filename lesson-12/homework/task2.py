import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    application_link TEXT,
    UNIQUE(title, company, location)
)
''')
conn.commit()

def scrape_jobs():
    url = 'https://realpython.github.io/fake-jobs'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = soup.find_all('div', class_='card-content')

    for job in jobs:
        title = job.find('h2', class_='title').text.strip()
        company = job.find('h3', class_='subtitle').text.strip()
        location = job.find('p', class_='location').text.strip()
        description = job.find('div', class_='content').text.strip()
        application_link = job.find('a', text='Apply')['href']

        cursor.execute('''
            SELECT description, application_link FROM jobs
            WHERE title = ? AND company = ? AND location = ?
        ''', (title, company, location))
        existing_job = cursor.fetchone()

        if existing_job:
            if existing_job[0] != description or existing_job[1] != application_link:
                cursor.execute('''
                    UPDATE jobs
                    SET description = ?, application_link = ?
                    WHERE title = ? AND company = ? AND location = ?
                ''', (description, application_link, title, company, location))
        else:
            cursor.execute('''
                INSERT OR IGNORE INTO jobs (title, company, location, description, application_link)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, company, location, description, application_link))

    conn.commit()
    print("Ma'lumotlar yuklandi va yangilandi.")

def filter_jobs(company=None, location=None):
    query = "SELECT title, company, location, description, application_link FROM jobs WHERE 1=1"
    params = []

    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")

    cursor.execute(query, params)
    return cursor.fetchall()

def export_to_csv(jobs, filename='filtered_jobs.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Company', 'Location', 'Description', 'Application Link'])
        writer.writerows(jobs)
    print(f"{filename} faylga saqlandi.")

if __name__ == "__main__":
    scrape_jobs()

    filtered_jobs = filter_jobs(location='Remote')
    export_to_csv(filtered_jobs, filename='remote_jobs.csv')

    sofa_jobs = filter_jobs(company='Sofa')
    export_to_csv(sofa_jobs, filename='sofa_jobs.csv')

    conn.close()
