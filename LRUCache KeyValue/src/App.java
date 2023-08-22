public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");

        int n = 4;
        LRUCache LRU = new LRUCache(n);
        LRU.set('A',1);
        LRU.set('B',13);
        LRU.set('C',67);
        LRU.set('D',4);
        LRU.set('E',23);
        System.out.println(LRU.get('E'));
        LRU.set('F',49);
        LRU.set('J',69);
        System.out.println(LRU.get('A'));
    }
}
