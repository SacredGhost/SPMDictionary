import re
import os

folder_name = "EnemyEntry generator"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

relative_path = os.path.join(folder_name, "output_enemy_entries.txt")
file_path = os.path.join(os.getcwd(), relative_path)

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' removed successfully.")
else:
    print(f"File '{file_path}' does not exist.")

def convert_item_lines(item_lines):
    drops = []
    for item_line in item_lines:
        match = re.match(r'\s*(.*?):\s*(\d+)', item_line)
        if match:
            item_name, weight = match.groups()
            drop_line = 'Drop (item_name = "{}", hex_value = get_hex_value("{}"), weight = {}),'.format(item_name, item_name, weight)
            drops.append(drop_line)
    return drops

def parse_template(template_text):
    template_list = template_text.split("Template ")
    parsed_templates = []

    for template in template_list:
        if not template.strip():
            continue

        lines = template.split('\n')
        template_number = lines[0].strip()

        # Remove trailing colon from "Template X:"
        template_number = template_number.rstrip(':')
        
        enemy_name = None
        drop_percent = None
        drops = []

        for line in lines[1:]:
            line = line.strip()
            if line.startswith("Name:"):
                # Capture the enemy name directly
                enemy_name = re.sub(r'Name:\s*', '', line).strip()
            elif line.startswith("DropItemChance:"):
                drop_percent_match = re.search(r'DropItemChance:\s+(\d+)\s*', line)
                if drop_percent_match:
                    drop_percent = float(drop_percent_match.group(1)) / 100
            elif line.startswith("NULL:"):
                continue
            elif line:
                match = re.match(r'(.+):\s+(\d+)', line)
                if match:
                    item_name, weight = match.groups()
                    drop_line = 'Drop (item_name = "{}", hex_value = get_hex_value("{}"), weight = {}),'.format(item_name, item_name, weight)
                    drops.append(drop_line)

        if enemy_name is not None and drop_percent is not None:
            enemy_entry = (
                "EnemyEntry (\n"
                '    "{}",\n'
                "    None,\n"
                '    "Template {}",\n'
                "    {},\n"
                "    EnemyDrops (\n"
                "        {}\n"
                "    )\n"
                ")".format(enemy_name, template_number, drop_percent, '\n        '.join(drops))
            )

            parsed_templates.append(enemy_entry)

    return parsed_templates

us0_file_path = os.path.join(folder_name, "us0.txt")

with open(us0_file_path, "r") as file:
    template_text = file.read()

generated_enemy_entries = parse_template(template_text)

with open(relative_path, "w") as output_file:
    for entry in generated_enemy_entries:
        output_file.write(entry + '\n')

print(f"File '{relative_path}' saved successfully.")