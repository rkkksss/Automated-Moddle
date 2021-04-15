
# Automated tests upload into Moodle 🐕


## Описание
Скрипт для автоматической генерации файлов формата *Gift with medias* (zip архив с условиями и картинками)

## Использование

Все картинки должны иметь название ```"заданиеXX..."```, где ```XX``` - номер теста 

Все текстовые файлы должны иметь название ```"Задание №XX"```, где ```XX``` - номер теста

```
python3 main.py [-h] --dest DIR --pic-path DIR --text-path DIR [--force]

Раскладываем фоточки

optional arguments:
  -h, --help       show this help message and exit
  --dest DIR       dir for result
  --pic-path DIR   dir with pictures
  --text-path DIR  dir with text
  --force          delete destination directory if exists
  ```

## Пример использования

Есть 2 папки: 
- photo, где лежат картинки для тестов с названиями вида ``` "задание1.вопрос1.2.jpg" ```
- test, где лежат тексты для тестов с названиями вида ``` "Задание №2.txt" ```
Сохранить данные вы хотите в папку res.
Тогда запуск скрипта будет иметь такой вид:
```
python3 sctipt.py --dest=res --pic-path=photo --text-path=test --force
```
