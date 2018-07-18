# библиотека для работы с расширителем портов
import gpioexp
# создаём объект для работы с расширителем портов 
exp = gpioexp.gpioexp()

while True:
    # считываем состояние потенциометра
    pot = exp.analogRead(0)
    # включаем яркость светодиода
    # в зависимости от состояние потенциометра
    exp.analogWrite(7, pot)