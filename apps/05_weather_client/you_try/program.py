import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'loc, condition, temp, scale')

def main():
    # print the header
    print_the_header()

    zipcode = int(input('What is your zip code? '))

    html = get_html_from_web(zipcode)

    # parse html
    report = get_weather_from_html(html)

    # display forecast
    print('The weather condition in {} is {}, and it\'s {} degrees {}.'.format(
        report.loc,
        report.condition,
        report.temp,
        report.scale
    ))


def print_the_header():
    print('----------------------------------------')
    print('             WEATHER APP')
    print('----------------------------------------')

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text

def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherConditionsCSS = '.condition-icon p'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'

    soup = bs4.BeautifulSoup(html, 'lxml')

    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = get_city_state(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(loc, condition, temp, scale)
    # return loc, condition, temp, scale
    report = WeatherReport(condition=condition, temp=temp, loc=loc, scale=scale)
    return report

def cleanup_text(text):
    if not text:
        return text

    text = text.strip()
    return text

def get_city_state(loc : str):
    parts = loc.split('\n')
    return parts[0].strip()



if __name__ == '__main__':
    main()