# coding=utf-8

from CookBookLearning.ClassTestCase.VolumeAction import TenantAction


def many_tenant():
    TenantAction(1).create_volume()
    TenantAction(2).create_volume()
    TenantAction(3).create_volume()


if __name__ == '__main__':
    many_tenant()
