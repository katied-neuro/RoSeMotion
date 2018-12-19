################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    def on_init(self, controller):
        print("Initialized")

    def on_connect(self, controller):
        print("Connected")

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print("Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
        #       frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))

        # Get hands
        for hand in frame.hands:

            fingerlist = hand.fingers.finger_type(Leap.Finger.TYPE_INDEX)
            bone_next = fingerlist[0].bone(Leap.Bone.TYPE_PROXIMAL)
            bone_prev = fingerlist[0].bone(Leap.Bone.TYPE_METACARPAL)

            matrix = Leap.Matrix(bone_prev.basis.x_basis, bone_prev.basis.y_basis, bone_prev.basis.z_basis)
            print(matrix.to_array_4x4())

            # bone_vec.angle_to(prev_bone.basis.x_basis)
            if hand.is_valid and fingerlist[0].is_valid:
                basis_prev = bone_prev.basis
                basis_next = bone_next.basis
            #     print("x = [{}; {}; {}];".format(hand.basis.x_basis.x, hand.basis.x_basis.y, hand.basis.x_basis.z))
            #     print("y = [{}; {}; {}];".format(hand.basis.y_basis.x, hand.basis.y_basis.y, hand.basis.y_basis.z))
            #     print("z = [{}; {}; {}];".format(hand.basis.z_basis.x, hand.basis.z_basis.y, hand.basis.z_basis.z))
                print("x_prev = [{}; {}; {}];".format(basis_prev.x_basis.x, basis_prev.x_basis.y, basis_prev.x_basis.z))
                print("y_prev = [{}; {}; {}];".format(basis_prev.y_basis.x, basis_prev.y_basis.y, basis_prev.y_basis.z))
                print("z_prev = [{}; {}; {}];".format(basis_prev.z_basis.x, basis_prev.z_basis.y, basis_prev.z_basis.z))
                
                print("x_next = [{}; {}; {}];".format(basis_next.x_basis.x, basis_next.x_basis.y, basis_next.x_basis.z))
                print("y_next = [{}; {}; {}];".format(basis_next.y_basis.x, basis_next.y_basis.y, basis_next.y_basis.z))
                print("z_next = [{}; {}; {}];".format(basis_next.z_basis.x, basis_next.z_basis.y, basis_next.z_basis.z))
            
            
                # print("x = {}, y = {}, z
            #  = {}".format(
                #     hand.basis.x_basis.angle_to(hand.arm.basis.x_basis) * Leap.RAD_TO_DEG,
                #     hand.basis.y_basis.angle_to(hand.arm.basis.y_basis) * Leap.RAD_TO_DEG,
                #     hand.basis.z_basis.angle_to(hand.arm.basis.z_basis) * Leap.RAD_TO_DEG))
                # sys.stdout.write("\rx = %4f, y = %4f, z = %4f" % (
                #     bone_next.basis.x_basis.angle_to(bone_prev.basis.x_basis) * Leap.RAD_TO_DEG,
                #     bone_next.basis.y_basis.angle_to(bone_prev.basis.y_basis) * Leap.RAD_TO_DEG,
                #     bone_next.basis.z_basis.angle_to(bone_prev.basis.z_basis) * Leap.RAD_TO_DEG))
                # sys.stdout.flush()
                # time.sleep(0.01)
            # handType = "Left hand" if hand.is_left else "Right hand"
            #
            # print "  %s, id %d, position: %s" % (
            #     handType, hand.id, hand.palm_position)
            #
            # # Get the hand's normal vector and direction
            # normal = hand.palm_normal
            # direction = hand.direction
            #
            # # Calculate the hand's pitch, roll, and yaw angles
            # print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
            #     direction.pitch * Leap.RAD_TO_DEG,
            #     normal.roll * Leap.RAD_TO_DEG,
            #     direction.yaw * Leap.RAD_TO_DEG)
            #
            # # Get arm bone
            # arm = hand.arm
            # print "  Arm direction: %s, wrist position: %s, elbow position: %s" % (
            #     arm.direction,
            #     arm.wrist_position,
            #     arm.elbow_position)
            #
            # # Get fingers
            # for finger in hand.fingers:
            #
            #     print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
            #         self.finger_names[finger.type],
            #         finger.id,
            #         finger.length,
            #         finger.width)
            #
            #     # Get bones
            #     for b in range(0, 4):
            #         bone = finger.bone(b)
            #         print "      Bone: %s, start: %s, end: %s, direction: %s" % (
            #             self.bone_names[bone.type],
            #             bone.prev_joint,
            #             bone.next_joint,
            #             bone.direction)

        # if not frame.hands.is_empty:
            # print("")

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
