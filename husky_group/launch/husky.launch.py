import os
import math
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, Command, FindExecutable
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

urdf_extras_path = PathJoinSubstitution(
            [FindPackageShare("husky_group"), "urdf", "husky_urdf_extras.urdf"]
) 

os.environ["CPR_URDF_EXTRAS"] = str(urdf_extras_path)
os.environ["HUSKY_TOP_PLATE_ENABLED"] = "true"
#os.environ["HUSKY_SERIAL_PORT"] = "/dev/prolific"

""" 
def generate_launch_description():

    # Get LIDAR parameters
    lidar_params = PathJoinSubstitution(
        [FindPackageShare('husky_group'),
        'params',
        'ouster_lidar.yaml'],
    )

    config_husky_ekf = PathJoinSubstitution(
        [FindPackageShare('husky_group'),
        'params',
        'localization.yaml'],
    )

    

    config_husky_velocity_controller = PathJoinSubstitution(
        [FindPackageShare("husky_group"),
        "params",
        "control.yaml"],
    )
    
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [FindPackageShare("husky_description"), "urdf", "husky.urdf.xacro"]
            ),
            " ",
            "name:=husky",
            " ",
            "prefix:=''",
            " ",
        ]
    )
    robot_description = {"robot_description": robot_description_content}

    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    node_controller_manager = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, config_husky_velocity_controller],
        output={
            "stdout": "screen",
            "stderr": "screen",
        },
    )

    spawn_controller = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["joint_state_broadcaster"],
        output="screen",
    )

    spawn_husky_velocity_controller = Node(
        package="controller_manager",
        executable="spawner.py",
        arguments=["husky_velocity_controller"],
        output="screen",
    )
    
    node_ekf = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_node',
        output='screen',
        parameters=[config_husky_ekf],
        )

    config_imu_filter = PathJoinSubstitution(
        [FindPackageShare('husky_control'),
        'config',
        'imu_filter.yaml'],
    )

    node_imu_filter = Node(
        package='imu_filter_madgwick',
        executable='imu_filter_madgwick_node',
        name='imu_filter',
        output='screen',
        parameters=[config_imu_filter]
    )
        

    # Launch husky_control/teleop_base.launch.py which is various ways to tele-op
    # the robot but does not include the joystick. Also, has a twist mux.
    launch_husky_teleop_base = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution(
        [FindPackageShare("husky_control"), 'launch', 'teleop_base.launch.py'])))

    # Launch husky_control/teleop_joy.launch.py which is tele-operation using a physical joystick.
    launch_husky_teleop_joy = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution(
        [FindPackageShare("husky_control"), 'launch', 'teleop_joy.launch.py'])))


    # Launch husky_bringup/accessories.launch.py which is the sensors commonly used on the Husky.
    launch_husky_accessories = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution(
        [FindPackageShare("husky_bringup"), 'launch', 'accessories.launch.py'])))



    #Launch the UM7 IMU
    node_um7_imu = Node(
        package="um7",
        executable="um7_node",
        output="screen",
    )


    #Launch the LIDAR
    launch_ouster_lidar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution(
        [FindPackageShare("ros2_ouster"), 'launch', 'os1_launch.py'])),
        launch_arguments ={
            "params_file" : lidar_params
        }.items()
    )


    #Launch the pointcloud to laserscan package
    node_pointcloud_to_laserscan =  Node(
    	name="pointcloud_to_laserscan",
        package="pointcloud_to_laserscan",
        remappings=[('cloud_in', '/points')],
        executable="pointcloud_to_laserscan_node",
        parameters=[{
        'target_frame': 'base_laser',
        'transform_tolerance': 0.01,
        'min_height': -0.50,
        'max_height': 0.2,
        'angle_min': -math.pi,  # -M_PI/2
        'angle_max': math.pi,  # M_PI/2
        'angle_increment': 0.0087,  # M_PI/360.0
        'scan_time': 0.3333,
        'range_min': 0.8,
        'range_max': 120.0,
        'use_inf': True,
        'inf_epsilon': 1.0,
        }]
    )


    ld = LaunchDescription()

    # Launch pointcloud to laserscan, imu and lidar
    ld.add_action(node_pointcloud_to_laserscan)
    ld.add_action(node_um7_imu)
    ld.add_action(launch_ouster_lidar)
    
    # Launch Husky UGV
    ld.add_action(node_robot_state_publisher)
    ld.add_action(node_controller_manager)
    ld.add_action(spawn_controller)
    ld.add_action(spawn_husky_velocity_controller)
    ld.add_action(node_ekf)
    ld.add_action(node_imu_filter)
    ld.add_action(launch_husky_teleop_base)
    ld.add_action(launch_husky_teleop_joy)
    ld.add_action(launch_husky_accessories)

    return ld

 """