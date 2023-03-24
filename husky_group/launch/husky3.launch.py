from symbol import parameters
import math
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

#test Fra lars
def generate_launch_description():

    
    urdf_extras_path = PathJoinSubstitution([
        FindPackageShare("husky_group"), "urdf", "husky_urdf_extras.urdf"        
    ])

    config_control = PathJoinSubstitution(
        [FindPackageShare("husky_group"),
        "params",
        "control.yaml"],
    )
    
    config_localization = PathJoinSubstitution(
        [FindPackageShare('husky_group'),
        'params',
        'localization.yaml'],
    )

    config_teleop_interactive_markers = PathJoinSubstitution(
        [FindPackageShare("husky_group"),
        "params",
        "teleop_interactive_markers.yaml"],
    )

    config_teleop_logitech = PathJoinSubstitution(
        [FindPackageShare("husky_group"),
        "params",
        "teleop_logitech.yaml"],
    )

    config_twist_mux = PathJoinSubstitution(
        [FindPackageShare("husky_group"),
        "params",
        "twist_mux.yaml"],
    )
    
    # Launch the husky robot using the husky_uia uia_master_husky repo
    launch_husky_base = GroupAction(
        actions=[
            PushRosNamespace('husky'),  
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(PathJoinSubstitution(
                [FindPackageShare("husky_base"), 'launch', 'base_launch.py'])),
                launch_arguments ={
                    "urdf_extras" : urdf_extras_path,
                    "control_params" : config_control,
                    "localization_params" : config_localization,
                    "teleop_interactive_markers_paramas" : config_teleop_interactive_markers,
                    "teleop_logitech_params" : config_teleop_logitech,
                    "twist_mux_params" : config_twist_mux,
                }.items()
            ),
        ]
    )

    ld = LaunchDescription()

    # Launch pointcloud to laserscan, imu and lidar

    # Launch Husky UGV
    ld.add_action(launch_husky_base)

    return ld

