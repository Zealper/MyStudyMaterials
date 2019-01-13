# coding=utf-8


class Test1(object):

    def __init__(self, number):
        self.number = number

    def tenant(self):
        print("I'm tenant {}".format(self.number))
        tenant_id = "I'm tenant id {}".format(self.number)
        tenant_token = "I'm tenant token {}".format(self.number)
        return tenant_id, tenant_token
