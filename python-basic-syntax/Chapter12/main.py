import csv
import os.path

from post import Post

file_path = "./data.csv"

posts = []

if os.path.exists(file_path):
    print("게시글 로딩중 ....")
    file = open(file_path, "r", encoding="utf8")
    reader = csv.reader(file)

    for data in reader:
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        posts.append(post)
else:
    file = open(file_path, "w", encoding="utf8", newline="")
    file.close()


# 게시글 쓰기
def write_post():
    """
    게시글 쓰기 함수
    :return:
    """
    print("###게시글쓰기###")
    title = input("제목을 입력해 주세요 \n >>>")
    content = input("내용을 입력해 주세요 \n >>>")

    # 글번호
    id = 1 if posts.__len__() == 0 else posts[-1].get_id() + 1
    view_count = 0
    post = Post(id, title, content, view_count)
    posts.append(post)

    print("입력이 완료되었습니다.")


# 게시글 상세
def detail_post(id):
    """
    게시글 상세보기
    :param id: 아이디
    :return:
    """
    print("###게시글상세###")

    for post in posts:
        print(post.get_id())
        if post.get_id() == id:
            post.add_view_count()
            print("번호 : ", post.get_id())
            print("제목 : ", post.get_title())
            print("본문 : ", post.get_content())
            print("조회수 : ", post.get_viewCount())
            target_post = post

    while True:
        print("Q) 수정: 1 삭제: 2 (메뉴로 돌아가려면 -1을 입력해주세요)")
        try:
            choice = int(input(">>>>"))
        except ValueError:
            print("숫자를 입력해주세요")
        else:
            if choice == 1:
                update_post(target_post)
                break
            elif choice == 2:
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print("잘못 입력하셨습니다.")


def update_post(target_post):
    """
    게시글 수정
    :param target_post:
    :return:
    """
    print("###게시글수정###")
    title = input("제목을 입력해 주세요 \n >>>")
    content = input("내용을 입력해 주세요 \n >>>")
    target_post.set_post(target_post.get_id(), title, content, target_post.get_viewCount())
    print("게시글이 수정되었습니다.")


def delete_post(target_post):
    """
    게시글삭제
    :param target_post:
    :return:
    """
    posts.remove(target_post)
    print("게시글이 삭제 되었습니다.")


# 게시글 목록
def list_post():
    """
    게시글목록
    :return:
    """
    print("###게시글목록###")

    if posts.__len__() == 0:
        print("목록없음")
        return

    ids = []
    for post in posts:
        ids.append(post.get_id())
        print("번호 : ", post.get_id())
        print("제목 : ", post.get_title())
        print("조회수 : ", post.get_viewCount())
        print("")

    while True:
        print("Q) 글번호를 선택해 주세요 (메뉴로 돌아가려면 -1을 입력해주세요)")
        try:
            choice = int(input(">>>>"))
        except ValueError:
            print("숫자를 입력해주세요")
        else:
            if choice in ids:
                detail_post(choice);
                break
            elif choice == -1:
                break
            else:
                print("선택된 ID가 없습니다.")


def save():
    """
    게시글 저장
    :return:
    """
    file = open(file_path, "w", encoding="utf8", newline="")
    writer = csv.writer(file)
    for post in posts:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_viewCount()]
        writer.writerow(row)
    file.close()
    print("저장이 완료되었습니다.")
    print("프로그램종료")


# 메뉴출력하기
while True:
    print("###FastCampus Blog###")
    print("- 메뉴를 선택해 주세요 -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    try:
        choice = int(input(">>>>"))
    except ValueError:
        print("숫자를 입력해주세요")
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            save()
            break
        else:
            print("잘못입력하셨습니다.")
