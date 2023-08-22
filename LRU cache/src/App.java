public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");

        LRUCache cache = new LRUCache(3);
        cache.set(1);
        cache.set(2);
        cache.set(3);
        cache.set(4);
        cache.set(5);
        cache.set(1);
        cache.set(2);
        cache.display();

    }
}
