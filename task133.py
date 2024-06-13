import requests
import logging
def site_connected(sites_list):

  logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='site_connected.log',
    filemode='w',
    encoding='utf-8'
  )

  success_log = open('success_responses.log', 'w')
  bad_responses_log = open('bad_responses.log', 'w')
  blocked_responses_log = open('blocked_responses.log', 'w')

  for site in sites_list:
    try:
      response = requests.get(site, timeout=3)
      if response.status_code == 200:

        logging.info(f"Сайт {site} доступен")
        success_log.write(f"INFO:{site}, response - {response.status_code}\n")
      else:

        logging.info(f"Сайт {site} нет доступа (код ответа: {response.status_code})")
        bad_responses_log.write(f"WARNING:{site}, response -  {response.status_code}\n")
    except requests.exceptions.RequestException:

      logging.info(f"Сайт {site} нет доступа (невозможно получить ответ)")
      blocked_responses_log.write(f"ERROR:{site}, NO CONNECTION\n")

  success_log.close()
  bad_responses_log.close()
  blocked_responses_log.close()

sites = [
  'https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com',
         'https://tiktok.com', 'https://www.ozon.ru'
]
site_connected(sites)
