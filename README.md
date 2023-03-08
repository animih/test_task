# test_task

## Задание 1. 
##### *Адаптировать код для диффузионной модели для генерации изображений цветов.*

Результат представлен в [ноутбке](https://github.com/animih/test_task/blob/main/1_diffusion_model/flowers.ipynb)

## Задание 2.
##### 1. *Написать модуль для графов*

Ключевые особенности модуля (как я понял задание)
- За основу представления графа взят словарь из списков (а не матрица смежности)
- Генерация случайного графа происходит с фиксированным числом вершин, где ребро между двумя любыми вершинами имеет 50 % шанс возниковения
- Отрисовка графа происходит путём равномерного размещения по окружности вершин и использует словари параметров как в matplotlib-е для задания параметров линий и текста

##### 2. *Алгоритм выбора маскимального числа N несмежных вершин*

Логика алгоритма объяснена в [ноутбке](https://github.com/animih/test_task/blob/main/2_graphs/task2.ipynb) там же находится пример работы алгоритма

## Задание 3.

##### 1. *Написать скрипт для подсчета числа вхождений каждого слова в файл*

Комменатрий : здесь я намерено постарался не использовать awk, так его использование очень быстро все сводит к написанию си-подобного кода и сильно упрощает работу как в [примере](https://www.golinuxcloud.com/count-occurrences-of-word-in-file-bash-linux/). Поэтому этот и последующий скрипт был написан через функцю tr.

Использование скрипта : ./count_words.sh filename

##### 2. *Написать скрипт для создания пустых файлов $word_n с названиями из топ-10 самых встречаемых слов*

Комменатрий : здесь я понял задание так, что на месте n должно стоять число вхождений слова в текст.

Использование скрипта : ./count_top_words.sh filename output_dir

##### 3. *Запустить скрипт в докер-контейнере*
Далее приведены команды из терминала, которые требуются для выполнения задачи (не придумал как вставить иначе)

Создание контейнера:
$docker run --name test_container -d -i -t alpine /bin/sh

Копирование текстового файла в котейнер:
$sudo docker cp dracula.txt test_container:/dracula.txt

Запуска bash-скрипта в контейнере:
$docker exec -i test_container /bin/sh -s dracula.txt < count_words.sh
