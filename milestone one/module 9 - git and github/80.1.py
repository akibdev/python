import wp_func

h1text = 'this is heading one'
p1text =' It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters'
h2text = 'this is heading two'
p2text = 'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which'

article = wp_func.wp_heading_one(h1text)+wp_func.wp_heading_p1(p1text)+wp_func.wp_heading_two(h2text)+wp_func.wp_heading_p2(p2text)

print(article)


# hello jonogon?