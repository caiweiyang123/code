"""
    技能系统
"""


class SkillImpactEffect:
    """
        技能影响效果
    """

    def impact(self):
        raise NotImplemented


class DamageEffect(SkillImpactEffect):
    def __init__(self, hp):
        self.hp = hp

    def impact(self):
        print("扣你%d血" % self.hp)


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
        print("眩晕持续%d秒" % self.time)


class SkillDeployer():
    """
        技能释放器
    """

    def __init__(self, name):
        self.name = name
        # 加载配置文件{技能名称:[效果一，效果二，。。]}
        self.__dict_skill_config = self.__load_config_file()
        # 创建效果对象
        self.__effect_object = self.__create_effect_objects()

    def __load_config_file(self):
        # 加载文件
        return {
            "降龙十八掌": ["DamageEffect(100)", "LowerDeffenseEffect(10,3)"],
            "六脉神剑": ["DamageEffect(100)", "DizzinessEffect(5)","LowerDeffenseEffect(10,3)"],
        }

    def __create_effect_objects(self):
        # 根据降龙十八掌拿到[效果1，效果2，效果3.。]
        list_effect_name = self.__dict_skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            list_effect_object.append(eval(item))
        return list_effect_object

    # 生成技能（执行效果）
    def generate_skill(self):
        for item in self.__effect_object:
            item.impact()

xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()
lmsj = SkillDeployer("六脉神剑")
lmsj.generate_skill()