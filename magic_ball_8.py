import random

def question_ball_8(answer):
    print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос: ")
    name = input("Введите ваше имя: ")
    print(f"Привет {name} ")
    while True:
        question = input("Введите вашь вопрос?: ")
        if question != "":
            print(random.choice(answer))

        question_variable = input("Хочешь задать еще один вопрос? (да/нет) или (yes/no): ")
        if "да" in question_variable.lower() or "yes" in question_variable.lower():
            pass
        elif "нет" in question_variable.lower() or "no" in question_variable.lower():
            print("Возвращайтесь если возникнут вопросы!")
            break


answer = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определенно да", "Можешь быть уверен в этом",
                  "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
                  "Пока не ясноб попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
                  "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
                  "Перспективы не очень хороши", "Весьма сомнительно"]

question_ball_8(answer)