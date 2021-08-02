class Service:
    instance1, instance2 = None, None
    calls = False

    def __init__(self, instanceNum) -> None:
        self.instanceNum = instanceNum

    @staticmethod
    def init():
        Service.instance1 = Service('1')
        Service.instance2 = Service('2')

    @staticmethod
    def getService():
        if Service.instance1 is None:
            Service.init()

        if Service.calls:
            Service.calls = not Service.calls
            return Service.instance1

        Service.calls = not Service.calls
        return Service.instance2


if __name__ == '__main__':
    obj2 = Service.getService()
    assert obj2.instanceNum == '2'

    obj1 = Service.getService()
    assert obj1.instanceNum == '1'

    obj4 = Service.getService()
    assert obj4.instanceNum == '2'

    obj3 = Service.getService()
    assert obj3.instanceNum == '1'
