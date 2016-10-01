Name:           ros-kinetic-trajectory-msgs
Version:        1.12.5
Release:        0%{?dist}
Summary:        ROS trajectory_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/trajectory_msgs
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-rosbag-migration-rule
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-std-msgs

%description
This package defines messages for defining robot trajectories. These messages
are also the building blocks of most of the control_msgs actions.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Sep 30 2016 Tully Foote <tfoote@osrfoundation.org> - 1.12.5-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Tully Foote <tfoote@osrfoundation.org> - 1.12.4-0
- Autogenerated by Bloom

