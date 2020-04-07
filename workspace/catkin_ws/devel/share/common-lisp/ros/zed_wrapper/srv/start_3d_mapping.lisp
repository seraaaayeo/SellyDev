; Auto-generated. Do not edit!


(cl:in-package zed_wrapper-srv)


;//! \htmlinclude start_3d_mapping-request.msg.html

(cl:defclass <start_3d_mapping-request> (roslisp-msg-protocol:ros-message)
  ((resolution
    :reader resolution
    :initarg :resolution
    :type cl:fixnum
    :initform 0)
   (fused_pointcloud_freq
    :reader fused_pointcloud_freq
    :initarg :fused_pointcloud_freq
    :type cl:float
    :initform 0.0))
)

(cl:defclass start_3d_mapping-request (<start_3d_mapping-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <start_3d_mapping-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'start_3d_mapping-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name zed_wrapper-srv:<start_3d_mapping-request> is deprecated: use zed_wrapper-srv:start_3d_mapping-request instead.")))

(cl:ensure-generic-function 'resolution-val :lambda-list '(m))
(cl:defmethod resolution-val ((m <start_3d_mapping-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader zed_wrapper-srv:resolution-val is deprecated.  Use zed_wrapper-srv:resolution instead.")
  (resolution m))

(cl:ensure-generic-function 'fused_pointcloud_freq-val :lambda-list '(m))
(cl:defmethod fused_pointcloud_freq-val ((m <start_3d_mapping-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader zed_wrapper-srv:fused_pointcloud_freq-val is deprecated.  Use zed_wrapper-srv:fused_pointcloud_freq instead.")
  (fused_pointcloud_freq m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <start_3d_mapping-request>) ostream)
  "Serializes a message object of type '<start_3d_mapping-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'resolution)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'fused_pointcloud_freq))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <start_3d_mapping-request>) istream)
  "Deserializes a message object of type '<start_3d_mapping-request>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'resolution)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'fused_pointcloud_freq) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<start_3d_mapping-request>)))
  "Returns string type for a service object of type '<start_3d_mapping-request>"
  "zed_wrapper/start_3d_mappingRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'start_3d_mapping-request)))
  "Returns string type for a service object of type 'start_3d_mapping-request"
  "zed_wrapper/start_3d_mappingRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<start_3d_mapping-request>)))
  "Returns md5sum for a message object of type '<start_3d_mapping-request>"
  "2df5cb98d96e7a58c7ef767c8c254cf9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'start_3d_mapping-request)))
  "Returns md5sum for a message object of type 'start_3d_mapping-request"
  "2df5cb98d96e7a58c7ef767c8c254cf9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<start_3d_mapping-request>)))
  "Returns full string definition for message of type '<start_3d_mapping-request>"
  (cl:format cl:nil "~%~%~%uint8 resolution~%~%~%float32 fused_pointcloud_freq~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'start_3d_mapping-request)))
  "Returns full string definition for message of type 'start_3d_mapping-request"
  (cl:format cl:nil "~%~%~%uint8 resolution~%~%~%float32 fused_pointcloud_freq~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <start_3d_mapping-request>))
  (cl:+ 0
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <start_3d_mapping-request>))
  "Converts a ROS message object to a list"
  (cl:list 'start_3d_mapping-request
    (cl:cons ':resolution (resolution msg))
    (cl:cons ':fused_pointcloud_freq (fused_pointcloud_freq msg))
))
;//! \htmlinclude start_3d_mapping-response.msg.html

(cl:defclass <start_3d_mapping-response> (roslisp-msg-protocol:ros-message)
  ((done
    :reader done
    :initarg :done
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass start_3d_mapping-response (<start_3d_mapping-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <start_3d_mapping-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'start_3d_mapping-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name zed_wrapper-srv:<start_3d_mapping-response> is deprecated: use zed_wrapper-srv:start_3d_mapping-response instead.")))

(cl:ensure-generic-function 'done-val :lambda-list '(m))
(cl:defmethod done-val ((m <start_3d_mapping-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader zed_wrapper-srv:done-val is deprecated.  Use zed_wrapper-srv:done instead.")
  (done m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <start_3d_mapping-response>) ostream)
  "Serializes a message object of type '<start_3d_mapping-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'done) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <start_3d_mapping-response>) istream)
  "Deserializes a message object of type '<start_3d_mapping-response>"
    (cl:setf (cl:slot-value msg 'done) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<start_3d_mapping-response>)))
  "Returns string type for a service object of type '<start_3d_mapping-response>"
  "zed_wrapper/start_3d_mappingResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'start_3d_mapping-response)))
  "Returns string type for a service object of type 'start_3d_mapping-response"
  "zed_wrapper/start_3d_mappingResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<start_3d_mapping-response>)))
  "Returns md5sum for a message object of type '<start_3d_mapping-response>"
  "2df5cb98d96e7a58c7ef767c8c254cf9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'start_3d_mapping-response)))
  "Returns md5sum for a message object of type 'start_3d_mapping-response"
  "2df5cb98d96e7a58c7ef767c8c254cf9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<start_3d_mapping-response>)))
  "Returns full string definition for message of type '<start_3d_mapping-response>"
  (cl:format cl:nil "bool done~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'start_3d_mapping-response)))
  "Returns full string definition for message of type 'start_3d_mapping-response"
  (cl:format cl:nil "bool done~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <start_3d_mapping-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <start_3d_mapping-response>))
  "Converts a ROS message object to a list"
  (cl:list 'start_3d_mapping-response
    (cl:cons ':done (done msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'start_3d_mapping)))
  'start_3d_mapping-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'start_3d_mapping)))
  'start_3d_mapping-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'start_3d_mapping)))
  "Returns string type for a service object of type '<start_3d_mapping>"
  "zed_wrapper/start_3d_mapping")