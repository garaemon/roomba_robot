cmake_minimum_required(VERSION 2.8.3)
project(roomba_500_series)


# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)
find_package(catkin REQUIRED COMPONENTS geometry_msgs actionlib_msgs cereal_port)
add_message_files(
  DIRECTORY msg
  FILES Battery.msg
  Buttons.msg
  RoombaIR.msg
  Note.msg
  IRCharacter.msg
  DigitLeds.msg
  Brushes.msg
  WheelDrop.msg
  Diagnostic.msg
  ScheduleLeds.msg
  Song.msg
  RoombaSwitch.msg
  Leds.msg
  PlaySong.msg
  Bumper.msg
  )



add_action_files(
  DIRECTORY action
  FILES GoDock.action
)

generate_messages(
  DEPENDENCIES geometry_msgs actionlib_msgs
)

catkin_package(
  DEPENDS
  CATKIN_DEPENDS geometry_msgs actionlib_msgs
  )

add_library(irobot_oi SHARED src/iRobot/OpenInterface.cpp)
add_library(go_dock SHARED src/GoDock/GoDock.cpp)
target_link_libraries(go_dock ${catkin_LIBRARIES})
target_link_libraries(irobot_oi ${catkin_LIBRARIES})
# rosbuild_add_executable(roomba560_node src/roomba560.cpp src/iRobot/OpenInterface.cpp src/GoDock/GoDock.cpp)
# target_link_libraries(roomba560_node cereal_port)

# rosbuild_add_executable(roomba500_light_node src/roomba500_lightweight.cpp src/iRobot/OpenInterface.cpp)
# target_link_libraries(roomba500_light_node cereal_port)

# rosbuild_add_executable(godock_server src/godock_server.cpp src/GoDock/GoDock.cpp)
# rosbuild_add_executable(godock_client src/godock_client.cpp)

