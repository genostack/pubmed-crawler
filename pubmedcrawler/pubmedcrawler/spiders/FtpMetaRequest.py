import json
import scrapy
import os
from dateutil import parser
class FtpMetaRequest(scrapy.http.Request):
    # add user with password to ftp meta request
    user_meta = {'ftp_user': 'anonymous', 'ftp_password': ''}

    def init(self, args, **kwargs):
        super(FtpMetaRequest, self).init(args, **kwargs)
        self.meta.update(self.user_meta)

class FileFtpRequest(FtpMetaRequest):
    pass

class ListFtpRequest(FtpMetaRequest):
    pass

class MedisumSpider(scrapy.Spider):
    name = "pubmed"
    def start_requests(self):
        # start request to get all files
           yield ListFtpRequest("ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/")
           yield ListFtpRequest("ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/")

    def parse(self, response):
        # get response with all files
        files = json.loads(response.body)
        # get data from each file
        for f in files:
            path = os.path.join(response.url, f['filename'])
            request = FileFtpRequest(path, callback=self.parse_item)
            yield request
    def parse_item(self, response):
         # do some actions
         item = PubmedcrawlerItem()
         item['article'] = response.body

         pass
