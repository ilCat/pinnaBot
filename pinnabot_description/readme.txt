instrucciones de uso
------------------------------------------------------------------------
*Para correr launch de rviz
    roslaunch pinnabot_description rviz.launch

*Para correr launch de gazebo
    roslaunch pinnabot_description spawn.launch

*Para abrir gazebo
    rosrun gazebo_ros gazebo

*Para correr control de teclado
    rosrun teleop_twist_keyboard teleop_twist_keyboard.py

    Reading from the keyboard  and Publishing to Twist!
        ---------------------------
        Moving around:
        u    i    o
        j    k    l
        m    ,    .

        For Holonomic mode (strafing), hold down the shift key:
        ---------------------------
        U    I    O
        J    K    L
        M    <    >

        t : up (+z)
        b : down (-z)

        anything else : stop

        q/z : increase/decrease max speeds by 10%
        w/x : increase/decrease only linear speed by 10%
        e/c : increase/decrease only angular speed by 10%

*Para ver la imagen de la cámara
    En Rviz, agregar una ''Camera'' ir a  ''Image Topic'' y selesccionar  /rrbot/camera1/image_raw
    o
    En otra pantalla:
        rosrun image_view image_view image:=/Pinna_bot/camera1/image_raw