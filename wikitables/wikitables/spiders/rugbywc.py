import csv
import scrapy


class RugbywcSpider(scrapy.Spider):
    name = 'rugbywc'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Rugby_World_Cup']

    def parse(self, response):
        col_names = ['Edition','Year','Host','Champion','Score-final','Runner-up','Third','Score-plate','Fourth','Num-teams']
        rows = []

        table = response.xpath('//tbody')[4].xpath('tr')  
        for i in range (2, len(table)):
            tr = table[i]
            ed = tr.xpath('td/text()').extract()[0][:-1] 
            yr = tr.xpath('td/a/text()').extract()[0]
            host = tr.xpath('td/a/text()').extract()[1]
            if i==3:
                champ = tr.xpath('td/b/a/text()').extract()[0]
                scr_f = tr.xpath('td/b/a/text()').extract()[1]
                run_up = tr.xpath('td/a/text()').extract()[6]
                third = tr.xpath('td/a/text()').extract()[7]
                scr_p = tr.xpath('td/a/text()').extract()[8]
                fourth = tr.xpath('td/a/text()').extract()[9]
                n_team = tr.xpath('td/text()').extract()[-1][:-1] 
                rows.append([ed, yr, host, champ, scr_f, run_up, third, scr_p, fourth, n_team])
                print(rows[-1])
            else:
                try:
                    champ = tr.xpath('td/a/text()').extract()[2]
                    if champ == 'a.e.t.': champ = tr.xpath('td/a/text()').extract()[1]
                    scr_f = tr.xpath('td/b/a/text()').extract()[1]
                    run_up = tr.xpath('td/a/text()').extract()[3]
                    third = tr.xpath('td/a/text()').extract()[4]
                    scr_p = tr.xpath('td/a/text()').extract()[5]
                    fourth = tr.xpath('td/a/text()').extract()[6]
                    n_team = tr.xpath('td/text()').extract()[-1][:-1] 
                    rows.append([ed, yr, host, champ, scr_f, run_up, third, scr_p, fourth, n_team])
                    print(rows[-1])
                except IndexError:
                    try:
                        champ = tr.xpath('td/b/a/text()').extract()[0]
                        scr_f = tr.xpath('td/b/a/text()').extract()[1]
                        run_up = tr.xpath('td/a/text()').extract()[2]
                        third = tr.xpath('td/a/text()').extract()[3]
                        scr_p = tr.xpath('td/a/text()').extract()[4]
                        fourth = tr.xpath('td/a/text()').extract()[5]
                        n_team = tr.xpath('td/text()').extract()[-1][:-1] 
                        rows.append([ed, yr, host, champ, scr_f, run_up, third, scr_p, fourth, n_team])
                        print(rows[-1])
                    except IndexError: None
        # Now persist it to disk
        with open("rugbywc_results.csv", "w", newline='') as _f:
            writer = csv.writer(_f)
            # write the column names
            writer.writerow(col_names)
            # now write the rows
            writer.writerows(rows)
        pass
