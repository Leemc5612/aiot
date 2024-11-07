#include <chrono>
#include <iostream>

using namespace std;
using namespace std::chrono_literals;

class HellowPublisher : public rclcpp::Node
{
public:
    HellowPublisher();

private:
    int _count;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr _pub;
    rclcpp::TimerBase::SharedPtr _timer;
    void printHello();
};

#endif // __HELLO_PUB_CLASS_HPP__
using namespace std;
using namespace std::chrono_literals;
void printHello();

int main()
{
    rclcpp::init(0, nullptr);
    // node = Node("hello")
    auto node = std::make_shared<rclcpp::Node>("hello");
    auto timer = node ->create_wall_timer(1s, printHello);
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;


}

void printHello(){
    static int count;
    cout << "Hello, World!!!!!!" <<count<< endl;
    count++;
}
HellowPublisher::HellowPublisher()
    : Node("hello"), _count(0)
{
    _pub = create_publisher<std_msgs::msg::String>("message", 10);
    _timer = create_wall_timer(1s, std::bind(&HellowPublisher::printHello, this));
}

void HellowPublisher::printHello()
{
    auto msg = std_msgs::msg::String();
    msg.data = "Hello, World!!!!! " + to_string(_count);
    _pub->publish(msg);
    RCLCPP_INFO(get_logger(), msg.data.c_str());
    _count++;
}