import sys
import re

def markdown_to_html():
    html_text = ""
    markdown_lines = sys.stdin.readlines()
    is_ordered_list = False
    is_unordered_list = False

    for line in markdown_lines:
        line = line.rstrip()  # Remove trailing whitespace

        # Convert headers
        for i in range(3, 0, -1):
            if line.startswith('#' * i):
                line = line.replace('#' * i, f'<h{i}>', 1) + f'</h{i}>'

        # Convert bold text
        if '**' in line:
            line = line.replace('**', '<b>', 1)
            line = line.replace('**', '</b>', 1)

        # Convert italic text
        if '*' in line:
            line = line.replace('*', '<i>', 1)
            line = line.replace('*', '</i>', 1)

        # Convert ordered lists
        if re.match(r'\d+\.', line):
            line = '<li>' + line[line.find(' ')+1:] + '</li>'
            if not is_ordered_list:
                line = '<ol>\n' + line
                is_ordered_list = True
        else:
            if is_ordered_list:
                line = '</ol>\n' + line
                is_ordered_list = False

        # Convert unordered lists
        if line.startswith('- '):
            line = '<li>' + line[2:] + '</li>'
            if not is_unordered_list:
                line = '<ul>\n' + line
                is_unordered_list = True
        else:
            if is_unordered_list:
                line = '</ul>\n' + line
                is_unordered_list = False

        # Convert code
        if '`' in line:
            line = line.replace('`', '<code>', 1)
            line = line.replace('`', '</code>', 1)

        # Convert horizontal rules
        if line.strip() == '---':
            line = '<hr>'

        # Convert links
        start_link = line.find('[')
        end_link = line.find(']')
        start_url = line.find('(')
        end_url = line.find(')')
        if start_link != -1 and end_link != -1 and start_url != -1 and end_url != -1:
            link_text = line[start_link+1:end_link]
            url = line[start_url+1:end_url]
            line = line.replace(f'[{link_text}]({url})', f'<a href="{url}">{link_text}</a>')

        # Convert images
        start_alt_text = line.find('![')
        end_alt_text = line.find(']')
        start_img_url = line.find('(')
        end_img_url = line.find(')')
        if start_alt_text != -1 and end_alt_text != -1 and start_img_url != -1 and end_img_url != -1:
            alt_text = line[start_alt_text+2:end_alt_text]
            img_url = line[start_img_url+1:end_img_url]
            line = line.replace(f'![{alt_text}]({img_url})', f'<img src="{img_url}" alt="{alt_text}"/>')

        html_text += line + '\n'

    if is_ordered_list:
        html_text += '</ol>\n'
    if is_unordered_list:
        html_text += '</ul>\n'

    return html_text

print(markdown_to_html())
