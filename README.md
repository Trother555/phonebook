# Простая телефонная книга на Django

## Модули:

### api
  Предоставляет api для телефонной книги
  endpoint: /api/v1/person/
  Методы:
  
  Тип   |Адрес |Параметры                                 |Тип контента
  ------|------|------------------------------------------|-----------
  POST  |/     | first_name<br>last_name<br>phone_number  |application/json
  GET   |/     | first_name<br>last_name                  |

  first_name и last_name - строки длиной до 50 символов
  phone_number - телефон в формате +00000000000
  
  
### front
  Фронт, использующий api. Пока синхронно.
