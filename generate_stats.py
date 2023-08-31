import json
import os
from jinja2 import Environment, FileSystemLoader               #requires jinja2
import sys

if len(sys.argv) < 2:
    print("Usage: python generate_stats.py <Page Title>")
    sys.exit(1)

page_title = sys.argv[1]

# Load the template environment
env = Environment(loader=FileSystemLoader('./'))

# Load the NFT metadata JSON files
trait_statistics = {}

for i in range(10000): #Set number of jsons in folder *IMPORTANT*
    json_filename = f"build/json/{i}.json"  # Adjust the file path accordingly
    with open(json_filename, 'r') as json_file:
        nft_metadata = json.load(json_file)

        attributes = nft_metadata.get("attributes", [])

        for attribute in attributes:
            trait_type = attribute.get("trait_type")
            value = attribute.get("value")

            if trait_type not in trait_statistics:
                trait_statistics[trait_type] = {}

            if value not in trait_statistics[trait_type]:
                trait_statistics[trait_type][value] = {'count': 1}
            else:
                trait_statistics[trait_type][value]['count'] += 1

# Count the number of JSON files in the directory
json_directory = "build/json"  # Adjust the file path accordingly
total_count = len([name for name in os.listdir(json_directory) if name.endswith(".json")])

# Calculate total counts and percentages for traits
for trait_type, values in trait_statistics.items():
    total_trait_count = sum(stats['count'] for value, stats in values.items())
    remaining_count = total_count - total_trait_count

    if trait_type not in trait_statistics:
        trait_statistics[trait_type] = {'None': {'count': 0}}

    values['None'] = {'count': remaining_count}

    for value, stats in values.items():
        stats['percentage'] = (stats['count'] / total_count) * 100

# Sort values within each trait type by count
for trait_type, values in trait_statistics.items():
    sorted_values = sorted(values.items(), key=lambda x: x[1]['count'], reverse=True)
    trait_statistics[trait_type] = {value: stats for value, stats in sorted_values}

# Render the template and generate the output HTML
template = env.get_template('template.html')  # 'template.html' is the name of your Jinja2 template file
output_html = template.render(page_title=page_title, trait_statistics=trait_statistics)

# Save the HTML to a file
with open('output.html', 'w') as output_file:
    output_file.write(output_html)
