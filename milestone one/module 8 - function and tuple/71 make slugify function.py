# def slugify(text):
#    slug = text.replace(' ','-').lower().strip()
#    while '--' in slug:
#       slug = slug.replace('--','-')
#    return slug

# title = input('Enter your title here: ')
# slug = slugify(title)
# print(slug)


# def slugify(text):
#    slug = text.strip().lower().replace(' ','-')
#    while '--' in slug:
#       slug = slug.replace('--','-')
#    return slug


# title = input('Enter your title here: ')
# slug = slugify(title)
# print(slug)


def slugfy(sentance):
   slug = sentance.strip().lower().replace(' ','-')
   while '--' in slug:
      slug = slug.replace('--','-')
   return slug

title = input('Enter your title here: ')
slug = slugfy(title)
print(slug)