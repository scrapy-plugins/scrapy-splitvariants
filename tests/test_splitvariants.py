""" Tests to cover splitvariants middleware """
from unittest import TestCase

from scrapy.spiders import Spider
from scrapy.item import DictItem, Field
from scrapy.http import HtmlResponse
from scrapy.utils.test import get_crawler

from scrapy_splitvariants import SplitVariantsMiddleware


class TestItem(DictItem):
    """
    Item used in test spider
    """
    fields = {
        'id': Field(),
        'name': Field(),
        'size': Field(),
        'price': Field(),
        'variants': Field()
    }


class SplitVariantsTest(TestCase):
    """ Split variants middleware test cases """
    def setUp(self):
        self.spider = Spider('myspider',
                             start_urls=["http://example.com"])
        self.response = HtmlResponse(body=b"<html></html>",
                                     url="http://www.example.com")

    def test_variants_splitted(self):
        """
        Checks if item with variants is split as expected
        """
        settings = {"SPLITVARIANTS_ENABLED": True}
        crawler = get_crawler(settings_dict=settings)
        mware = SplitVariantsMiddleware.from_crawler(crawler)

        # Define item with variants
        item = {"id": 12,
                "name": "Big chair",
                "variants": [{"size": "XL", "price": 200},
                             {"size": "L", "price": 220}]}

        # Define how split items should look
        expected = [
            {"id": 12, "name": "Big chair", "size": "XL", "price": 200},
            {"id": 12, "name": "Big chair", "size": "L", "price": 220}]

        # Calling middleware for given result as a Scrapy Item()
        result = [TestItem(item)]
        result = mware.process_spider_output(self.response, result,
                                             self.spider)
        self.assertEquals(list(result), expected)


    def test_variants_dict_split(self):
        """
        Checks if dict with "variants" is split as expected
        """
        settings = {"SPLITVARIANTS_ENABLED": True}
        crawler = get_crawler(settings_dict=settings)
        mware = SplitVariantsMiddleware.from_crawler(crawler)

        # Define item with variants
        item = {"id": 12,
                "name": "Big chair",
                "variants": [{"size": "XL", "price": 200},
                             {"size": "L", "price": 220}]}


        # Define how split items should look
        expected = [
            {"id": 12, "name": "Big chair", "size": "XL", "price": 200},
            {"id": 12, "name": "Big chair", "size": "L", "price": 220}]

        # Calling middleware for given result as a Python dict
        result = [item]
        result = mware.process_spider_output(self.response, result,
                                             self.spider)
        self.assertEquals(list(result), expected)


    def test_untouched(self):
        """
        Checks if dict with "variants" is split as expected
        """
        settings = {"SPLITVARIANTS_ENABLED": True}
        crawler = get_crawler(settings_dict=settings)
        mware = SplitVariantsMiddleware.from_crawler(crawler)

        # Define item with non-"variants" key
        item = {"id": 12,
                "name": "Big chair",
                "options": [{"size": "XL", "price": 200},
                            {"size": "L", "price": 220}]}

        result = mware.process_spider_output(self.response, [item],
                                             self.spider)

        # item has no "variants" key, it should be left untouched
        expected = [item]
        self.assertEquals(list(result), expected)
