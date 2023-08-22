import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

public class LRUCache {

    private HashMap<Character,Node> tracker;
    Node headNode;
    Node tailNode;
    private final int CACHE_SIZE;

    public LRUCache(int capacity) {
        tracker = new HashMap<Character,Node>();
        CACHE_SIZE = capacity;
    }

    private void add(Node node){
        node.nextNode = headNode;
        node.prevNode = tailNode;
        if (headNode !=null){
            headNode.prevNode = node;
        }
        headNode = node;
        if (tailNode ==null){
            tailNode = headNode;
        }
    }
    private void remove(Node node){
        if(node.prevNode != null){
            node.prevNode.nextNode = node.nextNode;
        }
        else{
            headNode = node.nextNode;
        }
        if(node.nextNode!= null){
           node.nextNode.prevNode = node.prevNode; 
        }
        else{
            tailNode = node.prevNode;
        }
        
        
    }

    public void set(char key, int value){
        if(tracker.containsKey(key)){
            Node node = tracker.get(key);
            node.value = value;
            remove(node);
            add(node);
        }
        else {
            Node node = new Node(key,value);            
            if(tracker.size()>CACHE_SIZE){
                tracker.remove(tailNode.key);
                remove(tailNode);
                add(node);
            }
            else{
                add(node);
            }
            tracker.put(key, node);
        }
    }
        
    public int get(char key){
        if (tracker.containsKey(key)){
            Node node = tracker.get(key);
            remove(node);
            add(node);
            return (node.value);
        }
        return -1;
    }


    

}
