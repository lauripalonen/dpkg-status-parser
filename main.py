from modules.json_converter import Json_converter
import sys

print('Dpkg status data parser')
print('-----------------------')
input_name = input('File name (input): ')

try:
  input_file = open(input_name) 
  input_file.close()
except:
  print('Error while trying to open file \'{}\''.format(input_name))
  print('Aborting...')
  sys.exit()

output_name = input('File name (output): ')

converter = Json_converter(input_name, output_name)
converter.run()