cmake_minimum_required(VERSION 2.8.3)
project(roomba_500_series)


# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)
find_package(catkin REQUIRED COMPONENTS geometry_msgs actionlib_msgs cereal_port tf nav_msgs)
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
include_directories(include ${catkin_INCLUDE_DIRS})
add_library(irobot_oi SHARED src/iRobot/OpenInterface.cpp)
add_dependencies(irobot_oi ${PROJECT_NAME}_gencpp)
target_link_libraries(irobot_oi ${catkin_LIBRARIES})

add_library(go_dock SHARED src/GoDock/GoDock.cpp)
target_link_libraries(go_dock ${catkin_LIBRARIES})
add_dependencies(go_dock ${PROJECT_NAME}_gencpp)

add_executable(roomba560_node src/roomba560.cpp src/iRobot/OpenInterface.cpp src/GoDock/GoDock.cpp)
target_link_libraries(roomba560_node ${catkin_LIBRARIES})
add_dependencies(roomba560_node ${PROJECT_NAME}_gencpp)

add_executable(roomba500_light_node src/roomba500_lightweight.cpp src/iRobot/OpenInterface.cpp)
target_link_libraries(roomba500_light_node ${catkin_LIBRARIES})
add_dependencies(roomba500_light_node ${PROJECT_NAME}_gencpp)

add_executable(godock_server src/godock_server.cpp src/GoDock/GoDock.cpp)
target_link_libraries(godock_server ${catkin_LIBRARIES})
add_dependencies(godock_server ${PROJECT_NAME}_gencpp)

add_executable(godock_client src/godock_client.cpp)
target_link_libraries(godock_client ${catkin_LIBRARIES})
add_dependencies(godock_client ${PROJECT_NAME}_gencpp)

install(TARGETS godock_client godock_server roomba500_light_node roomba560_node irobot_oi go_dock
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
        ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION})

install(DIRECTORY include/${PROJECT_NAME}/
        DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION})
