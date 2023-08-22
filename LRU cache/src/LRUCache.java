import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;

public class LRUCache {
    
    private HashSet<Integer> set;
    private Deque<Integer> list;
    private final int CACHE_SIZE;

    public LRUCache(int capacity){
        set = new HashSet<>();
        list = new LinkedList<>();
        CACHE_SIZE = capacity;
    }

    public void set (int value){
        if (!set.contains(value)){
            if (list.size() == CACHE_SIZE){
                int last = list.removeLast();
                set.remove(last);
            }
        }
        else{
            list.remove(value);
        }
        list.push(value);
        set.add(value);
    }

    public void display(){

        Iterator<Integer> itr = list.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next() + " ");
        }
    }

}
