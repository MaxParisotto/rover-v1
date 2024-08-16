#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"

class ExplorationNode : public rclcpp::Node
{
public:
    ExplorationNode()
        : Node("exploration_node")
    {
        cmd_pub_ = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel", 10);
        scan_sub_ = this->create_subscription<sensor_msgs::msg::LaserScan>(
            "scan", 10, std::bind(&ExplorationNode::scan_callback, this, std::placeholders::_1));
        
        timer_ = this->create_wall_timer(
            500ms, std::bind(&ExplorationNode::timer_callback, this));
    }

private:
    void scan_callback(const sensor_msgs::msg::LaserScan::SharedPtr msg)
    {
        // Analyze scan data to avoid obstacles or find frontiers
        // This is where you'd implement the exploration logic
    }

    void timer_callback()
    {
        auto cmd_msg = geometry_msgs::msg::Twist();

        // For now, just move forward continuously
        cmd_msg.linear.x = 0.2;
        cmd_pub_->publish(cmd_msg);
    }

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_pub_;
    rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr scan_sub_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ExplorationNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}