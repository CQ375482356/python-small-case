

```python
#异常处理
# 可以让程序具有极好的容错性，更健壮。
# Python的异常处理机制主要依靠try、except、else、finally和raise五个关键字。try后面放置可能引发异常的代码块；except后对应异常类型和一个代码块，
# 用于表明except处理该类型的代码块，在多个except块后还可以放一个else块，表明不出现异常时还执行else块；最后还可以yield一个finally块，用于回收在try块里打开的物理资源。
# raise用于引发一个实际的异常对象，可单独作为语句使用。
# #使用try..except捕获异常
业务实现代码放在try块中定义，所有异常处理逻辑放在except块中处理，从而实现将"业务实现代码"和"错误处理代码分离"。
异常机制语法结构：
try： #引发异常
    #业务实现代码
    ...
except(Errorl,Error2,...)as e:   #捕获异常
    alert 输入不合法
    goto retry
    
#指定异常，非指定则无法处理
s1="hello"
try:
    int(s1)
except IndexError as e:  #万能异常用Exception，捕获任意异常，未知错误。
    print(e) 

#多异常捕获，使用except块捕获多种类型异常时，只要将多个异常用圆括号括起来，中间用逗号隔开即可。
import sys
try:
    a=int(sys.argv[1]) #代表运行程序时提高的第一个参数
    b=int(sys.argv[2]) #代表运行程序时提高的第二个参数
    c=a/b
    print("两数相除结果：",c)
except (IndexError,ValueError,ArithmeticError):
    print("程序发生数组越界、数据异常、算术异常之一")
except:
    print("未知错误")
#else块
#else块可以放在try块后面，也可以单独用else块，当try块无异常，而else块有异常，else块作用明显。
def else_test():
    s=input("请输入除数：")
    result=30/int(s)
    print("30除以%s的结果：%g" %(s,result))
def right_main():
    try:
        print("try块代码无异常")
    except:
        print("程序出现错误")
    else:
        else_test()
def wrong_main():
    try:
        print("try块代码无异常")
        else_test()
    except:
        print("程序出现错误")
wrong_main()
right_main()#放在else块中代码所引发的异常不会被except捕获，try后面能够捕获

#自定义异常，raise引发异常
class EvaException(BaseException):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg
    try:
        raise EvaException("类型错误")  #引发自定义异常,如果不带参数，默认runtimeError。
    except EvaException as e:
        print(e)
        
#except和raise结合使用
class PriceException(Exception):pass
class Pricetest:
    def __init__(self,init_price):
        self.init_price=init_price
    def bid(self,bid_price):
        d=0.0
        try:
            d=float(bid_price)
        except Exception as e:
            print("异常：",e)
            raise PriceException("必须为数值，不能包含其他字符！")
        if self.init_price>d :
            raise PriceException("拍卖价格低于起拍价，不允许竞拍！")
        init_price=d
def main():
    at=Pricetest(30.8)
    try:
        at.bid(40)
    except PriceException as e:
        print("main()函数捕获的异常：",e)
main()

注意：
python异常机制非常方便，但不能过度使用，把异常和普通错误混在一起，不编写任何错误处理代码，以简单引发异常代替所有错误处理；但不能代替流程控制。
对可预料的错误提供相应的处理。
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-17-4da237797267> in <module>()
         17 s1="hello"
         18 try:
    ---> 19     int(s1)
         20 except IndexError as e:  #万能异常用Exception，捕获任意异常，未知错误。
         21     print(e)
    

    ValueError: invalid literal for int() with base 10: 'hello'

