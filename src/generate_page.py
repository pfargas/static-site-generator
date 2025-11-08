from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, 'r') as f:
        markdown = f.read()

    with open(template_path, 'r') as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    html_file = html_node.to_html()

    html_title = extract_title(markdown)

    final_html = template.replace(r"{{ Content }}", html_file).replace(r"{{ Title }}", html_title)
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    with open(dest_path, 'w') as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    full_path = os.path.abspath(dir_path_content)
    for item in os.listdir(full_path):
        curr_item_path_content = os.path.join(full_path, item)
        curr_dest_path_content = os.path.join(dest_dir_path, item).replace('.md', '.html')
        if not os.path.isfile(curr_item_path_content):
            os.makedirs(curr_dest_path_content, exist_ok=True)
            generate_pages_recursive(curr_item_path_content, template_path, curr_dest_path_content, basepath)
        else:
            generate_page(curr_item_path_content, template_path, curr_dest_path_content, basepath)