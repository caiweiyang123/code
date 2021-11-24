"""
    三大特征：
        封装：将每种影响效果单独做成类
        继承：将各种影响技能效果抽象为SkillImpactEffect
                隔离技能释放器与各种影响效果的变化了
        多态：各种影响效果再重写SkillImpactEffect中impact方法
                释放器调用SkillImpactEffect执行各种效果
    六大原则：
        开闭：增加新技能效果，不修改释放器代码
        单一职责：SkillImpactEffect 负责隔离变化
                DamageEffect 负责定义具体效果
                SkillDeployer 负责释放技能
        依赖倒置：释放器没有调用具体效果，而是调用SkillImpactEffect
                抽象的不依赖具体的
                释放器通过”依赖注入“（读取配置文件，创建影响效果对象）
                释放器不依赖具体影响效果

        组合复用：释放器与影响效果是组合关系
                可以灵活的选择各种影响效果
        里氏替换：（1）父出现的地方可以被子类替换
                释放器存储影响效果列表，实际可以将各种子类存进来
        迪米特法则：低耦合所有类之间的耦合度都很低
"""
class SkillImpactEffect:
    """
        技能影响效果
    """

    def impact(self):
        raise NotImplementedError()


class DamageEffect(SkillImpactEffect):
    """
        伤害生命效果
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("扣你%d血" % self.value)


class LowerDeffenseEffect(SkillImpactEffect):
    """
        降低防御力
    """

    def __init__(self, value, time):
        self.value = value
        self.time = time

    def impact(self):
        print("降低%d防御力，持续%d秒" % (self.value, self.time))


class DizzinessEffect(SkillImpactEffect):
    """
        眩晕
    """

    def __init__(self, time):
        self.time = time

    def impact(self):
        print("眩晕持续%d秒" % (self.time))

class SkillDeployer:
    """
        技能释放器
    """


    def __init__(self,name):
        self.name = name
        # 加载配置文件{技能名称：[效果一，效果二，效果三...]}
        self.__dict_skill_config=self.__load_config_file()
        # 创建效果对象
        self.__effect_object = self.__create_effect_objects()
    def __load_config_file(self):
        """
            加载文件
        """
        return {
            "降龙十八掌":["DamageEffect(200)","LowerDeffenseEffect(-10,5)","DizzinessEffect(2)"],
            "六脉神剑":["DamageEffect(100)","LowerDeffenseEffect(-5,5)"]
        }

    def __create_effect_objects(self):
        # 根据name创建相应的技能对象
        list_effect_name = self.__dict_skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            effect_object = eval(item)
            list_effect_object.append(effect_object)
        return list_effect_object

    # 生成技能（执行效果）
    def generate_skill(self):
        print("技能释放啦！")
        for item in self.__effect_object:
            item.impact()

if __name__ == '__main__':
    xlsbz = SkillDeployer("降龙十八掌")
    xlsbz.generate_skill()
    print("-"*50)
    lmsj = SkillDeployer("六脉神剑")
    lmsj.generate_skill()