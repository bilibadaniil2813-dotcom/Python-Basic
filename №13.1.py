import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    cleaned = []
    in_tag = False
    for char in html:
        if char == '<':
            in_tag = True
        elif char == '>':
            in_tag = False
        elif not in_tag:
            cleaned.append(char)

    text = ''.join(cleaned)
    lines = [line for line in text.splitlines() if line.strip()]

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(lines))


if __name__ == '__main__':
    delete_html_tags('draft.html')
    print('OK')
