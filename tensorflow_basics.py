# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:27:35 2017

@author: DerekBroadhead

Basic tensorflow layout and design
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Standard Libraries
import six # Best for compatability
import tensorflow as tf


# Basic node overview
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
print(node1, node2) # Expected return is the descriptors for the nodes

# Basic display overview
sess = tf.Session()
print('sess.run([node1, node1]): {}'.format(sess.run([node1, node2])))

# Basic graph overview
node3 = tf.add(node1, node2)
print('node3: {}'.format(node3))
print('sess.run([node3]): {}'.format(sess.run([node3])))

