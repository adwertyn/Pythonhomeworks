from bs4 import BeautifulSoup

with open('weather.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

weather_data = []
rows = soup.find('tbody').find_all('tr')

print("Weather Forecast:")
for row in rows:
    cols = row.find_all('td')
    day = cols[0].text.strip()
    temperature = int(cols[1].text.strip().replace('°C', ''))
    condition = cols[2].text.strip()
    weather_data.append({'day': day, 'temperature': temperature, 'condition': condition})
    print(f"Day: {day}, Temperature: {temperature}°C, Condition: {condition}")

max_temp = max(weather_data, key=lambda x: x['temperature'])['temperature']
hottest_days = [entry['day'] for entry in weather_data if entry['temperature'] == max_temp]
sunny_days = [entry['day'] for entry in weather_data if entry['condition'] == 'Sunny']

print("\nHottest Day(s):", ', '.join(hottest_days))
print("Sunny Day(s):", ', '.join(sunny_days))
average_temp = sum(entry['temperature'] for entry in weather_data) / len(weather_data)
print(f"\nAverage Temperature: {average_temp:.2f}°C")
