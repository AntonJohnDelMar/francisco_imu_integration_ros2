from rclpy.node import Node
import rclpy

from francisco_imu.imu import ArtemisOpenLog as AOL


class imuNode(Node):
	def __init__(self):
		super().__init__("imu_node");
		theSerialPort = "/dev/ttyUSB0";
		self.imuArtemis = AOL(theSerialPort, 115200, 1);
		 
		self.create_timer(0.1, self.get_imu_data); 


	def get_imu_data(self):
		theEuler, theAccel, theGyro = self.imuArtemis.run();
		self.get_logger().info(f"Gyro: {theGyro}, Accel: {theAccel}");
		

def main(args = None):
	rclpy.init(args = args);
	
	theImuNode = imuNode();
	
	rclpy.spin(theImuNode);
	
	theImuNode.destroy_node();
	rclpy.shutdown();


if __name__ == '__main__':
	main(); 
