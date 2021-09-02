import json
from application import app
import pytest
    
class TestClass():
    def setup_class(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def teardown_class(self):
        pass
        
    #test case: / endpoint
    def test_hello(self):
        response = self.app.get('/')
        
        assert response.status_code == 200
        assert response.data == b'Hello!!!'
        assert response.mimetype == 'text/html'

     
    #test case: /add endpoint (valid input)
    def test_add1(self):
        response = self.app.get('/add?op1=3&op2=4')
        
        if (not response.is_json):
            pytest.fail("Response is not json object!")
      
        j = response.get_json() #j is dict type
        expected_output = {"operand 1":3, "operand 2":4, "sum":7}
        
        assert response.status_code == 200
        assert response.mimetype == 'application/json'
        assert j == expected_output
       
           
    #test case: /add endpoint (missing operand)
    def test_add2(self):
        response = self.app.get('/add?op1=3')
       
        assert response.status_code == 400
        assert response.is_json
        assert response.mimetype == 'application/json'
        
        j = response.get_json() #j is dict type
        assert j ==  {'error': 'missing parameter(s)'}
        
    def test_mul1(self):
        http_body = json.dumps({"op1":3,"op2":5})
        
        response = self.app.post('/mul',
                data=http_body,
                content_type='application/json')
                
        assert response.status_code == 200
        assert response.is_json
        
        j = response.get_json() #j is dict type
        assert j == {'mul': 15}
        
        
   