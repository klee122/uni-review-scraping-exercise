import scrapy

class unireviewspider(scrapy.Spider):
    name = 'unireview'
    start_urls = ['https://www.whatuni.com/university-course-reviews/search/?study-level=postgraduate']

    def parse(self,response):
        
        for review in response.css('div.rlst_wrap'):
            yield {
                'name': review.css('h2 a::attr(title)').get(),
                'rating': review.css('span.cat_rat.rw_qus_des::text').getall()[1].replace('(','').replace(')',''),
                'comment': review.css('[id^="overallCommentId_"]::text').get(),
            }

        next_page = 'https://www.whatuni.com' + response.css('ul.pagn li:last-child a::attr(href)').get()
        if next_page != None:
            yield response.follow(next_page, callback=self.parse)