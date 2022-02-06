"""
一、视图
    视图就是通过查询得到一张虚拟表，然后保存下来，下次可以直接使用，视图也是表
为什么要用视图
    如果要频繁操作一张虚拟表，你就可以制作成视图，后续直接操作
如何操作
    固定语法
    create view 视图名 as 虚拟表的查询语句
注意：
    -1.创建视图在硬盘上只会有表结构，没有表数据（数据还是来自于之前的表）
    -2.视图只是用来查询的 里面的数据不要继续修改 可能会影响真正的表
视图使用频率高不高
    不高，创建了多个视图后会造成表不好维护，试图了解就可，基本不用

二、触发器
    在满足对表的数据进行增、删、改的情况下，自动触发的功能
    使用触发器可以帮助我们监控、日志
    触发器可以在六种情况下触发、增前、增后、删前删后、改前改后
基本语法结构
    create trigger 触发器的名字，before/after  insert/update/delete on 表名
    for each row begin sql语句 end
    具体使用 针对触发器的名字 通常要做到见名知义
    针对删和改、书写格式一致

三、事务
什么是事务
    开启一个事务可以包含多条sql语句，这些sql语句要么同时成功
    要么一个都不成功，成为事务的原子性
事务的作用
    保证了对数据的安全性
事务的四大特性
ACID
A:原子性
    一个事务是一个不可分割的单位，事务中包含的诸多操作
    要么同时成功要么同时失败
C:一致性
    事务必须是使数据库从一个一致性的状态变到另外一个一致性的状态
    一致性和原子性密切相关
I:隔离性
    一个事务的执行不能被其他事务干扰
    （即一个事务内部的操作及使用到的数据对并发的其他事务是隔离的，并发执行的事务之间也是互相不干扰的）
D:持久性
    一个事务一旦提交成功执行成功，那么他对数据库中数据的修改应该是永久的
    接下来的其它操作或者故障不应该对其有任何影响
如何使用事务
    事务相关关键字
    1.开启事务
        start transaction;
    2.回滚（回到事务之前的状态）
        rollback
    3.二次确认（确认之后就无法回滚了）
        commit;

模拟转账功能
create table user(
    id int primary key auto_increment,
    name char(16),
    balance int
    );
insert into user(name.balance) values("jason",1000),("egon",2000)，("tank",3000);
先开启事务
start transaction;
多条sql语句
update user set balance= 900 where name='jason';
update user set balance= 1010 where name='egon';
update user set balance= 1090 where name='tank';

总结：当想让多条sql语句同时执行时才会使用事务。

四、存储过程
    存储过程就类似于python中的自定义函数
    它的内部包含了一系列可以执行的sql语句，存储过程存放于MYSQL服务端中， 可以直接调用存储过程出发内部sql语句执行
基本使用
    create procedure 存储过程的名字（形参一，形参二。。）
    begin sql代码 end
调用
    call 存储过程的名字（）
三种开发模型
    第一种:应用程序：程序员写代码开发
          MYSQL：提前编写好存储过程，供应用程序使用
        好处：开发效率提升了，执行效率也上去了
        缺点：考虑到认为元素、跨部门沟通的问题，后续的存储过程扩展性差
    第二种：应用程序：程序员写代码开发外，涉及到数据库操作也自己动手写
        优点：扩展性高
        缺点：开发效率高
            编写sql语句太过繁重，而且后续还需要考虑sql优化问题
    第三种：应用程序：只写程序代码 不写sql语句  给予别人写好的操作MYsql的框架使用
        优点：开大效率高
        缺点：语句扩展性差，可能会出现效率低的问题
    存储过程演示：
    delimiter $$
    create procedure p1（
    in m int, # 只进不出， m 不能返回出去
    in n int,
    out res int,） # 该形参可以返回出去
    begin
    select tname from teacher where tid>m and tid<n;
    set res=666; # 将res变量修改 用来标识当前的存储过程代买确实执行了
    end $$
    delimiter ;
# 针对形参res 不能直接传数据，应该传一个变量名
# 定义变量
set @ret = 10;
# 查看变量对应的值
select @ret;
"""
