cmake_minimum_required(VERSION 3.8)
project(rover-v1)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)

# Add executables
add_executable(motor_controller_node src/motor_controller_node.cpp)
ament_target_dependencies(motor_controller_node rclcpp std_msgs geometry_msgs)

add_executable(lidar_node src/lidar_node.cpp)
ament_target_dependencies(lidar_node rclcpp sensor_msgs std_msgs)

add_executable(imu_node src/imu_node.cpp)
ament_target_dependencies(imu_node rclcpp sensor_msgs std_msgs)

add_executable(camera_node src/camera_node.cpp)
ament_target_dependencies(camera_node rclcpp sensor_msgs std_msgs)

add_executable(exploration_node src/exploration_node.cpp)
ament_target_dependencies(exploration_node rclcpp sensor_msgs geometry_msgs)

# Install executables
install(TARGETS
  motor_controller_node
  lidar_node
  imu_node
  camera_node
  exploration_node
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()