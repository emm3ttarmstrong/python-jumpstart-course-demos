import requests

def main():
    # print the header
    print_the_header()

    zipcode = int(input('What is your zip code? '))

    html = get_html_from_web(zipcode)

    # parse html
    # display forecast


def print_the_header():
    print('----------------------------------------')
    print('             WEATHER APP')
    print('----------------------------------------')

def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    main()