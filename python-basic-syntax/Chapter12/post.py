class Post:
    """
        게시물 클래스
        param id:글번호
        param title:글제목
        param content: 글내용
        param viewCount: 조회수
    """

    def __init__(self, id, title, content, viewCount):
        self.id = id
        self.title = title
        self.content = content
        self.viewCount = viewCount

    def set_post(self, id, title, content, viewCount):
        self.id = id
        self.title = title
        self.content = content
        self.viewCount = viewCount

    def add_view_count(self):
        self.viewCount += 1

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_viewCount(self):
        return self.viewCount


if __name__ == "__main__":
    post = Post(1, "테스트", "테스트입니다.", 0)
    print(f"{post.get_id()} , {post.get_content()} , {post.get_title()}, {post.get_viewCount()}")
    post.set_post(1, "테스트2", "테스트입니다.2", 0)
    print(f"{post.get_id()} , {post.get_content()} , {post.get_title()}, {post.get_viewCount()}")
    post.add_view_count()
    print(f"{post.get_id()} , {post.get_content()} , {post.get_title()}, {post.get_viewCount()}")
