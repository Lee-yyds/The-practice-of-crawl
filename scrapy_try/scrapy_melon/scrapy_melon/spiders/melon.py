import scrapy
from scrapy import cmdline
from scrapy_melon.items import ScrapyMelonItem
from scrapy_melon.pipelines import ScrapyMelonPipeline


class MelonSpider(scrapy.Spider):
    name = 'melon'
    allowed_domains = ['api.tgspa5.xyz']
    base_url = 'https://api.tgspa5.xyz/v1/videos?category=1&tags=&order_by=updated_at&per_page=20&page=%d'
    start_urls = []
    for i in range(1, 251):
        start_urls.append(base_url % i)

    def parse(self, response, *args, **kwargs):
        dt_list = response.json()['data']['items']
        item = ScrapyMelonItem()
        for i in dt_list:
            item['title'] = i['chs_title']
            item['url'] = 'https://1105143.tgsph2.xyz//#/play/' + str(i['id'])
            print(item)
            yield dict(item)


cmdline.execute('scrapy crawl melon --nolog'.split())
