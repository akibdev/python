users = [
  {
    "user_id": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": False
  },
  {
    "user_id": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": False
  },
  {
    "user_id": 1,
    "id": 3,
    "title": "fugiat veniam minus",
    "completed": False
  },
  {
    "user_id": 1,
    "id": 4,
    "title": "et porro tempora",
    "completed": True
  },
  {
    "user_id": 1,
    "id": 5,
    "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
    "completed": False
  },
  {
    "user_id": 1,
    "id": 6,
    "title": "qui ullam ratione quibusdam voluptatem quia omnis",
    "completed": False
  },
  {
    "user_id": 1,
    "id": 7,
    "title": "illo expedita consequatur quia in",
    "completed": False
  },
  {
    "user_id": 1,
    "id": 8,
    "title": "quo adipisci enim quam ut ab",
    "completed": True
  },
  {
    "user_id": 1,
    "id": 9,
    "title": "molestiae perspiciatis ipsa",
    "completed": False
  },
  {
    "user_id": 1,
    "id": 10,
    "title": "illo est ratione doloremque quia maiores aut",
    "completed": True
  },
  {
    "user_id": 1,
    "id": 11,
    "title": "vero rerum temporibus dolor",
    "completed": True
  },
  {
    "user_id": 1,
    "id": 12,
    "title": "ipsa repellendus fugit nisi",
    "completed": True
  },
  {
    "user_id": 1,
    "id": 13,
    "title": "et doloremque nulla",
    "completed": False
  },
  {
    "user_id": 1,
    "id": 14,
    "title": "repellendus sunt dolores architecto voluptatum",
    "completed": True
  },
  {
    "user_id": 1,
    "id": 15,
    "title": "ab voluptatum amet voluptas",
    "completed": True
  },
  {
    "user_id": 1,
    "id": 16,
    "title": "accusamus eos facilis sint et aut voluptatem",
    "completed": True
  },
  {
    "user_id": 1,
    "id": 17,
    "title": "quo laboriosam deleniti aut qui",
    "completed": True
  },
  {
    "user_id": 1,
    "id": 18,
    "title": "dolorum est consequatur ea mollitia in culpa",
    "completed": False
  },
  {
    "user_id": 1,
    "id": 19,
    "title": "molestiae ipsa aut voluptatibus pariatur dolor nihil",
    "completed": True
  },
  {
    "user_id": 1,
    "id": 20,
    "title": "ullam nobis libero sapiente ad optio sint",
    "completed": True
  },
  {
    "user_id": 2,
    "id": 21,
    "title": "suscipit repellat esse quibusdam voluptatem incidunt",
    "completed": False
  },
  {
    "user_id": 2,
    "id": 22,
    "title": "distinctio vitae autem nihil ut molestias quo",
    "completed": True
  },
  {
    "user_id": 2,
    "id": 23,
    "title": "et itaque necessitatibus maxime molestiae qui quas velit",
    "completed": False
  },
  {
    "user_id": 2,
    "id": 24,
    "title": "adipisci non ad dicta qui amet quaerat doloribus ea",
    "completed": False
  },
  {
    "user_id": 2,
    "id": 25,
    "title": "voluptas quo tenetur perspiciatis explicabo natus",
    "completed": True
  },
  {
    "user_id": 2,
    "id": 26,
    "title": "aliquam aut quasi",
    "completed": True
  },
  {
    "user_id": 2,
    "id": 27,
    "title": "veritatis pariatur delectus",
    "completed": True
  },
  {
    "user_id": 2,
    "id": 28,
    "title": "nesciunt totam sit blanditiis sit",
    "completed": False
  },
  {
    "user_id": 2,
    "id": 29,
    "title": "laborum aut in quam",
    "completed": False
  },
  {
    "user_id": 2,
    "id": 30,
    "title": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis",
    "completed": True
  },
  {
    "user_id": 2,
    "id": 31,
    "title": "repudiandae totam in est sint facere fuga",
    "completed": False
  },
  {
    "user_id": 2,
    "id": 32,
    "title": "earum doloribus ea doloremque quis",
    "completed": False
  },
  {
    "user_id": 2,
    "id": 33,
    "title": "sint sit aut vero",
    "completed": False
  },
  {
    "user_id": 2,
    "id": 34,
    "title": "porro aut necessitatibus eaque distinctio",
    "completed": False
  },
]

complete = []
uncomplete = []
for user in users:
   if user.get('completed'):
      complete.append(user.get('id'))
   else:
      uncomplete.append(user.get('id'))

print(complete)