from scrapy import cmdline
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
cmdline.execute("scrapy crawl nfu -o result.csv -t csv".split())