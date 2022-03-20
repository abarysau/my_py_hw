# HOME WORK 12.2

print('\n----------------\nHOME WORK 12.2\n----------------\n')


print('\nShop sample program\n')

# my modules

import xml.etree.ElementTree as ET

# my classes & variables

class XmlTreeHelper:

    def add_tags_with_text(parent, tags):
        elements = []
        for tag in tags:
            element = ET.SubElement(parent, tag)
            element.text = tags[tag]
            elements.append(element)
        return elements    
      
        

file = ''
root = ET.Element('shop')

category = ET.SubElement(root, 'category', {'name': 'Vegan Products'})

product_1 = ET.SubElement(category, 'product', {'name': 'Good Morning Sunshine'})
product_2 = ET.SubElement(category, 'product', {'name': 'Spaghetti Veganietto'})
product_3 = ET.SubElement(category, 'product', {'name': 'Fantastic Almond Milk'})

product_1_details = {'type': 'cereals',
                  'producer': 'Foods Limited',
                  'price': '9.90',
                  'currency': 'USD'}
product_2_details = {'type': 'pasta',
                  'producer': 'Programmers Eat Pasta Gmbh',
                  'price': '14.49',
                  'currency': 'EUR'}
product_3_details = {'type': 'beverages',
                  'producer': 'Drinks4Coders Inc.',
                  'price': '19.75',
                  'currency': 'USD'}
    
XmlTreeHelper.add_tags_with_text(product_1, product_1_details)
XmlTreeHelper.add_tags_with_text(product_2, product_2_details)
XmlTreeHelper.add_tags_with_text(product_3, product_3_details)


# my program


# Create XML doc and save it into a file

while True:
    try:
        file = input('\nEnter the XML file name to save (shop.xml): ')
        if file == '':
            file = 'shop.xml'
        tree = ET.ElementTree(root)
        print()
        print(ET.dump(root))
        tree.write(file, 'UTF-8', xml_declaration=True)    
        print('\nThe data were saved in file', file, end='\n\n') 
        break
    except Exception as e:
        print(e)

print('\nBye')
