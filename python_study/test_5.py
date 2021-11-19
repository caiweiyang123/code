import requests
import assertpy
import pytest


class Test(object):
    # ip = ["223.167.150.251", "223.167.150.220", "223.167.150.444"]
    # id = ["6006", "6007", "6008"]
    query = [("223.167.150.251", "6006"), ("223.167.150.220", "6007"), ("223.167.150.444", "6008")]

    @pytest.mark.parametrize("ip, id", query)
    # @pytest.mark.parametrize("ip", ip)
    # @pytest.mark.parametrize("id", id)
    def test_1(self, ip,id):
        url_2 = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php'

        params= {'query':ip,'resource_id':id}
        response = requests.get(url=url_2, params=params)
        print(response.json())
        assertpy.assert_that(response.json()['status']).is_equal_to('0')

