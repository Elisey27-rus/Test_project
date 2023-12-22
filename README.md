##README
#Описание проекта
Этот мини-проект реализован с использованием фреймворка Django и предоставляет веб-приложение для
управления товарами и их покупкой с использованием платежной системы Stripe. Проект включает в себя следующие функции:

1.Создана модель Item с тремя характеристиками: name, description и price.

2.Реализованы три веб-страницы (вьюшки):

main: Главная страница, на которой перечислены все доступные товары.
details: Страница, где можно просмотреть описание товара и перейти к странице для его покупки.
create: Страница, позволяющая создавать новые товары.

3.Проект упакован в Docker-контейнер для облегчения развертывания и управления.

4.В админке Django настроена возможность просматривать и редактировать товары.

#Установка и запуск проекта
Чтобы установить и запустить проект на вашем компьютере, выполните следующие шаги:

Клонирование репозитория: Склонируйте репозиторий с проектом на свой компьютер:
bash
Copy code
git clone https://github.com/Elisey27-rus/Test_project
cd Test_project
Настройка виртуального окружения (рекомендуется): Создайте виртуальное окружение Python, чтобы изолировать зависимости
проекта:
bash
Copy code
python -m venv venv
Активация виртуального окружения (Linux/macOS):
bash
Copy code
source venv/bin/activate

Никогда ранее я не имел опыта работы с Stripe, но я сделал все возможное для успешного перехода к процессу покупки
товара.
В результате получил следующий респонс:
{"sessionId": "cs_test_a1PNkSMSHBl4lwz13ieKrPAvkyD8nVaqt6AFwC4X3JhXpu9kgDfCKHCLiN"}
Этот респонс подтверждает успешное завершение сессии.

Также у меня возник вопрос о создании двух Stripe Keypair для разных валют.
На данный момент мне не полностью понятен процесс, но я предлагаю альтернативный вариант:
парсинг данных центробанка и их курсов валют для определения стоимости валют, необходимых нам."

Контактная информация
Если у вас есть вопросы или требуется дополнительная помощь, свяжитесь со мной:

#Имя: Станислав Елисейкин
#Телефон: +7 996 988 27 26
#Электронная почта: eliseykinstas1995@gmail.com
