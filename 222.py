class Human:

    def __init__(self, name) -> None:
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')

    def __str__(self) -> str:
        return self.name


class Student(Human):

    def ask_question(self, someone, question):
        self.someone = someone
        self.question = question
        print(f'{self.someone}, {self.question}')
        someone.answer_question(question)
        print()


class Curator(Human):
    def answer_question(self, question):
        self.question = question
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)

    def __str__(self) -> str:
        return self.name


class Mentor(Human):
    def answer_question(self, question):
        self.question = question
        if question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)

    def __str__(self) -> str:
        return self.name


class CodeReviewer(Human):
    def answer_question(self, question):
        self.question = question
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)

    def __str__(self) -> str:
        return self.name


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')


student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
