# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /snap/clion/100/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /snap/clion/100/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/nikkie/Documents/HackBG/Sensors

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/nikkie/Documents/HackBG/Sensors/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/Sensors.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Sensors.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Sensors.dir/flags.make

CMakeFiles/Sensors.dir/main.cpp.o: CMakeFiles/Sensors.dir/flags.make
CMakeFiles/Sensors.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/nikkie/Documents/HackBG/Sensors/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Sensors.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Sensors.dir/main.cpp.o -c /home/nikkie/Documents/HackBG/Sensors/main.cpp

CMakeFiles/Sensors.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Sensors.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/nikkie/Documents/HackBG/Sensors/main.cpp > CMakeFiles/Sensors.dir/main.cpp.i

CMakeFiles/Sensors.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Sensors.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/nikkie/Documents/HackBG/Sensors/main.cpp -o CMakeFiles/Sensors.dir/main.cpp.s

CMakeFiles/Sensors.dir/sensor.cpp.o: CMakeFiles/Sensors.dir/flags.make
CMakeFiles/Sensors.dir/sensor.cpp.o: ../sensor.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/nikkie/Documents/HackBG/Sensors/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/Sensors.dir/sensor.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Sensors.dir/sensor.cpp.o -c /home/nikkie/Documents/HackBG/Sensors/sensor.cpp

CMakeFiles/Sensors.dir/sensor.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Sensors.dir/sensor.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/nikkie/Documents/HackBG/Sensors/sensor.cpp > CMakeFiles/Sensors.dir/sensor.cpp.i

CMakeFiles/Sensors.dir/sensor.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Sensors.dir/sensor.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/nikkie/Documents/HackBG/Sensors/sensor.cpp -o CMakeFiles/Sensors.dir/sensor.cpp.s

CMakeFiles/Sensors.dir/sensors.cpp.o: CMakeFiles/Sensors.dir/flags.make
CMakeFiles/Sensors.dir/sensors.cpp.o: ../sensors.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/nikkie/Documents/HackBG/Sensors/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/Sensors.dir/sensors.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Sensors.dir/sensors.cpp.o -c /home/nikkie/Documents/HackBG/Sensors/sensors.cpp

CMakeFiles/Sensors.dir/sensors.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Sensors.dir/sensors.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/nikkie/Documents/HackBG/Sensors/sensors.cpp > CMakeFiles/Sensors.dir/sensors.cpp.i

CMakeFiles/Sensors.dir/sensors.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Sensors.dir/sensors.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/nikkie/Documents/HackBG/Sensors/sensors.cpp -o CMakeFiles/Sensors.dir/sensors.cpp.s

# Object files for target Sensors
Sensors_OBJECTS = \
"CMakeFiles/Sensors.dir/main.cpp.o" \
"CMakeFiles/Sensors.dir/sensor.cpp.o" \
"CMakeFiles/Sensors.dir/sensors.cpp.o"

# External object files for target Sensors
Sensors_EXTERNAL_OBJECTS =

Sensors: CMakeFiles/Sensors.dir/main.cpp.o
Sensors: CMakeFiles/Sensors.dir/sensor.cpp.o
Sensors: CMakeFiles/Sensors.dir/sensors.cpp.o
Sensors: CMakeFiles/Sensors.dir/build.make
Sensors: CMakeFiles/Sensors.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/nikkie/Documents/HackBG/Sensors/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable Sensors"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Sensors.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Sensors.dir/build: Sensors

.PHONY : CMakeFiles/Sensors.dir/build

CMakeFiles/Sensors.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Sensors.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Sensors.dir/clean

CMakeFiles/Sensors.dir/depend:
	cd /home/nikkie/Documents/HackBG/Sensors/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nikkie/Documents/HackBG/Sensors /home/nikkie/Documents/HackBG/Sensors /home/nikkie/Documents/HackBG/Sensors/cmake-build-debug /home/nikkie/Documents/HackBG/Sensors/cmake-build-debug /home/nikkie/Documents/HackBG/Sensors/cmake-build-debug/CMakeFiles/Sensors.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Sensors.dir/depend

