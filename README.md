# Welcome-project. Тестовое задание для инженера

**Привет!**

Это тестовое домашниее задание, которое поможет нам съеэкономить ваше и наше время и избежать множества вопросов на очной встрече.

При выполнении этого задания, нам хочет увидеть, как ты:

- Пишеш и структурируеш код
- Тестируеш то, что написано (unit tests)
- Документируеш свое решение


Мы ценим твое время и не хотим чтобы тратил много времени на это задание, поэтому не ожидаем полноценного и законченного решения. 

1. Напиши алгоритм  
2. 2-3 unit теста будет достаточно
3. Несколько строк документации по какой либо части твоего решения (без детализации)

Ниже ты можеш найти описание задачи которую мы предлагаем решить.

`Пожалуйста сделай fork этого репо и когда решение будет готово - отравь нам ссылку на PR`

`Если будут вопросы и/или нужно будет уточнение по задаче - это нормально. Просто создай issue и мы постараемся быстро тебе ответить`


**Good luck и увидимся позже!**

## Задача

У нас есть 2 и более сервисов описания API которых мы можем получить. Это собственно будут наши входные данные для нашего решения.

Задачa - сделать решение, которое будет принимать эти данные и формировать map/json.


### Пример входных данных


Каждый запрос это массив кортежей (verb, path). 


                 verb           path
                  |              |
                  |              |

    service1 = [("GET", "/api/v1/cluster/metrics"),
                ("POST", "/api/v1/cluster/{cluster}/plugins"),
                ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}")]


    service2 = [("GET", "/api/v1/cluster/freenodes/list"),
                ("GET", "/api/v1/cluster/nodes"),
                ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}"),
                ("POST", "/api/v1/cluster/{cluster}/plugins")]


слова в фигурных скобках {} - параметры

### Решение

Необходимо реализовать следующую логику:

*Сценарий 1*. Первый вызов


    IN ->    [("GET", "/api/v1/cluster/metrics"),
              ("POST", "/api/v1/cluster/{cluster}/plugins"),
              ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}")]

                                |

    LOGIC ->            parse and collect data
                        
        Разбить path на состовляюшие (split "/") и сформировать структуру типа дерево, ключами и узлами которого будут эти составлящие слова, а значением конечного пути - verb (метод - POST, GET..). 
        При формировании этого дерева исключить версию (/api/v1) и параметры ({cluster})

                                |

    OUT ->      {'cluster': 
                    {'metrics': 'GET', 
                    'plugins': 'POST'}
                }    


*Сценарий 2*. Второй и последующие вызовы


    IN ->    [("GET", "/api/v1/cluster/freenodes/list"),
              ("GET", "/api/v1/cluster/nodes"),
              ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}"),
              ("POST", "/api/v1/cluster/{cluster}/plugins")]

                                |

    LOGIC ->            parse and collect data
                        
        1. Ранее обработанные данные участвуют в обработке
        2. Если путь/поддерево не существует - создать новую ветвь
        3. Если путь/поддерево существует - проверить verb
            3.1 Если verb такой же  - пропустить
            3.2 Если verb отличается - вызвать Exception с полным путем до этого verb 

                                |

    OUT ->     {'cluster': 
                    {'metrics': 'GET', 
                    'plugins': 'POST', 
                    'freenodes': {'list': 'GET'}, 
                    'nodes': 'GET'
                    }
                }

