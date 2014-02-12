cmake_minimum_required(VERSION 2.8.3)
project(cereal_port)

find_package(catkin REQUIRED COMPONENTS roscpp)
catkin_package(
  DEPENDS
  CATKIN_DEPENDS roscpp
  INCLUDE_DIRS include
  LIBRARIES cereal_port
  )

include_directories(include ${catkin_INCLUDE_DIRS})
add_library(cereal_port SHARED src/CerealPort.cpp)
target_link_libraries(cereal_port ${catkin_LIBRARIES})

install(DIRECTORY include/${PROJECT_NAME}/
        DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION})
install(TARGETS cereal_port
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
        ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION})
