import os
import requests
from dotenv import load_dotenv
load_dotenv("bitly_token.env")
import argparse


parser = argparse.ArgumentParser(description='Обработка ссылки с помощью Bitly.')
parser.add_argument('url', help='Введите URL-адрес для обработки')
args = parser.parse_args()
link = args.url


def is_bitlink(bitly_token, url):
  bitlink = url.replace('https://', '')
  url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
  headers = {'Authorization': f'Bearer {bitly_token}'}
  response = requests.get(url, headers=headers)
  return response.ok


def shorten_link(bitly_token, long_url):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
    'Authorization': f'Bearer {bitly_token}'
            }
    params = {'long_url': long_url}
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(bitly_token, bitlink):
    bitlink = bitlink.replace('https://', '')
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {'Authorization': f'Bearer {bitly_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def process_link(bitly_token, link):
    if is_bitlink(bitly_token, link):
        print('Количество кликов', count_clicks(bitly_token, link))
    else:
        print('Битлинк', shorten_link(bitly_token, link))


def main():
    bitly_token = os.environ["BITLY_TOKEN"]
    process_link(bitly_token, link)


if __name__ == '__main__':
    main()
