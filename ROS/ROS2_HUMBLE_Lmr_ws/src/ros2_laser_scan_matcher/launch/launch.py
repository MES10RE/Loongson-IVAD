#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_laser_scan_matcher',
            executable='laser_scan_matcher',  # 节点可执行文件名
            name='laser_scan_matcher',
            output='screen',
            parameters=[{
                'use_scan_matching': True,
                'use_tf_scan_transformation': True,
                'publish_tf': True,
                'base_frame': 'base_link',
                'odom_frame': 'odom',
                'fixed_frame': 'odom',
                'target_frame': 'base_link',
                'laser_frame': 'laser_link',
                'max_iterations': 10,
                'publish_pose': True,
                'publish_pose_stamped': True,
                'publish_pose_with_covariance': False,
                'publish_tf_transform': True,
                'use_correlative_scan_matching': False,
                'scan_topic': '/scan',
            }]
        )
    ])
