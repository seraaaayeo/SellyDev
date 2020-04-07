;; Auto-generated. Do not edit!


(when (boundp 'zed_wrapper::start_3d_mapping)
  (if (not (find-package "ZED_WRAPPER"))
    (make-package "ZED_WRAPPER"))
  (shadow 'start_3d_mapping (find-package "ZED_WRAPPER")))
(unless (find-package "ZED_WRAPPER::START_3D_MAPPING")
  (make-package "ZED_WRAPPER::START_3D_MAPPING"))
(unless (find-package "ZED_WRAPPER::START_3D_MAPPINGREQUEST")
  (make-package "ZED_WRAPPER::START_3D_MAPPINGREQUEST"))
(unless (find-package "ZED_WRAPPER::START_3D_MAPPINGRESPONSE")
  (make-package "ZED_WRAPPER::START_3D_MAPPINGRESPONSE"))

(in-package "ROS")





(defclass zed_wrapper::start_3d_mappingRequest
  :super ros::object
  :slots (_resolution _fused_pointcloud_freq ))

(defmethod zed_wrapper::start_3d_mappingRequest
  (:init
   (&key
    ((:resolution __resolution) 0)
    ((:fused_pointcloud_freq __fused_pointcloud_freq) 0.0)
    )
   (send-super :init)
   (setq _resolution (round __resolution))
   (setq _fused_pointcloud_freq (float __fused_pointcloud_freq))
   self)
  (:resolution
   (&optional __resolution)
   (if __resolution (setq _resolution __resolution)) _resolution)
  (:fused_pointcloud_freq
   (&optional __fused_pointcloud_freq)
   (if __fused_pointcloud_freq (setq _fused_pointcloud_freq __fused_pointcloud_freq)) _fused_pointcloud_freq)
  (:serialization-length
   ()
   (+
    ;; uint8 _resolution
    1
    ;; float32 _fused_pointcloud_freq
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _resolution
       (write-byte _resolution s)
     ;; float32 _fused_pointcloud_freq
       (sys::poke _fused_pointcloud_freq (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _resolution
     (setq _resolution (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _fused_pointcloud_freq
     (setq _fused_pointcloud_freq (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass zed_wrapper::start_3d_mappingResponse
  :super ros::object
  :slots (_done ))

(defmethod zed_wrapper::start_3d_mappingResponse
  (:init
   (&key
    ((:done __done) nil)
    )
   (send-super :init)
   (setq _done __done)
   self)
  (:done
   (&optional __done)
   (if __done (setq _done __done)) _done)
  (:serialization-length
   ()
   (+
    ;; bool _done
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _done
       (if _done (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _done
     (setq _done (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass zed_wrapper::start_3d_mapping
  :super ros::object
  :slots ())

(setf (get zed_wrapper::start_3d_mapping :md5sum-) "2df5cb98d96e7a58c7ef767c8c254cf9")
(setf (get zed_wrapper::start_3d_mapping :datatype-) "zed_wrapper/start_3d_mapping")
(setf (get zed_wrapper::start_3d_mapping :request) zed_wrapper::start_3d_mappingRequest)
(setf (get zed_wrapper::start_3d_mapping :response) zed_wrapper::start_3d_mappingResponse)

(defmethod zed_wrapper::start_3d_mappingRequest
  (:response () (instance zed_wrapper::start_3d_mappingResponse :init)))

(setf (get zed_wrapper::start_3d_mappingRequest :md5sum-) "2df5cb98d96e7a58c7ef767c8c254cf9")
(setf (get zed_wrapper::start_3d_mappingRequest :datatype-) "zed_wrapper/start_3d_mappingRequest")
(setf (get zed_wrapper::start_3d_mappingRequest :definition-)
      "


uint8 resolution


float32 fused_pointcloud_freq

---
bool done

")

(setf (get zed_wrapper::start_3d_mappingResponse :md5sum-) "2df5cb98d96e7a58c7ef767c8c254cf9")
(setf (get zed_wrapper::start_3d_mappingResponse :datatype-) "zed_wrapper/start_3d_mappingResponse")
(setf (get zed_wrapper::start_3d_mappingResponse :definition-)
      "


uint8 resolution


float32 fused_pointcloud_freq

---
bool done

")



(provide :zed_wrapper/start_3d_mapping "2df5cb98d96e7a58c7ef767c8c254cf9")


