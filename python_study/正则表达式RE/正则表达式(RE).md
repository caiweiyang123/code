#正则表达式
##<p >&emsp;动机</p>
###<p >&emsp;&emsp;1.文本处理已经成为计算机常见的工作之一</p>
###<p >&emsp;&emsp;2.对文本内容的索搜，定位，提取是逻辑比较复杂的工作</p>
###<p >&emsp;&emsp;3.为了快速方便解决上述问题，产生了正则表达式技术</p>
##<p >&emsp;简介</p>
###<p >&emsp;&emsp;1.定义</p>
#####<p >&emsp;&emsp;&emsp;&emsp;即文本的高级匹配模式，，提供搜索，替换等功能。其本质是由一系列字符和特殊符号构成的字符串，这个字符串即正则表达式。</p>
###<p >&emsp;&emsp;2.原理</p>
#####<p >&emsp;&emsp;&emsp;&emsp;通过普通字符和有特定含义的字符，来组成字符串，用以描述一定的字符串规则，比如：重复，位置等，来表达某类特定的字符串，进而匹配</p>
###<p >&emsp;&emsp;3.目标<p>
#####<p >&emsp;&emsp;&emsp;&emsp;熟练掌握正则表达式元字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;能够读懂常见正则表达式，编辑简单的正则规则</p>
#####<p >&emsp;&emsp;&emsp;&emsp;能够熟练使用RE模块操作正则表达式</p>
##<p >&emsp;元字符使用</p>
###<p >&emsp;&emsp;普通字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：每个普通字符匹配对应的字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;注意事项：正则表达式在python中也可以匹配中文</p>
###<p >&emsp;&emsp;或关系</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符： |</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配|两侧任意的正则表达式即可</p>
###<p >&emsp;&emsp;匹配单个字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：.</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配除换行符外的任意一个字符</p>
###<p >&emsp;&emsp;匹配字符集</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：[字符集]</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配字符集中的任意一个字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;表达形式：</p>
#####<p >&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[abc#！好]表示[]中的任意一个字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[0-9][a-z][A-Z]表示区间内任意一个字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[_#?0-9a-z]混合书写，一般区间表达写在后面</p>
###<p >&emsp;&emsp;匹配字符集反集</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：[^字符集]</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配除了字符集以外的的任意一个字符</p>
###<p >&emsp;&emsp;匹配字符串开始位置</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：^</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配目标字符串的开头位置</p>
###<p >&emsp;&emsp;匹配字符串结束位置</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：$</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配目标字符串的结束位置</p>
#####<p >&emsp;&emsp;&emsp;&emsp;规则技巧：^和$必然出现在正则表达式的开头和结尾处。如果两者同时出现，则中间的部分必须是匹配整个目标字符串的全部内容</p>
###<p >&emsp;&emsp;匹配字符重复</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：*</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配前面的字符出现0次或多次</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：+</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配前面的字符出现1次或多次</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：？</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配前面的字符出现0次或1次</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：{n}</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配前面的字符出现n次</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：{m,n}</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：匹配前面的字符出现m到n次</p>
###<p >&emsp;&emsp;匹配任意（非）数字字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：\d\D</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：\d匹配任意数字字符，\D匹配任意非数字字符</p>
###<p >&emsp;&emsp;匹配任意（非）普通字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：\w\W</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：\w匹配任意普通字符，\W匹配任意非普通字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;说明：普通字符指数字，字母，下划线，汉字。</p>
###<p >&emsp;&emsp;匹配任意（非）空字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：\s\S</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：\s匹配空字符，\S匹配非空字符</p>
#####<p >&emsp;&emsp;&emsp;&emsp;说明：空字符是指 空格 \r回车符 \n换行符 \t制表符 \v垂直制表符 \f换页符 </p>
###<p >&emsp;&emsp;匹配开头结尾位置</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：\A\Z</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：\A匹配开头位置，\Z匹配结尾位置</p>
###<p >&emsp;&emsp;匹配（非）单词的边界位置</p>
#####<p >&emsp;&emsp;&emsp;&emsp;元字符：\b\B</p>
#####<p >&emsp;&emsp;&emsp;&emsp;匹配规则：\b匹配单词边界，\B匹配非单词边界</p>
#####<p >&emsp;&emsp;&emsp;&emsp;说明：单词边界指数字字母（汉字）下划线与其他字符的交界位置</p>
#<p >&emsp;&emsp;&emsp;&emsp;类别&emsp;&emsp;&emsp;&emsp;元字符</p>
###<p >&emsp;&emsp;&emsp;&emsp;匹配字符&emsp;&emsp;&emsp;&emsp; .[...][^...]\d\D\w\W\s\S</p>
###<p >&emsp;&emsp;&emsp;&emsp;匹配重复&emsp;&emsp;&emsp;&emsp; *+？{n}{m,n}</p>
###<p >&emsp;&emsp;&emsp;&emsp;匹配位置&emsp;&emsp;&emsp;&emsp; ^$\A\Z\b\B</p>
###<p >&emsp;&emsp;&emsp;&emsp;其他&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | ()\</p>
#正则表达式的转义
###<p >&emsp;&emsp;1.如果使用正则表达式匹配特殊字符则需要加\表示转义。</p>
##<p >&emsp;&emsp;&emsp;&emsp;特殊字符：.&emsp;*&emsp;+&emsp;?&emsp;^&emsp;$&emsp;[]&emsp;()&emsp;{}&emsp;|&emsp;\</p>
###<p >&emsp;&emsp;2.在编程语言中，常使用原生字符串书写正则表达式避免多重转义的麻烦。</p>
#贪婪模式和非贪婪模式
##<p >&emsp;&emsp;1.定义</p>
###<p >&emsp;&emsp;&emsp;贪婪模式:默认情况下，匹配重复的元字符总是尽可能多的向后匹配内容。比如：*+?{m,n}</p>
###<p >&emsp;&emsp;&emsp;非贪婪模式（懒惰模式）:让匹配重复的元字符尽可能少的向后匹配内容。</p>
##<p >&emsp;&emsp;2.贪婪模式转换为非贪婪模式--在匹配重复元字符后加"?"号即可</p>
#正则表达式分组
##<p >&emsp;&emsp;1.定义</p>
###<p >&emsp;&emsp;&emsp;在正则表达式中，以（）建立正则表达式的内部分组，子组是正则表达式的一部分，可以作为内部整体操作对象</p>
##<p >&emsp;&emsp;2.作用</p>
###<p >&emsp;&emsp;&emsp;·可以被作为整体操作，改变元字符的操作对象</p>
###<p >&emsp;&emsp;&emsp;·可以通过编程语言某些接口获取匹配内容中，子组对应的内容部分</p>
##<p >&emsp;&emsp;3.捕获组</p>
###<p >&emsp;&emsp;&emsp;可以给正则表达式的子组起一个名字，表达该子组的意义。这种有名称的子组即为捕获组。</p>
##<p >&emsp;&emsp;4.注意事项</p>
###<p >&emsp;&emsp;&emsp;·一个正则表达式中可以包含多个子组</p>
###<p >&emsp;&emsp;&emsp;·子组可以嵌套，但是不要重叠或者嵌套结构复杂</p>
###<p >&emsp;&emsp;&emsp;·子组序列号一般从外到内，从左到右计数</p>
#正则表达式匹配原则
###<p >&emsp;&emsp;&emsp;1.正确性，能够正确的匹配出目标字符串</p>
###<p >&emsp;&emsp;&emsp;2.排他性，除了目标字符串外尽可能少的匹配其他内容</p>
###<p >&emsp;&emsp;&emsp;3.全面性，尽可能考虑到目标字符串的所有情况，不遗漏</p>
#Python re模块使用
###<p >&emsp;&emsp;参考代码，re.py/regex.py
