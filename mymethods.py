def calculateInclusivePrice(exclusivePrice,tax):
    inclusivePrice = (exclusivePrice * tax) + exclusivePrice
    return (inclusivePrice)
 
 
products =[{"name":"milk","description":"cow milk","tax":0.16,"exclPrice":35.50},
           {"name":"bread","description":"white","tax":0.16,"exclPrice":45.50},
           {"name":"cooking oil","description":"salit","tax":0.16,"exclPrice":95.50},
           {"name":"soda","description":"fanta","tax":0.16,"exclPrice":33.50},
           {"name":"flour","description":"soko","tax":0.16,"exclPrice":92.50},]

for product in products:
    inclPrice = (calculateInclusivePrice(product["exclPrice"],product["tax"]))
    product["inclusivePrice"] = inclPrice
    print(product["name"], product["inclusivePrice"],product["description"])