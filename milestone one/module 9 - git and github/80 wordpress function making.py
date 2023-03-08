# def peragraph(text):
#     code = f'<-- this is peragraph -->\n<p>{text}</p>\n<!-- this is peragraph -->'
#     return code
# demo = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old'

# print(peragraph(demo))


def wp_heading_one(wph1):
    wph1_code = f'<!-- heading one -->\n<h1>{wph1}</h1>\n<-- heading one -->'
    return wph1_code

def wp_p1(wpp1):
    wpp1_code = f'<!-- peragraph one -->\n<p>{wpp1}</p>\n<-- peragraph one -->'
    return wpp1_code

def wp_heading_two(wph2):
    wph2_code = f'<!-- heading two -->\n<h2>{wph2}</h2>\n<-- heading two -->'
    return wph2_code

def wp_p2(wpp2):
    wpp2_code = f'<!-- peragraph two -->\n<p>{wpp2}</p>\n<-- peragraph two -->'
    return wpp2_code