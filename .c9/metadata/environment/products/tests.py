{"filter":false,"title":"tests.py","tooltip":"/products/tests.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":1,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["","# Create your tests here.",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":12,"column":53},"action":"insert","lines":["from .models import Product","","# Create your tests here.","class ProductTests(TestCase):","    \"\"\"","    Here we'll define the tests that we'll run against our","    Product model","    \"\"\"","","    def test_str(self):","        test_name = Product(name='A product')","        self.assertEqual(str(test_name), 'A product')"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":53},"end":{"row":12,"column":53},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":89,"mode":"ace/mode/python"}},"timestamp":1565099263473,"hash":"4809a80f81413f451ad8d33e28eafd93b9156a14"}