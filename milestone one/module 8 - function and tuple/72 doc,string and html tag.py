# def heading_two(text):
#    heading = f'<h2>{text}</h2>'
#    return heading

# data = heading_two('heading two')
# print(data)

# def heading_two(text):
#    '''
#    hello
#    '''

#    heading = f'<h2>{text}</h2>'
#    return heading

# data = heading_two('this is heading two')
# print(data)

# def html_tag(text, html_tag):
#    """
#    Return HTML Tag of any text
#    :pratext: any kind of string
#    :param html_tag: what king of html tag you want to generate
#    :return: HTML tag of any tag
#    """
#    html = f'<{html_tag}>{text}</{html_tag}>'
#    return html

# data = html_tag('hello jonogon', 'bolt')
# print(data)


def html_tag(text, html_tag):
   html = f'<{html_tag}>{text}</{html_tag}>'
   return html
html = html_tag('hello jonogon', 'h4')
print(html)