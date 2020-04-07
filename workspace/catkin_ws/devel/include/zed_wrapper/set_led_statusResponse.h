// Generated by gencpp from file zed_wrapper/set_led_statusResponse.msg
// DO NOT EDIT!


#ifndef ZED_WRAPPER_MESSAGE_SET_LED_STATUSRESPONSE_H
#define ZED_WRAPPER_MESSAGE_SET_LED_STATUSRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace zed_wrapper
{
template <class ContainerAllocator>
struct set_led_statusResponse_
{
  typedef set_led_statusResponse_<ContainerAllocator> Type;

  set_led_statusResponse_()
    : done(false)  {
    }
  set_led_statusResponse_(const ContainerAllocator& _alloc)
    : done(false)  {
  (void)_alloc;
    }



   typedef uint8_t _done_type;
  _done_type done;





  typedef boost::shared_ptr< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> const> ConstPtr;

}; // struct set_led_statusResponse_

typedef ::zed_wrapper::set_led_statusResponse_<std::allocator<void> > set_led_statusResponse;

typedef boost::shared_ptr< ::zed_wrapper::set_led_statusResponse > set_led_statusResponsePtr;
typedef boost::shared_ptr< ::zed_wrapper::set_led_statusResponse const> set_led_statusResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace zed_wrapper

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsMessage': True, 'IsFixedSize': True, 'HasHeader': False}
// {'zed_wrapper': ['/home/hyeok/workspace/catkin_ws/src/zed-ros-wrapper/zed_wrapper/msg'], 'std_msgs': ['/home/hyeok/ros_catkin_ws/install/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/home/hyeok/ros_catkin_ws/install/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsMessage< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "89bb254424e4cffedbf494e7b0ddbfea";
  }

  static const char* value(const ::zed_wrapper::set_led_statusResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x89bb254424e4cffeULL;
  static const uint64_t static_value2 = 0xdbf494e7b0ddbfeaULL;
};

template<class ContainerAllocator>
struct DataType< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "zed_wrapper/set_led_statusResponse";
  }

  static const char* value(const ::zed_wrapper::set_led_statusResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool done\n"
"\n"
;
  }

  static const char* value(const ::zed_wrapper::set_led_statusResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.done);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct set_led_statusResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::zed_wrapper::set_led_statusResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::zed_wrapper::set_led_statusResponse_<ContainerAllocator>& v)
  {
    s << indent << "done: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.done);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ZED_WRAPPER_MESSAGE_SET_LED_STATUSRESPONSE_H
