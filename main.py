from Post import Post

post = Post(database="anelinfo", collection="posts")
# post.createIndex("name")
post.insert({"name": "post2", "description": "12323"})
print(post.list())