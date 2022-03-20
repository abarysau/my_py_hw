# HOME WORK 12.1

print('\n----------------\nHOME WORK 12.1\n----------------\n')


print('\nTemperature Converter sample program\n')

# my modules

import xml.etree.ElementTree as ET

# my classes & variables

class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        return 9.5/5.0 * temperature_in_celsius + 32

class ForecastXmlParser:
    def __init__(self, temperature_converter):
        self.temperature_converter = temperature_converter

    def parse(self, file):
        tree = ET.parse(file)
        root = tree.getroot()
        for child in root:
            day = child.find('day').text
            temperature_in_celsius = int(child.find(
                'temperature_in_celsius').text)
            temperature_in_fahrenheit = round(
                self.temperature_converter.convert_celsius_to_fahrenheit(
                    temperature_in_celsius),1)
            print('{0}: {1} Celsius, {2} Fahrenheit'.format(
                day.ljust(10), temperature_in_celsius, temperature_in_fahrenheit))
      
        

file = ''
temperature_converter = TemperatureConverter()
forecast_xml_parser = ForecastXmlParser(temperature_converter)


# my program


# get input data from XML file

while True:
    try:
        file = input('\nEnter the XML file name (forecast.xml): ')
        if file == '':
            file = 'forecast.xml'
        print('\nThe data from', file, 'to be processed', end='\n\n') 
        forecast_xml_parser.parse(file)
        
        break
    except Exception as e:
        print(e)

print('\nBye')
