# DB와 연결하지 않았을 때 임시로 사용했습니다.
class Review:
    title = ''
    content = ''
    user = ''
#instance 생성 메서드    
    def __init__(self, content=content, title=title, user=user):#키=변수
        self.content = content
        self.title = title
        self.user = user
#생성된 인스턴스는 review1에 저장됩니다      
review1 = Review(title="인생 영화입니다", content="blabla", user="me")
review2 = Review(title="노잼", content="blabla2", user="me2")
review3 = Review(title="돈 아깝다 진짜", content="blabla3", user="me3")
review4 = Review(title="명징하게 직조해넨 어쩌구", content="blabla4", user="me4")