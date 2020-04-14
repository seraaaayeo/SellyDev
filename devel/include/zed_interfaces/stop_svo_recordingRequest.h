// Generated by gencpp from file zed_interfaces/stop_svo_recordingRequest.msg
// DO NOT EDIT!


#ifndef ZED_INTERFACES_MESSAGE_STOP_SVO_RECORDINGREQUEST_H
#define ZED_INTERFACES_MESSAGE_STOP_SVO_RECORDINGREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace zed_interfaces
{
template <class ContainerAllocator>
struct stop_svo_recordingRequest_
{
  typedef stop_svo_recordingRequest_<ContainerAllocator> Type;

  stop_svo_recordingRequest_()
    {
    }
  stop_svo_recordingRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> const> ConstPtr;

}; // struct stop_svo_recordingRequest_

typedef ::zed_interfaces::stop_svo_recordingRequest_<std::allocator<void> > stop_svo_recordingRequest;

typedef boost::shared_ptr< ::zed_interfaces::stop_svo_recordingRequest > stop_svo_recordingRequestPtr;
typedef boost::shared_ptr< ::zed_interfaces::stop_svo_recordingRequest const> stop_svo_recordingRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace zed_interfaces

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsMessage': True, 'IsFixedSize': True, 'HasHeader': False}
// {'zed_interfaces': ['/home/hyeok/workspace/catkin_ws/src/zed-ros-wrapper/zed_interfaces/msg'], 'std_msgs': ['/home/hyeok/ros_catkin_ws/install/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/home/hyeok/ros_catkin_ws/install/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsMessage< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "zed_interfaces/stop_svo_recordingRequest";
  }

  static const char* value(const ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct stop_svo_recordingRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::zed_interfaces::stop_svo_recordingRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // ZED_INTERFACES_MESSAGE_STOP_SVO_RECORDINGREQUEST_H
