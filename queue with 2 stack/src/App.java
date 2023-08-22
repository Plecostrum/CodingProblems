import java.util.Stack;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        
        queue<Integer> queue = new queue<>();

        for (int i = 0; i < 5; i++) {
            System.out.println(i);
            queue.enque(i);
        }
        for (int i = 0; i < 5; i++) {
            System.out.println(queue.deque());
        }
        

        

    }
}
