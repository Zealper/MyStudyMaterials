from CookBookLearning.ClassTestCase.Authentication import Test1


class TenantAction(object):

    def __init__(self, number):
        self.tenant_id, self.tenant_token = Test1(number).tenant()

    def create_volume(self):
        print('creating volume')
        print(self.tenant_token, self.tenant_id)
