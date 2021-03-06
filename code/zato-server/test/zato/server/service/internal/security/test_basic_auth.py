# -*- coding: utf-8 -*-

"""
Copyright (C) 2013 Dariusz Suchojad <dsuch at zato.io>

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# Bunch
from bunch import Bunch

# Zato
from zato.common import zato_namespace
from zato.common.test import rand_bool, rand_int, rand_string, ServiceTestCase
from zato.server.service.internal.security.basic_auth import GetList, Create, Edit, ChangePassword, Delete

################################################################################

class GetListTestCase(ServiceTestCase):
    
    def setUp(self):
        self.service_class = GetList
        self.sio = self.service_class.SimpleIO
    
    def get_request_data(self):
        return {'cluster_id': rand_int()}
    
    def get_response_data(self):
        return Bunch({'id':rand_int(), 'name':self.name, 'is_active':rand_bool(), 'username':rand_string(),
             'realm':rand_string()}
        )
    
    def test_sio(self):
        self.assertEquals(self.sio.request_elem, 'zato_security_basic_auth_get_list_request')
        self.assertEquals(self.sio.response_elem, 'zato_security_basic_auth_get_list_response')
        self.assertEquals(self.sio.input_required, ('cluster_id',))
        self.assertEquals(self.sio.output_required, ('id', 'name', 'is_active', 'username', 'realm'))
        self.assertEquals(self.sio.namespace, zato_namespace)
        self.assertRaises(AttributeError, getattr, self.sio, 'input_optional')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_optional')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_repeated')
        
    def test_impl(self):
        self.assertEquals(self.service_class.get_name(), 'zato.security.basic-auth.get-list')
        
##############################################################################

class CreateTestCase(ServiceTestCase):
    
    def setUp(self):
        self.service_class = Create
        self.sio = self.service_class.SimpleIO      
    
    def get_request_data(self):
        return {'cluster_id':rand_int(), 'name':rand_string(), 'is_active':rand_bool(), 'username':rand_string(), 'realm':rand_string()}
    
    def get_response_data(self):
        return Bunch({'id':rand_int(), 'name':rand_string()})
    
    def test_sio(self):
        self.assertEquals(self.sio.request_elem, 'zato_security_basic_auth_create_request')
        self.assertEquals(self.sio.response_elem, 'zato_security_basic_auth_create_response')
        self.assertEquals(self.sio.input_required,('cluster_id', 'name', 'is_active', 'username', 'realm'))
        self.assertEquals(self.sio.output_required, ('id', 'name'))
        self.assertEquals(self.sio.namespace, zato_namespace)
        self.assertRaises(AttributeError, getattr, self.sio, 'input_optional')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_optional')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_repeated')
        
        def test_impl(self):
            self.assertEquals(self.service_class.get_name(), 'zato.security.basic-auth.create')
       
###############################################################################
class EditTestCase(ServiceTestCase):
    
    def setUp(self):
        self.service_class = Edit
        self.sio = self.service_class.SimpleIO
    
    def get_request_data(self):
        return ({'id':rand_int(), 'cluster_id':rand_int(), 'name':rand_string(), 'is_active':rand_bool(),
                 'username':rand_string(), 'realm':rand_string()})
        
    def get_response_data(self):
        return Bunch({'id':rand_int(), 'name':rand_string()})        
    
    def test_sio(self):
        
        self.assertEquals(self.sio.request_elem, 'zato_security_basic_auth_edit_request')
        self.assertEquals(self.sio.response_elem, 'zato_security_basic_auth_edit_response')
        self.assertEquals(self.sio.input_required, ('id', 'cluster_id', 'name', 'is_active', 'username', 'realm'))
        self.assertEquals(self.sio.output_required, ('id', 'name'))
        self.assertEquals(self.sio.namespace, zato_namespace)
        self.assertRaises(AttributeError, getattr, self.sio, 'input_optional')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_optional')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_repeated')
        
    def test_impl(self):
        self.assertEquals(self.service_class.get_name(), 'zato.security.basic-auth.edit')
        
############################################################################### 
           
class ChangePasswordTestCase(ServiceTestCase):
    
    def setUp(self):
        self.service_class = ChangePassword
        self.sio = self.service_class.SimpleIO
    
    def get_request_data(self):
        return {'id':rand_int(), 'password1':rand_string(), 'password2':rand_string()}
    
    def get_response_data(self):
        return Bunch()    
    
    def test_sio(self):
        self.assertEquals(self.sio.request_elem, 'zato_security_basic_auth_change_password_request')
        self.assertEquals(self.sio.response_elem, 'zato_security_basic_auth_change_password_response')
        self.assertEquals(self.sio.input_required, ('id',))
        self.assertEquals(self.sio.namespace, zato_namespace)
        self.assertRaises(AttributeError, getattr, self.sio, 'input_optional')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_required')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_optional')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_repeated')
        
    def test_impl(self):
        self.assertEquals(self.service_class.get_name(), 'zato.security.basic-auth.change-password')

##############################################################################

class DeleteTestCase(ServiceTestCase):
    
    def setUp(self):
        self.service_class = Delete
        self.sio = self.service_class.SimpleIO
  
    def get_request_data(self):
        return {'id': rand_int()}
    
    def get_response_data(self):
        return Bunch()
    
    def test_sio(self):
        self.assertEquals(self.sio.request_elem, 'zato_security_basic_auth_delete_request')
        self.assertEquals(self.sio.response_elem, 'zato_security_basic_auth_delete_response')
        self.assertEquals(self.sio.input_required, ('id',))
        self.assertEquals(self.sio.namespace, zato_namespace)
        self.assertRaises(AttributeError, getattr, self.sio, 'input_optional')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_required')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_optional')
        self.assertRaises(AttributeError, getattr, self.sio, 'output_repeated')
        
    def test_impl(self):
        self.assertEquals(self.service_class.get_name(), 'zato.security.basic-auth.delete')
