====================
scrapy-splitvariants
====================

.. image:: https://travis-ci.org/scrapy-plugins/scrapy-splitvariants.svg?branch=master
    :target: https://travis-ci.org/scrapy-plugins/scrapy-splitvariants

.. image:: https://codecov.io/gh/scrapy-plugins/scrapy-splitvariants/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/scrapy-plugins/scrapy-splitvariants


``SplitVariantsMiddleware`` is a Scrapy spider middleware used to split
single items into multiple items when they have a "variants" key with multiple values.


Example usage
=============

Let's assume your spider outputs an item with different size options
(from an ecommerce website for example)::

    item = {"id": 12,
            "name": "Big chair",
            "variants": [{"size": "XL", "price": 200, "currency": "USD"},
                         {"size": "L", "price": 100, "currency": "USD"}]}

When you enable ``SplitVariantsMiddleware``, this single item will become
2 items with the different variants values into a different item::

    {"id": 12, "name": "Big chair", "size": "XL", "price": 200, "currency": "USD"}
    {"id": 12, "name": "Big chair", "size": "L", "price": 100, "currency": "USD"}


Installation
============

Install scrapy-splitvariants using ``pip``::

    $ pip install scrapy-splitvariants


Configuration
=============

1. Add ``SplitVariantsMiddleware`` by including it in ``SPIDER_MIDDLEWARES``
   in your ``settings.py`` file::

      SPIDER_MIDDLEWARES = {
          'scrapy_splitvariants.SplitVariantsMiddleware': 100,
      }

   Here, priority ``100`` is just an example.
   Set its value depending on other middlewares you may have enabled already.

2. Enable the middleware using ``SPLITVARIANTS_ENABLED`` set to ``True``
   in your ``setting.py``.
