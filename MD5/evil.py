#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """          \�QX���#��P�IFjJ"���3�C�������m1�g˙3x�M�<�-��q�7K�� (m�m���0�/�N���
��!����Mb]�GI��![��l�ϫ�n��@Ƥ�ϡ�$�T\�
"""

from hashlib import sha256
h = sha256(blob).hexdigest()

print "I come in peace"

if h == "0223d6aba4d0fb4826300d17315275523c8b23f912b031afa88e6e368b1f5a2a":
	print "Prepare to be destroyed"