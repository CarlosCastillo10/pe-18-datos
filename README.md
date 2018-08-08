# pe-18-datos

## actualizar desde los forks
- git remote add upstream https://github.com/reroes/pe-18-datos
- git fetch  upstream
- git merge upstream/master
- git push

## sentencias scrapy

In [49]: l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__info--age"]/span[@class="fi-p__info--ageNum"]/text(
    ...: )').extract()[0]
Out[49]: u'31'

In [50]: l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__info--role"]/text()').extract()[0]
Out[50]: u'\r\nArquero              '

In [51]: l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__n"]/a/span/text()').extract()[0]
Out[51]: u'Franco ARMANI'

