def largest_histogram(histogram):
    hp,hc=0,0 #hc(high count)-верхушка для с(count),hp(high position)-верхушка для p(position)
    p,c=[],[]#используем метод стека(с(count)-количество в столбце,p(position)-индекс стролбца )
    result=[]#записываем все size'ы(размеры прямоугольников) сюда
    for i in range(0,len(histogram)):
        print(i,'-индекс ',histogram[i],'-число ')
        if histogram[i]>hc:#если количество элементов в столбце больше верхушки
            hc=histogram[i]#это новая верхушка
            hp=i#а верхушка позиции = индексу
            c.append(hc)#добавляем в стек
            p.append(hp)
            print(p,'-p ',c,'-c ')
        elif histogram[i]<hc:#если количество элементов в стобце меньше верхушки, то
            if histogram[i] in c:#если элемент уже присутствовал ранее в стеке - сбрасываем стек(p,c) до него
                while c[-1]!=histogram[i]:#при этом(выполняя сброс) просчитываем размеры всех возможных прямоугольников по горизонтали-вертикали 
                    print(c[-1:],'-c[-1:] ',[histogram[i]],'-histogram[i] ',i,'-i')
                    hc=c.pop()#при подсчёте сбрасываемый из стека элемент становится верхушкой, чтобы использовать его в формуле
                    hp=p.pop()
                    print(hp,'-hp',hc,'-hc')
                    size=hc*(i-hp)#здесь i, т.к. i+1-1. SIZE - основная формула для подсчета размера прямоугольника
                    print(size,'-size inside loop')
                    result.append(size)#добавляем в result
                hc=c.pop()#теперь, когда мы сбросили все элементы в стеке до того, что был ранее
                hp=p.pop()#делаем их верхушкой стека
                c.append(hc)#и возвращаем в стек
                p.append(hp)
                print(p,'-p ',c,'-c ')
            else:#если меньшего значения(количества элементов) не было в стеке, то просто заменяем верхушку с(но не p!) данным значением
                hc=histogram[i]
                c.pop()
                c.append(hc)
                print(p,'-p ',c,'-c ')
        size=hc*(i+1-hp)#считаем size для полученных значений hp и hc 
        result.append(size)#добавляем в result
        print(size,'-size')
    max_size=min(c)*(len(histogram)-p[0])#после завершения петли, последним считаем max-размер по горизонтали 
    print(max_size,'last_size')
    result.append(max_size)
    return(max(result))#возвращаем максимальное значение из result

print(largest_histogram([2,1,4,5,1,3,3]))#пример


#SHORTED VERSION 2.0
"""
def largest_histogram(histogram):
    hp,hc,p,c,result=0,0,[],[],[]
    for i in range(0,len(histogram)):
        if histogram[i]>hc:
            hc,hp=histogram[i],i
            c.append(hc),p.append(hp)
        elif histogram[i]<hc:
            if histogram[i] in c:
                while c[-1]!=histogram[i]:
                    result.append(c.pop()*(i-p.pop()))
                hc,hp=c[-1],p[-1]
            else:
                hc=histogram[i]
                c.pop(),c.append(hc)
        size=hc*(i+1-hp)
        result.append(size)
    max_size=min(c)*(len(histogram)-p[0])
    result.append(max_size)
    return(max(result))
print(largest_histogram([1,3,2,1,2]))
"""
