#elements
products = response.css('details-pricing')

"title": products.css('a::text').get()
"price": products.css('p.price.larger::text').get()
"link": products.css('a::attr(href)').get()

)
