#! /usr/bin/env python

from gazebo_msgs.srv import GetModelState
import rospy
import time

class Block:
    def __init__(self, name, relative_entity_name):
        self._name = name
        self._relative_entity_name = relative_entity_name

class Tutorial:

    _blockListDict = {
        'block_a': Block('mybot', 'base_footprint'),
        'block_b': Block('mybot', 'garra1garraesquerda1'),

    }

    def show_gazebo_models(self):
        try:
            model_coordinates = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
            for block in self._blockListDict.itervalues():
                blockName = str(block._name)
                resp_coordinates = model_coordinates(blockName, block._relative_entity_name)

                print ('Status.success = ', resp_coordinates.success)
                print(blockName)
                print("Trackeando " + str(block._name))
                print("Valeur de X : " + str(resp_coordinates.pose.position.x))
                print("Quaternion X : " + str(resp_coordinates.pose.orientation.x))

        except rospy.ServiceException as e:
            rospy.loginfo("Get Model State service call failed:  {0}".format(e))


if __name__ == '__main__':
    while True:
        tuto = Tutorial()
        tuto.show_gazebo_models()
        time.sleep(3)